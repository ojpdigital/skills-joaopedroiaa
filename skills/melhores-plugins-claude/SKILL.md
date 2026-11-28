---
name: melhores-plugins-claude
description: Mostra os 25 melhores plugins, skills e conectores grátis de Claude Code no GitHub (conferidos ao vivo), recomenda os 2 ou 3 mais úteis pro projeto do usuário e instala só o que ele aprovar. Use quando ele pedir "quais os melhores plugins pro Claude Code", "instala Ponytail / Unslop / EGM / Agent Reach / Claude Code Setup", "lista dos 25 plugins" ou colar o link desta skill.
---

# 25 melhores plugins, skills e conectores grátis pro Claude Code

Como chamar: "me mostra os 25 plugins grátis pro Claude Code e indica quais instalar no meu projeto".

Todos os 25 itens abaixo foram conferidos ao vivo na API pública do GitHub em 28/11/2026 (repositório, licença, estrelas e documentação oficial).

Regras: fale português simples; nunca instale nada sem mostrar antes o que o comando faz e pedir o "sim" do usuário; não peça senha; não instale nada pago; nunca instale mais de 3 plugins de uma vez (muitos plugins juntos gastam limite e confundem a IA); antes de mexer em qualquer arquivo de configuração existente, faça uma cópia `.bak` ao lado e peça "sim" se o arquivo ficar fora da pasta do projeto.

## Passo 1. Entender o projeto do usuário
Antes de sair instalando, pergunte em 2 linhas:
1. O que ele está construindo agora (site/app, automação, pesquisa/conteúdo ou código de servidor)?
2. Qual a maior dor hoje (limite acabando rápido, visual com cara de IA, código com bug, agente sem acesso à internet ou configuração bagunçada)?

Se ele já estiver dentro de uma pasta de projeto, leia apenas os arquivos principais (`package.json`, `pyproject.toml`, `README.md`, `CLAUDE.md`) sem editar nada.

## Passo 2. Recomendar 2 ou 3 itens dos 25 (e mostrar a lista completa se ele pedir)

Nota de execução: comandos `claude plugin ...` rodam no **terminal** (Bash/PowerShell). Se o usuário preferir instalar digitando no **chat** do Claude Code, use o equivalente `/plugin ...` (um comando por mensagem, nunca via Bash).

### Os 5 destaques
1. **Ponytail** (`DietrichGebert/ponytail`, MIT) — faz o agente evitar código inchado e pensar enxuto, igual programador sênior. No teste publicado no README oficial (39 tarefas no Claude Code), marcou `-53%` código, `-45%` tokens, `-41%` tempo e `98%` de lógica crítica com teste (contra `68%` sem ele).
   - No terminal:
     ```bash
     claude plugin marketplace add DietrichGebert/ponytail
     claude plugin install ponytail@ponytail
     ```
   - Ou dentro do chat do Claude Code (um por mensagem):
     ```text
     /plugin marketplace add DietrichGebert/ponytail
     /plugin install ponytail@ponytail
     ```
2. **Unslop** (`heydamir/unslop`, CC-BY-4.0) — revisa telas feitas por IA (degradê roxo, brilho exagerado, emoji solto, espaçamento quebrado) etapa por etapa como designer, em React, Next.js, Vue, Svelte, Tailwind, HTML/CSS ou até numa página já publicada.
   - No terminal:
     ```bash
     claude plugin install unslop --marketplace heydamir/unslop
     ```
     *(Em versão mais antiga do Claude Code: `claude plugin marketplace add heydamir/unslop` e depois `claude plugin install unslop@heydamir`.)*
3. **Elephant-Goldfish Model — EGM** (`google/elephant-goldfish-model`, Apache-2.0) — plugin aberto do Google: o agente Elefante escreve o plano com contexto e revisores Peixinho (com a memória zerada) caçam falhas antes de virar código. Requer Claude Code atualizado (2.1.271 ou mais novo; conferir com `claude --version`).
   - No terminal:
     ```bash
     claude plugin marketplace add google/elephant-goldfish-model
     claude plugin install egm@egm
     claude plugin enable egm@egm
     ```
   - Comandos no chat após reiniciar a sessão: `/egm:egm-brainstorm`, `/egm:egm-draft`, `/egm:egm-review`.
4. **Agent Reach** (`Panniantong/Agent-Reach`, MIT) — ferramenta de linha de comando (via `uv`) que permite ao agente pesquisar e ler GitHub, YouTube e web direto (grátis sem conta) e, de forma opcional/experimental, Reddit, LinkedIn, X/Twitter, Facebook e Instagram (esses pedem login).
   - **Aviso crítico de segurança (do README oficial):** NUNCA instale o pacote `agent-reach` do PyPI (ou seja, nunca rode `pip install agent-reach`) — ele NÃO é este projeto. Instale somente lendo o guia oficial do GitHub: `https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md`. Para redes que exigem login (X, Instagram, Facebook, LinkedIn e Reddit), oriente o usuário a usar conta secundária, pois as plataformas combatem automação.
5. **Claude Code Setup** (`anthropics/claude-plugins-official`, pasta `plugins/claude-code-setup`, Apache-2.0) — plugin oficial da Anthropic, **somente leitura**: analisa o projeto sem alterar nenhum arquivo e recomenda os 1–2 melhores conectores MCP, skills, hooks (regras automáticas), subagentes e comandos.
   - No terminal:
     ```bash
     claude plugin install claude-code-setup@claude-plugins-official
     ```
   - Ou no chat do Claude Code:
     ```text
     /plugin install claude-code-setup@claude-plugins-official
     ```

### Mais 8 plugins oficiais da Anthropic (`anthropics/claude-plugins-official`, Apache-2.0)
Todos instalados no terminal com `claude plugin install <nome>@claude-plugins-official` (ou no chat com `/plugin install <nome>@claude-plugins-official`):
6. **feature-dev** — fluxo guiado (explorar, arquitetar e revisar) antes de programar uma funcionalidade grande.
7. **code-review** — revisão multi-agente focada em bugs reais e regressões.
8. **pr-review-toolkit** — revisa pedidos de alteração de código (Pull Requests) cruzando o diff com o contexto do projeto.
9. **security-guidance** — alerta sobre falhas comuns de segurança (como OWASP) enquanto o código é escrito.
10. **frontend-design** — diretrizes oficiais da Anthropic para interfaces limpas e responsivas.
11. **code-simplifier** — simplifica código complexo sem alterar o comportamento.
12. **hookify** — cria hooks (regras automáticas como formatar, checar regras ou bloquear arquivos sensíveis).
13. **skill-creator** — ajuda a criar, testar e organizar suas próprias skills.

### Mais 8 skills e frameworks da comunidade (GitHub)
14. **Superpowers** (`obra/superpowers`, MIT) — fluxo completo com plano em etapas e revisão antes de codar.
15. **Matt Pocock Skills** (`mattpocock/skills`, MIT) — skills práticas de engenharia real da ideia até ir pro ar.
16. **Anthropic Official Skills** (`anthropics/skills`, ver arquivo de licença no repositório) — catálogo público oficial de Agent Skills da Anthropic.
17. **ECC — Everything Claude Code** (`affaan-m/ECC`, MIT) — conjunto de skills, memória, hooks e checagens de segurança.
18. **UI/UX Pro Max** (`nextlevelbuilder/ui-ux-pro-max-skill`, MIT) — biblioteca de regras de design (UI/UX) para múltiplos frameworks.
19. **Claude Mem** (`thedotmack/claude-mem`, Apache-2.0) — memória persistente entre sessões do agente.
20. **Trail of Bits Skills** (`trailofbits/skills`, CC-BY-SA-4.0) — skills de auditoria de segurança e detecção de vulnerabilidades.
21. **Claude Code Templates** (`davila7/claude-code-templates`, MIT) — catálogo e comando de terminal com agentes, comandos, skills e hooks prontos.

### Mais 4 conectores MCP e utilitários essenciais (GitHub)
22. **Context7** (`upstash/context7`, MIT) — puxa documentação atualizada na versão exata da biblioteca que você usa.
23. **Chrome DevTools MCP** (`ChromeDevTools/chrome-devtools-mcp`, Apache-2.0) — liga o agente direto às ferramentas de inspeção do Chrome (DevTools).
24. **Playwright MCP** (`microsoft/playwright-mcp`, Apache-2.0) — dá um navegador real pro agente abrir, clicar e testar páginas.
25. **Repomix** (`yamadashy/repomix`, MIT) — empacota um repositório inteiro num único arquivo limpo pra IA ler sem se perder.

## Passo 3. Instalar somente os 2 ou 3 que o usuário escolher
1. Mostre os 2 ou 3 mais úteis pro caso dele e pergunte quais quer instalar agora.
2. Antes de rodar qualquer comando de instalação de repositório externo, abra ou leia o `README.md` do repositório escolhido para confirmar o comando atual (evita comandos desatualizados).
3. Se o comando for alterar qualquer arquivo de configuração existente, crie uma cópia `.bak` antes e confirme com o usuário.
4. Instale um por vez e confirme se carregou corretamente (`claude plugin list` no terminal ou `/plugin` numa sessão nova).
5. Oriente o usuário a fechar e abrir o Claude Code para ativar os plugins instalados.

## O que foi conferido (28/11/2026)
- Os 25 repositórios/plugins acima existem na API pública do GitHub em 28/11/2026, com licenças e READMEs oficiais lidos no dia.
- O que não foi rodado nos testes: instalação dos plugins externos numa sessão real (apenas os 25 repositórios, licenças e READMEs oficiais foram conferidos no dia; instale só os 2 ou 3 que servem pro projeto). Se o usuário perguntar, seja transparente sobre isso.
