# Vídeo animado estilo Vox com o Claude, de graça

Testado em 23/11/2026 num computador Linux com Node 22 e o HyperFrames 0.9.84. O vídeo do disquete (25 s, vertical) saiu deste passo a passo; o projeto inteiro está em [`exemplo-disquete/`](exemplo-disquete/).

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta vazia e cole:

```text
Instala e roda pra mim a skill video-estilo-vox do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois faz um vídeo estilo Vox de 25 segundos, vertical, sobre por que o botão de salvar ainda é um disquete, confere os quadros e me entrega o MP4.
```

Ele instala o HyperFrames, monta o vídeo, confere os quadros (texto encavalado, ícone errado, número sem fonte) e renderiza. Troque o tema pelo seu.

## O que você precisa
- Claude Code (ou Codex, Cursor) instalado e logado.
- Node.js 22 ou mais novo e o FFmpeg.
- Nada pago: o HyperFrames é aberto (licença Apache-2.0) e o render roda no seu computador.

## Na mão: os 2 comandos (dentro da pasta do seu vídeo)

1. HyperFrames no Claude:
```
npx skills add heygen-com/hyperframes -a claude-code -y
```
2. A skill de vídeo estilo Vox (vox-explainer, da coleção oficial de skills da comunidade do HyperFrames):
```
npx skills add heygen-com/hyperframes-community-skills --skill vox-explainer -a claude-code -y
```
Os dois copiam as skills pra `.claude/skills/` da pasta. Abra o Claude Code nessa pasta depois de instalar (skill nova só carrega em sessão nova).

## O prompt do meu vídeo (o do disquete)

> Usa a skill vox-explainer e faz um explicativo estilo Vox de 25 segundos, vertical 1080x1920, sobre por que o botão de salvar ainda é um disquete. Tudo em português. Sem locução e sem nenhuma API paga: só texto na tela, colagem e animação. Pode pular as aprovações e decidir sozinho. Monta o projeto HyperFrames nesta pasta e roda o lint.

Depois, pra ver e pra gerar o MP4:
```
npx hyperframes snapshot --at 2,7,13,18,23   # quadros parados pra conferir antes
npx hyperframes render -o out/meu-video.mp4  # o MP4
```
No meu teste o render de 25 s levou 19,6 s.

## O que dá errado e como resolver (aconteceu aqui)
- **Texto encavalado:** título grande quebra em 3 linhas e passa por cima do de baixo. Peça: "confere os quadros do snapshot e arruma texto sobreposto e texto saindo da tela". Foi a 2ª rodada do meu.
- **Ícone desenhado errado:** o disquete saiu parecendo um "H". Peça pra ele redesenhar olhando o snapshot.
- **Informação inventada:** na 1ª versão a grade de ícones tinha nome de app que nem tem botão de disquete. Confira todo nome e número que aparece na tela antes de postar.
- O `lint` mostra avisos de "sub-composição": não impedem o render.

## Custo real
- HyperFrames e skill: R$ 0.
- Render no seu computador: R$ 0 (o meu de 25 s levou 19,6 s).
- O Claude: o que já está no seu plano.
- Locução: opcional. A skill pergunta antes de usar qualquer voz paga (diz o serviço e o custo antes da chamada).

## 10 temas que funcionam nesse estilo (coisa que todo mundo vê e nunca reparou)
1. Por que o botão de salvar ainda é um disquete.
2. Por que o teclado é QWERTY e não ABC.
3. Por que o "@" virou o símbolo do e-mail.
4. Por que a tomada brasileira tem 3 pinos.
5. Por que todo app de banco é roxo, laranja ou vermelho.
6. Por que o ícone de telefone é um gancho que ninguém mais usa.
7. Por que a nota de 200 reais tem um lobo-guará.
8. Por que o Wi-Fi tem esse símbolo de leque.
9. Por que todo carro novo é branco, preto ou prata.
10. Por que o Pix pegou e o DOC sumiu.

Prompt base pra qualquer um deles: "Usa a skill vox-explainer e faz um explicativo estilo Vox de 30 segundos, vertical 1080x1920, sobre <tema>. Tudo em português, com fonte pra todo número que aparecer na tela."

## O próximo passo

O próximo passo depois disso é o vídeo nem precisar de você na frente da câmera. Foi com esse mesmo Claude que eu criei o Seu João, um senhor que não existe e posta todo dia sem eu aparecer. [Gravei uma aula mostrando como montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=video-estilo-vox)
