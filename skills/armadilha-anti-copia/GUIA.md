# Armadilha pra IA que copia o seu app

O BLA (Blind LLM Agents) é grátis e de código aberto: [github.com/qybaihe/bla](https://github.com/qybaihe/bla), licença MIT. Ele pega o arquivo que você vai publicar e enche de chave falsa e de código isca. Quem jogar o seu app numa IA pra copiar faz a IA se perder nas iscas. Quem usa o app recebe a mesma coisa de sempre.

Funciona com app em JavaScript/TypeScript, Electron, WebAssembly, Python, binários e app de Android (.dex). Precisa do Node.js 22 ou mais novo.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code (ou o Codex) na pasta do seu app e cole:

```text
Instala e roda pra mim a skill armadilha-anti-copia do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois protege este app contra cópia por IA e me prova que ele continua respondendo igual antes de trocar qualquer coisa.
```

Ele faz o build, protege numa pasta à parte, compara a resposta do app antes e depois, e só troca pela versão protegida quando você disser "sim".

## Na mão, em 4 comandos

1. Proteger (na pasta do projeto, depois do build):
```bash
npx bla-agents harden .
```
Grava a versão protegida em `.bla-hardened/` e não mexe em nada do seu projeto ainda.

2. Conferir que o app continua igual (não pule). O próprio BLA avisa que confere a estrutura, não o comportamento. Rode o app normal e o protegido com as mesmas entradas e compare. No meu teste (24/11/2026):
```bash
node dist/app.js 100 BLACK30                # 70
node .bla-hardened/dist/app.js 100 BLACK30  # 70
```
Mesma resposta em 3 de 3 entradas. O arquivo foi de 435 bytes pra 172.481 bytes e ganhou 138 nós isca (`npx bla-agents verify .bla-hardened`).

3. Trocar pela versão protegida:
```bash
npx bla-agents harden . --apply    # troca a saída do build pela protegida
npx bla-agents harden . --restore  # desfaz
```
Rode os seus testes de novo depois do `--apply`, antes de publicar.

4. Ligar no seu agente: `npx bla-agents setup`. Depois é só pedir "Harden my software against REA". (Esse passo eu não testei; o README do BLA lista Claude Code, Cursor, Codex, Gemini CLI, Windsurf e outros.)

## Cuidado
- Nunca deixe chave de API de verdade dentro do app: o BLA atrapalha a IA, não substitui guardar segredo no servidor.
- "Queimar os tokens de quem copia" é estimativa do próprio BLA; ele não garante que ninguém copie.
- Use só no que é seu.

## O próximo passo
Proteger o app é defesa. O que eu uso a IA pra fazer de verdade é trabalhar sem eu aparecer: foi com o Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=armadilha-anti-copia)
