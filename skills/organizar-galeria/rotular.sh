#!/usr/bin/env bash
# Passa as folhas pro Claude em lotes de 5 e junta os JSON em rotulos.json. Uso: rotular.sh SAIDA [paralelos=4]
# Lote que falha (limite do plano, erro, JSON incompleto) NÃO vira "pronto": o script avisa em voz alta, sai com erro e, se você
# rodar de novo, refaz só os lotes que faltam (os prontos ficam em SAIDA/rot/lote-NNN.json).
# Lote só conta como pronto se TODAS as miniaturas de cada folha tiverem resposta (conferido contra SAIDA/indice.json):
# quando o Claude pula uma miniatura, o lote não é gravado e é refeito na rodada seguinte.
set -uo pipefail
S=$1; PAR=${2:-4}; DIR=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$S/rot"
echo "$(ls "$S/folhas" | wc -l) folhas de 16 fotos, $PAR lotes de 5 ao mesmo tempo"
ls "$S/folhas" | sed 's/.jpg//' | xargs -n5 | nl -w3 -n rz | while read -r n lote; do echo "$n $lote"; done > "$S/rot/lotes.txt"
# confere a resposta contra o indice.json: cada folha do lote com todas as posições (1..16) respondidas
VAL='import json,re,sys
t=open(sys.argv[1]).read(); m=re.search(r"\{.*\}",t,re.S); d=json.loads(m.group(0)); ind=json.load(open(sys.argv[3]))["folhas"]
falta={f:[i for i in range(1,len(ind[f])+1) if i not in {x.get("n") for x in d.get(f,[])}] for f in sys.argv[4:]}
falta={f:v for f,v in falta.items() if v}
assert not falta, f"miniaturas sem resposta: {falta}"
json.dump(d,open(sys.argv[2],"w"),ensure_ascii=False)'
rodar() {
  n=$1; shift
  if [ -s "$S/rot/lote-$n.json" ]; then  # lote gravado por versão antiga pode estar incompleto: confere de novo
    python3 -c "$VAL" "$S/rot/lote-$n.json" "$S/rot/lote-$n.json" "$S/indice.json" "$@" 2>/dev/null && return 0
    rm -f "$S/rot/lote-$n.json"
  fi
  arqs=""; for f in "$@"; do arqs="$arqs $S/folhas/$f.jpg"; done
  if claude -p "$(cat "$DIR/PROMPT-MESTRE.md")

Folhas deste lote (abra cada uma com a ferramenta Read):$arqs" --allowedTools Read --output-format text > "$S/rot/lote-$n.raw" 2> "$S/rot/lote-$n.err" < /dev/null \
  && python3 -c "$VAL" "$S/rot/lote-$n.raw" "$S/rot/lote-$n.json" "$S/indice.json" "$@" 2>> "$S/rot/lote-$n.err"
  then echo "lote $n pronto: $1 a ${@: -1}"
  else rm -f "$S/rot/lote-$n.json"; echo "LOTE $n FALHOU ($1 a ${@: -1}): veja $S/rot/lote-$n.err e $S/rot/lote-$n.raw" >&2; fi
}
export -f rodar; export S DIR VAL
xargs -P "$PAR" -L1 bash -c 'rodar "$@"' _ < "$S/rot/lotes.txt"
python3 - "$S" <<'P'
import json,glob,sys
S=sys.argv[1]; esperados=[l.split()[0] for l in open(S+'/rot/lotes.txt')]
r={}
for f in sorted(glob.glob(S+'/rot/lote-*.json')): r.update(json.load(open(f)))
json.dump(r,open(S+'/rotulos.json','w'),ensure_ascii=False)
ok={f.split('lote-')[1][:3] for f in glob.glob(S+'/rot/lote-*.json')}; falt=[n for n in esperados if n not in ok]
print(len(r),'folhas rotuladas')
if falt:
    print(f'ATENÇÃO: {len(falt)} lote(s) SEM rótulo: {" ".join(falt)}. Os arquivos dessas folhas vão parar em "sem-rotulo". Rode ./rotular.sh {S} de novo (refaz só esses).',file=sys.stderr); sys.exit(1)
P
