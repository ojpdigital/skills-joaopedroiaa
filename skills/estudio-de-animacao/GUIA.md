# Estúdio de animação no Claude Code, com 3 skills grátis

São 3 skills grátis e de código aberto que, juntas, fazem o Claude Code sair de uma ideia pra um vídeo animado com narração, música e efeito, sem você abrir editor. As skills são grátis; o Claude Code precisa de uma conta do Claude com plano que inclua o Claude Code.

- **Lemo Opuscar** ([github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)): 99 estilos de filme, do quadro branco explicativo ao desenho animado e à aquarela. Você dá a ideia; ele escreve a história, desenha as cenas, narra e põe trilha. Tudo feito em código, sem gerador de vídeo. [Galeria dos estilos](https://lemomo-ai.github.io/lemo-opuscar/).
- **Blender Skills** ([github.com/arjun988/blender-skills](https://github.com/arjun988/blender-skills)): 94 skills que fazem o Claude mexer no Blender por você (modelo 3D, cena, animação), pelo Blender MCP.
- **Earshot** ([github.com/Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)): dá ouvido pro Claude. Efeitos sonoros feitos em código: um banco de 252 efeitos de filme, e ele cria um novo se faltar.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill estudio-de-animacao do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois faz o meu primeiro vídeo animado.
```

Ele confere o que a sua máquina tem, pergunta quais das 3 você quer, instala e já faz um vídeo de 30 segundos com você.

## Na mão
Precisa do Claude Code, do Python 3.10 ou mais novo, do ffmpeg e do git. O Blender (grátis, blender.org) só pra terceira skill.

1. Opuscar, no terminal:
```bash
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```
2. Earshot:
```bash
python3 -m venv ~/.earshot && ~/.earshot/bin/pip install "earshot @ git+https://github.com/Leonxlnx/earshot"
~/.earshot/bin/earshot make "a soft whoosh for a card transition" -o whoosh.wav
```
(No Windows: `py -m venv %USERPROFILE%\.earshot` e `%USERPROFILE%\.earshot\Scripts\pip install "earshot @ git+https://github.com/Leonxlnx/earshot"`.) E dentro do Claude Code: `/plugin marketplace add Leonxlnx/earshot` e `/plugin install earshot@earshot`.
3. Blender Skills: este é o mais difícil na mão; prefira o jeito fácil acima. Precisa do Blender, do addon do Blender MCP e do uv (docs.astral.sh/uv). Depois: `claude mcp add blender -- uvx blender-mcp` (Windows: `claude mcp add blender -- cmd /c uvx --python 3.11 blender-mcp`) e copie a pasta oculta `.claude/skills` do repositório pra pasta do seu projeto.
4. Peça: "Faz um filme de 30 segundos no estilo watercolor sobre <seu assunto>. Narração calma em português."

## O meu teste (26/11/2026)
- Clonei os 3 repositórios e conferi os números na fonte: 99 estilos no Opuscar, 94 skills no Blender Skills, 252 efeitos no banco do Earshot.
- Instalei o Earshot e gerei dois sons com ele (um whoosh e um ding): o whoosh das trocas de tela do meu vídeo saiu daí.
- O que eu não testei: um filme inteiro do Opuscar e o Blender pelo MCP. Os dois rodam no seu Claude Code logado e no seu Blender; a minha máquina de teste não tinha nenhum dos dois. Então: testei o Earshot gerando som pelo terminal. Dos outros dois, li o código e os comandos de instalação, mas não instalei nem rodei.

## Bom saber
- O autor do Opuscar diz que os estilos saem melhor com o Claude no esforço alto (digite `/effort high`), que gasta mais do limite do seu plano.
- Algumas funções extras do Blender MCP (modelos prontos da Sketchfab, Hyper3D) usam chave de serviço próprio. O básico roda sem nada pago.

## O próximo passo
Com isso você faz o vídeo sem abrir editor. O que eu faço é dar um passo além: o vídeo nem precisa de mim. Foi com o Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=estudio-de-animacao)
