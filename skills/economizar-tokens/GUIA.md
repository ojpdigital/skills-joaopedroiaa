# Gastar menos limite no Claude Code: o modo "advisor" oficial

Se você usa o Claude Opus pra tudo, está gastando um dos modelos mais caros até em tarefa fácil. A Anthropic tem um modo oficial em que o **Sonnet faz o trabalho** e o **Opus entra só como conselheiro** nas partes difíceis. Junto com isso, dá pra pôr os **subagentes** (os ajudantes que o Claude chama pra tarefa pequena) **no Haiku**, o modelo mais barato.

Fonte: documentação oficial do Claude Code, [advisor](https://code.claude.com/docs/en/advisor) e [subagentes](https://code.claude.com/docs/en/sub-agents), lida em 27/11/2026.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill economizar-tokens do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois liga o modo econômico no meu Claude Code.
```

## Na mão (2 comandos e 1 trecho nas configurações)
1. Dentro do Claude Code, digite `/model sonnet` e aperte Enter. Depois digite `/advisor opus` e aperte Enter (um de cada vez).
2. Peça ao Claude: "faz uma cópia do meu ~/.claude/settings.json e junta este trecho sem apagar nada" (no Windows o arquivo fica em `C:\Users\SEU_NOME\.claude\settings.json`; se já existir um bloco `"env"`, as 2 linhas entram dentro dele):
   ```json
   {
     "env": {
       "CLAUDE_CODE_SUBAGENT_MODEL": "haiku",
       "CLAUDE_CODE_SUBAGENT_MODEL_FORCE": "1"
     }
   }
   ```
3. Feche e abra o Claude Code. Ao abrir aparece o aviso "Advisor Tool (experimental) is on and may use more tokens". Quando ele consulta o Opus, aparece "Advising".

Pra desligar: `/advisor off`, apague as 2 linhas do `env` e, se quiser o modelo de antes, `/model opus`.

## Quando o Opus entra
Quem decide é o próprio Claude. Segundo a doc, ele costuma chamar o conselheiro:
- antes de escolher o caminho de uma tarefa;
- quando um erro fica voltando;
- antes de dizer que terminou.

Quer que ele chame mais (ou menos)? Escreva isso no seu `CLAUDE.md` (o arquivo de instruções que o Claude lê toda vez que abre). A skill já deixa um texto pronto.

## O que é verdade e o que não é
- **Economiza?** A doc diz que normalmente custa menos do que deixar o modelo forte o tempo todo. Ela não dá número. Desconfie de quem promete "50%": meça você mesmo com `/usage`.
- **É um comando só?** Não: são 2 comandos e 1 trecho nas configurações.
- **`--subagents haiku`?** Esse atalho circula por aí e não existe. O jeito oficial é o do passo 2.
- **Onde funciona:** conta do Claude (assinatura) ou API da Anthropic, e também no Claude Platform on AWS e no Claude Models on Google Cloud gerenciado pela Anthropic. É experimental. Não funciona no Amazon Bedrock, no Agent Platform do Google Cloud nem no Microsoft Foundry. O uso do conselheiro conta no limite do seu plano.
- Cada consulta relê a conversa inteira: em sessão muito longa, abra uma nova de vez em quando.
- Os subagentes no Haiku também podem consultar o Opus, então custam um pouco mais que o Haiku sozinho.
- O aviso não apareceu? Veja se o seu settings.json tem `DISABLE_TELEMETRY` ou uma lista `availableModels` sem o Opus: as duas coisas desligam o advisor.

## O que eu conferi (27/11/2026)
- As páginas oficiais do advisor e dos subagentes, com os comandos e o trecho acima.
- Que o Claude Code 2.1.327 já traz `advisorModel` e `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`.
- O que eu não medi: quanto economiza numa sessão real. Isso muda com o tipo de tarefa.

## O próximo passo
Foi com esse mesmo Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=economizar-tokens)
