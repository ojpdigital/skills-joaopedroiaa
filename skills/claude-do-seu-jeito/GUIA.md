# Seu Claude do seu jeito em 10 minutos

Funciona no app do Claude (celular ou computador), no site e no Claude Code. Testei os prompts 1, 2 e 3 em 22/11/2026.

## O jeito mais fácil: a IA faz tudo (Claude Code)
Abra o Claude Code numa pasta e cole:

```text
Instala e roda pra mim a skill claude-do-seu-jeito do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois começa a me entrevistar.
```

Ele faz a entrevista, grava as instruções no CLAUDE.md, monta a pasta segundo-cerebro e escreve a sua primeira skill. No app ou no site do Claude, use os 4 prompts abaixo, um de cada vez.

## 1. A entrevista
Cola isto numa conversa nova:
> Me entrevista pra você me conhecer. Uma pergunta por vez, no máximo 7, sobre: quem eu sou, o que eu faço, pra quem eu faço, e como eu quero que você me responda (tamanho, tom, formato, o que eu odeio em resposta).

Responde cada pergunta do seu jeito, sem caprichar no texto.

## 2. Vira instrução global
Quando acabar, manda:
> Agora transforma minhas respostas em instruções globais pra eu colar nas configurações do Claude (no máximo 1.200 caracteres). Manda só o texto das instruções.

Copia o texto e cola em Configurações > Perfil, no campo de instruções (o nome do campo pode mudar com a versão do app). A partir daí ele lê isso no começo de toda conversa.

O que mudou no meu teste, com o mesmo pedido ("escreve um roteiro de reel de 30 segundos sobre como criar um influenciador com IA"):
- Sem instruções: título, negrito, notas de produção e legenda, umas 300 palavras.
- Com instruções: gancho, meio e fecho falados, em 3 blocos, do jeito que eu falo.

## 3. O segundo cérebro
> Agora me entrevista de novo, uma pergunta por vez, sobre meu trabalho, minha vida pessoal e meus projetos em andamento. No fim, organiza tudo numa pasta "segundo-cerebro" com um arquivo .md pra cada assunto.

## 4. O que vale automatizar vira skill
> Lê tudo que eu te contei e me diz as 3 tarefas que mais valem automatizar. Depois escreve a primeira como uma skill do Claude: nome, quando usar e o passo a passo.

No meu teste ele escolheu o lote de reels da semana e escreveu a skill inteira (pergunta o tema, propõe 7 ganchos, espera eu aprovar, escreve roteiro e legenda).

## Onde isso me leva
Foi com esse mesmo Claude, configurado assim, que eu criei o Seu João, um personagem feito com IA que posta todo dia sem eu aparecer. [Gravei uma aula mostrando como montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=claude-do-seu-jeito)
