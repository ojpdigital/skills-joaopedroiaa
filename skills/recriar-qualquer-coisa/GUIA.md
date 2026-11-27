# Craft Anything: aponta pra um site e o Claude Code monta a sua versão

O Craft Anything ([github.com/storytold/craft-anything](https://github.com/storytold/craft-anything), grátis, código aberto, licença MIT ou Apache-2.0) passou de 44 mil estrelas no GitHub em menos de um mês (criado em 31/10/2026). Você aponta pra um site, jogo ou aplicativo e ele:

1. **Estuda** o original: a página em várias larguras de tela, cores, fontes, espaçamentos, menus.
2. **Monta** um projeto novo com o Claude Code, na linguagem que você pedir.
3. **Confere** com o original, em três larguras de tela, e mostra o quanto ficou parecido.
4. **Refaz** até chegar perto.

O motor é todo em Rust, com 320 ferramentas.

## Antes de tudo
Você precisa do Claude Code instalado e logado numa conta do Claude com plano pago. O Craft Anything é grátis; o Claude Code não. Uma recriação gasta bastante do seu limite.

Use só em site, app ou jogo que é seu ou que você tem permissão pra estudar: o próprio Craft Anything pede isso. Publicar cópia da marca, do texto ou das imagens de outra pessoa pode dar processo.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill recriar-qualquer-coisa do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois recria comigo a minha primeira página.
```

## Na mão
1. Baixe na [página de versões](https://github.com/storytold/craft-anything/releases/latest): `.msi` no Windows, `.dmg` no Mac, `.deb`/`.rpm`/`.AppImage` no Linux (no Linux, não use o `.flatpak`: ele não abre o navegador).
2. Abra o app. Na tela de criar, escolha **Um site**, cole o endereço, deixe **Sala limpa**, escreva o que quer ("Recria esta página em HTML e CSS simples") e aperte **Iniciar**.
3. Acompanhe os passos (Estudar, Criar, Verificar, Pronto) e o quanto ficou parecido. Pra mudar algo, escreva na caixa embaixo ("deixa o topo azul").

O projeto fica em `Documentos/Craft Anything`: o resultado em `app/` e cada comparação com o original em `checks/`.

## Use com cabeça
- O modo **Sala limpa** (padrão) não lê o código do original, só o que um visitante vê. O **Profundo** lê tudo: só no que é seu.
- O Modo automático vem ligado e deixa o agente rodar comandos no seu computador. Pra ele perguntar antes: no projeto, clique em **Aprovações** (embaixo da caixa de texto) e ponha **Outros comandos** em **Perguntar**. Pra valer em tudo: Configurações > desligue o **Modo automático**.
- Instalar dependências roda código no seu computador. Não clique "Sempre" pro `npm` em projeto que você não confia.
- Está em "early alpha": pode travar.

## O meu teste (27/11/2026)
- Baixei a versão 0.6.1 pra Linux, conferi o código SHA256 da release (prova que o arquivo não foi alterado) e rodei o `doctor`: achou o Chrome e o Claude Code instalado (ainda sem login).
- O que eu não testei: abrir o app num site e uma recriação inteira. Ela roda no seu Claude Code logado; na minha máquina de teste ele não estava logado.

## O próximo passo
Eu uso o Claude Code pra produzir os vídeos do Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=recriar-qualquer-coisa)
