# Superpowers: o plugin com mais estrelas no GitHub que o próprio Claude Code

O Superpowers ([github.com/obra/superpowers](https://github.com/obra/superpowers), grátis, código aberto, licença MIT) tem mais estrelas no GitHub que o próprio Claude Code: 326.839 contra 157.125 (lido em 26/11/2026). Está na [loja oficial do Claude](https://claude.com/plugins/superpowers), com mais de 1 milhão de instalações. O plugin é grátis; o Claude Code precisa de uma conta do Claude com plano que inclua o Claude Code.

O que ele muda: você pede um site e o Claude não sai escrevendo código. Primeiro ele pergunta o que você quer de verdade, depois mostra o plano em partes pequenas e só anda quando você aprova. Aí quebra tudo em tarefas de 2 a 5 minutos, põe um agente novo em cada uma e revisa no fim de cada etapa. São 15 skills que ligam sozinhas.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill plugin-superpowers do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois começa comigo o meu primeiro projeto com o Superpowers.
```

## Na mão (1 comando)
Dentro do Claude Code, digite:

```text
/plugin install superpowers@claude-plugins-official
```

Feche e abra o Claude Code. Pra conferir, peça "vamos fazer uma lista de tarefas em React": se ele começar te fazendo perguntas em vez de sair codando, está ligado.

Se não achar: `/plugin marketplace add obra/superpowers-marketplace` e `/plugin install superpowers@superpowers-marketplace`.

No Codex: `/plugins`, busque "superpowers" e instale. No Cursor: `/add-plugin superpowers`.

## Como usar bem
1. Responda as perguntas com calma: é ali que o resultado melhora.
2. Leia o desenho que ele mostra e corrija o que não for isso.
3. Leia o plano e diga "vai".
4. Deixe ele trabalhar: ele revisa cada etapa sozinho. Isso gasta bastante do limite do seu plano, e ele pode parar pra pedir permissão.

## O meu teste (26/11/2026)
- Clonei o repositório e conferi na fonte: 15 skills (brainstorming, writing-plans, subagent-driven-development e mais 12), versão 7.0.2, os números de estrelas na API do GitHub e as instalações na página da loja oficial.
- O que eu não testei: a instalação pelo `/plugin` e um projeto rodando. Isso roda no seu Claude Code logado; a minha máquina de teste não estava logada num plano.

## Bom saber
- Uma parte opcional (o companheiro visual do brainstorming) carrega o logo do autor de um site dele, com a versão do plugin e nada do seu projeto. Pra desligar, acrescente no `~/.claude/settings.json`: `"env": { "SUPERPOWERS_DISABLE_TELEMETRY": "1" }`.

## O próximo passo
O Superpowers faz o Claude trabalhar como um time. Foi com esse mesmo Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=plugin-superpowers)
