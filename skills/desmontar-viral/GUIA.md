# Desmonta qualquer vídeo viral, cena por cena

**rea-video**, de JuneYaooo: grátis, licença Apache-2.0, roda no Claude Code (e no Codex).
Link: https://github.com/JuneYaooo/rea-video

## O que ele te dá
- Cada cena do vídeo: filmada, feita com IA, montada em código ou tela gravada, com a % de certeza.
- O roteiro frase por frase com o tempo, as legendas (sai até o arquivo .srt), os cortes e os efeitos sonoros.
- Um relatório (report.html) e o plano pra refazer: o que gravar, o que gerar e o que montar.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code na pasta onde está o vídeo e cole:

```text
Instala e roda pra mim a skill desmontar-viral do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois desmonta este vídeo cena por cena e me dá o plano pra refazer no mesmo ritmo: <caminho do vídeo.mp4>
```

## Instalar na mão

O jeito que o autor ensina (eu não testei este): no Claude Code, cola
> Instala https://github.com/JuneYaooo/rea-video e depois desmonta este vídeo: /caminho/do/video.mp4

Ou como plugin:
```
claude plugin marketplace add JuneYaooo/rea-video
claude plugin install rea-video@rea-video
```

O jeito que eu testei em 22/11 (precisa de Python 3.10+ e ffmpeg):
```bash
git clone https://github.com/JuneYaooo/rea-video
python3 -m venv rea && rea/bin/pip install "./rea-video[ocr]"
rea/bin/rea-video decompose viral.mp4 -o saida --lang en
rea/bin/rea-video summary saida/breakdown.json
```
Na 1ª vez ele baixa uns 216 MB de modelos pra separar voz, música e efeitos. Levou 7 minutos num vídeo de 37 s.

Dica: dá pra ligar um modelo que vê vídeo (o Gemini serve) pra ele acertar mais o que é filmado e o que é IA. Sem ele também roda.

## O que deu no vídeo que eu desmontei (o reel do próprio plugin, 37 s)
- 13 cenas, 2,9 s cada em média, 19 cortes por minuto.
- 42% filmado, 40% montado em código, 19% tela gravada.
- 23 legendas com tempo, 21 efeitos sonoros (11 sons diferentes), voz gravada de verdade e música de biblioteca.
- O plano pra refazer: 3 cenas pra gravar e 1 projeto de código pras telas.

## Pra que eu uso
Antes de modelar um viral, eu desmonto ele: vejo onde estão os cortes, quanto tempo cada tela fica e onde entra cada efeito. Aí eu refaço com o meu conteúdo, no mesmo ritmo.

Foi assim que eu montei os vídeos do Seu João, um personagem que eu criei com IA e que posta todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=desmontar-viral)
