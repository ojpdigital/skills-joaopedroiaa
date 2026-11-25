#!/usr/bin/env python3
"""Organiza galeria de fotos com o Claude, sem mexer nos originais. Só biblioteca padrão + Pillow (pip install pillow).

  python3 organizar.py folhas  GALERIA SAIDA            separa vídeos e duplicadas, gera folhas de 16 miniaturas
  python3 organizar.py aplicar GALERIA SAIDA rotulos.json  mostra quantas vão pra cada pasta (não copia)
  python3 organizar.py aplicar GALERIA SAIDA rotulos.json --copiar   copia (os originais ficam onde estão)
  python3 organizar.py procurar SAIDA praia              acha pelas tags
  python3 organizar.py --autoteste
"""
import csv, hashlib, json, shutil, subprocess, sys
from collections import Counter
from pathlib import Path

IMG = {'.jpg', '.jpeg', '.png', '.webp', '.heic'}
VID = {'.mp4', '.mov', '.m4v', '.avi', '.mkv'}
FOLHA = 16  # 4x4
MINI = 256


def varrer(galeria):
    """-> (imagens a rotular, vídeos, duplicadas[(arquivo, igual_a)]). Duplicada = mesmo conteúdo (sha256), fica a de nome menor."""
    vistos, imgs, vids, dups = {}, [], [], []
    base = Path(galeria)
    for p in sorted(base.rglob('*')):  # entra nas subpastas (Google Fotos/Takeout, álbuns); nomes = caminho relativo
        ext = p.suffix.lower(); nome = p.relative_to(base).as_posix()
        if not p.is_file() or (ext not in IMG and ext not in VID):
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h in vistos:
            dups.append((nome, vistos[h]))
        else:
            vistos[h] = nome
            (vids if ext in VID else imgs).append(nome)
    if not (imgs or vids or dups):
        sys.exit(f'ERRO: nenhuma imagem nem vídeo em {galeria} (nem nas subpastas). Confira o caminho e se os arquivos são {sorted(IMG | VID)}.')
    return imgs, vids, dups


def folhas(galeria, saida):
    from PIL import Image, ImageDraw, ImageOps
    try:
        import pillow_heif; pillow_heif.register_heif_opener()
    except ImportError:
        pass
    imgs, vids, dups = varrer(galeria)
    out = Path(saida); (out / 'folhas').mkdir(parents=True, exist_ok=True)
    indice = {}
    for k in range(0, len(imgs), FOLHA):
        lote = imgs[k:k + FOLHA]
        nome = f'folha-{k // FOLHA + 1:03d}'
        folha = Image.new('RGB', (4 * MINI, 4 * MINI), 'white')
        for i, nm in enumerate(lote):
            try:
                im = ImageOps.exif_transpose(Image.open(Path(galeria) / nm)).convert('RGB')
            except Exception:
                im = Image.new('RGB', (MINI, MINI), 'gray')
            im = ImageOps.fit(im, (MINI - 4, MINI - 4))
            x, y = (i % 4) * MINI, (i // 4) * MINI
            folha.paste(im, (x + 2, y + 2))
            d = ImageDraw.Draw(folha); d.rectangle((x + 2, y + 2, x + 40, y + 28), fill='black')
            d.text((x + 8, y + 8), str(i + 1), fill='yellow')
        folha.save(out / 'folhas' / f'{nome}.jpg', quality=82)
        indice[nome] = lote
    (out / 'indice.json').write_text(json.dumps({'folhas': indice, 'videos': vids, 'duplicadas': dups}, ensure_ascii=False, indent=1))
    print(f'{len(imgs)} imagens em {len(indice)} folhas · {len(vids)} vídeos · {len(dups)} duplicadas ({len(imgs) + len(vids) + len(dups)} arquivos)')


def plano(indice, rotulos):
    """-> {arquivo: (pasta, tags)} para imagens + vídeos + duplicadas; arquivo sem rótulo vai pra 'sem-rotulo'."""
    res = {}
    for folha, lote in indice['folhas'].items():
        r = {x['n']: x for x in rotulos.get(folha, [])}
        for i, nm in enumerate(lote, 1):
            x = r.get(i)
            res[nm] = (x['pasta'], x.get('tags', [])) if x else ('sem-rotulo', [])
    for nm in indice['videos']:
        res[nm] = ('videos', [])
    for nm, _ in indice['duplicadas']:
        res[nm] = ('duplicadas', [])
    return res


def aplicar(galeria, saida, rotulos_json, copiar=False):
    out = Path(saida); indice = json.loads((out / 'indice.json').read_text())
    pl = plano(indice, json.loads(Path(rotulos_json).read_text()))
    cont = Counter(p for p, _ in pl.values())
    for pasta, n in sorted(cont.items(), key=lambda kv: -kv[1]):
        print(f'{n:6d}  {pasta}')
    print(f'{len(pl)} arquivos em {len(cont)} pastas')
    if cont.get('sem-rotulo'):
        print(f"ATENÇÃO: {cont['sem-rotulo']} arquivos SEM RÓTULO: o Claude não respondeu essas folhas (limite do plano ou erro). "
              'Rode ./rotular.sh de novo: ele só refaz os lotes que faltam. Só copie quando esse número for 0.', file=sys.stderr)
    if not copiar:
        print('(nada foi copiado; rode de novo com --copiar)'); return pl
    with open(out / 'tags.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['arquivo', 'pasta', 'tags'])
        for nm, (pasta, tags) in pl.items():
            (out / 'organizada' / pasta).mkdir(parents=True, exist_ok=True)
            shutil.copy2(Path(galeria) / nm, out / 'organizada' / pasta / nm.replace('/', '__'))  # copia (nome achatado: subpastas não colidem); o original não sai do lugar
            w.writerow([nm, pasta, ' '.join(tags)])
    print(f'copiado para {out / "organizada"}; tags em {out / "tags.csv"}')
    return pl


def procurar(saida, termo):
    for l in csv.DictReader(open(Path(saida) / 'tags.csv')):
        if termo.lower() in (l['tags'] + ' ' + l['arquivo']).lower():
            print(l['pasta'] + '/' + l['arquivo'], '|', l['tags'])


def autoteste():
    import tempfile
    from PIL import Image
    with tempfile.TemporaryDirectory() as t:
        g = Path(t) / 'g'; g.mkdir()
        for n, c in (('a.jpg', 'red'), ('b.jpg', 'red'), ('c.png', 'blue')):
            Image.new('RGB', (40, 30), c).save(g / n)
        (g / 'v.mp4').write_bytes(b'x'); (g / 'nota.txt').write_text('x')
        imgs, vids, dups = varrer(g)
        assert imgs == ['a.jpg', 'c.png'] and vids == ['v.mp4'] and dups == [('b.jpg', 'a.jpg')], (imgs, vids, dups)
        folhas(g, Path(t) / 's')
        rot = Path(t) / 'r.json'; rot.write_text(json.dumps({'folha-001': [{'n': 1, 'pasta': 'cores', 'tags': ['vermelho']}]}))
        pl = aplicar(g, Path(t) / 's', rot, copiar=True)
        assert pl['c.png'][0] == 'sem-rotulo' and pl['b.jpg'][0] == 'duplicadas'
        sub = Path(t) / 'g3' / 'Takeout' / 'Google Fotos' / 'Fotos de 2023'; sub.mkdir(parents=True); Image.new('RGB', (40, 30), 'green').save(sub / 'IMG_1.jpg'); Image.new('RGB', (40, 30), 'green').save(Path(t) / 'g3' / 'IMG_1.jpg')
        i3, _, d3 = varrer(Path(t) / 'g3'); assert sorted(i3 + [x for x, _ in d3]) == ['IMG_1.jpg', 'Takeout/Google Fotos/Fotos de 2023/IMG_1.jpg'], (i3, d3)  # subpasta e mesmo nome sem colidir
        r = subprocess.run([sys.executable, __file__, 'folhas', str(Path(t) / 'vazia-que-nao-existe'), str(Path(t) / 's9')], capture_output=True, text=True); assert r.returncode != 0 and 'ERRO' in (r.stderr + r.stdout)  # pasta sem imagem falha alto
        assert (g / 'a.jpg').exists() and (Path(t) / 's/organizada/cores/a.jpg').exists()
    print('autoteste ok')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--autoteste']: autoteste()
    elif a[:1] == ['folhas']: folhas(a[1], a[2])
    elif a[:1] == ['aplicar']: aplicar(a[1], a[2], a[3], '--copiar' in a)
    elif a[:1] == ['procurar']: procurar(a[1], a[2])
    else: print(__doc__)
