# Instalação feita pelo agente

Este arquivo é pra você, agente (Claude Code, Codex, Cursor ou outro que roda comando). O usuário colou uma mensagem pedindo pra instalar uma skill deste repositório e, quase sempre, pra já fazer a tarefa. Fale com ele em português simples (ou no idioma em que ele escreveu) e diga, antes de cada comando, o que ele faz.

Regras:
- Não peça senha nem token, e não digite login por ele.
- Rode só o que esta instalação e a skill pedem. Nada de apagar ou mexer em arquivo dele fora da pasta de trabalho.
- Nada pago sem ele dizer "sim" antes, com o preço na frente.
- Deu erro num passo: diga o erro em uma frase e o que ele pode fazer. Não invente caminho por fora.

## 1. Qual skill
O nome vem na mensagem dele (a lista está no README.md). Se ele não disse, mostre a tabela do README e pergunte qual.

## 2. Baixar o repositório
```bash
git clone --depth 1 https://github.com/ojpdigital/skills-joaopedroiaa "${TMPDIR:-/tmp}/skills-joaopedroiaa" 2>/dev/null || git -C "${TMPDIR:-/tmp}/skills-joaopedroiaa" pull --ff-only
```
Sem `git`: diga que precisa dele (git-scm.com) e pare.

## 3. Instalar na pasta de trabalho
A pasta de trabalho é a pasta aberta agora.
```bash
mkdir -p .claude/skills && cp -R "${TMPDIR:-/tmp}/skills-joaopedroiaa/skills/<skill>" .claude/skills/
```
Ele pediu pra valer em todo projeto? Copie pra `~/.claude/skills/` no lugar de `.claude/skills/`.
No Codex e em outros agentes que leem `AGENTS.md`: copie a pasta do mesmo jeito e acrescente uma linha no `AGENTS.md` da pasta: `Skill <skill>: quando eu pedir <o que a skill faz>, leia .claude/skills/<skill>/SKILL.md e siga.`

## 4. Conferir
`.claude/skills/<skill>/SKILL.md` existe? Então está instalada. Ela aparece sozinha numa sessão nova do Claude Code.

## 5. Já fazer a tarefa
Não precisa abrir sessão nova pra começar: leia agora `.claude/skills/<skill>/SKILL.md` e siga do passo 1, nesta mesma conversa, com o que ele já escreveu na mensagem.

## 6. Fechar
Apague a cópia temporária (`rm -rf "${TMPDIR:-/tmp}/skills-joaopedroiaa"`) e diga numa mensagem curta: o que ficou instalado, em qual pasta, e a frase que ele digita da próxima vez pra usar de novo (está no começo do SKILL.md, em "Como chamar").
