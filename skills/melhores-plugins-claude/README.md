# Os 25 melhores plugins grátis pro Claude Code no GitHub

Uma lista curada e conferida ao vivo no GitHub (28/11/2026) com os 5 destaques do vídeo mais 20 plugins oficiais, skills da comunidade e conectores MCP (integrações que ligam o Claude a ferramentas externas), tudo grátis.

## O jeito mais fácil: o Claude escolhe e instala pra você
Abra o Claude Code na pasta do seu projeto e cole:

```text
Instala e roda pra mim a skill melhores-plugins-claude do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa numa pasta temporária, lê o INSTALL.md e segue os passos. Depois me mostra os 25 plugins por categoria e me ajuda a escolher e instalar os melhores pro meu projeto.
```

Ele não instala nada sem você dizer "sim" e nunca pede senha.

## Os 5 destaques do vídeo (com link oficial)

Onde rodar: comandos que começam com `claude plugin ...` vão no **terminal** do computador. Se preferir fazer dentro do **chat** do Claude Code, troque `claude plugin` por `/plugin` (um comando por mensagem).

1. **Ponytail** — [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT · 200 mil ★)
   Faz o agente pensar enxuto, igual programador sênior. No teste publicado no README deles (39 tarefas), marcou `-53%` código, `-45%` tokens, `-41%` tempo e `98%` da lógica crítica com teste (contra `68%` sem ele).
   ```bash
   claude plugin marketplace add DietrichGebert/ponytail
   claude plugin install ponytail@ponytail
   ```

2. **Unslop** — [heydamir/unslop](https://github.com/heydamir/unslop) (CC-BY-4.0 · 22,7 mil ★)
   Tira a cara de "feito por IA" (degradê roxo, brilho solto, espaçamento torto) e refaz a tela etapa por etapa como um designer.
   ```bash
   claude plugin install unslop --marketplace heydamir/unslop
   ```
   *(Em versão mais antiga do Claude Code, no terminal: `claude plugin marketplace add heydamir/unslop` e depois `claude plugin install unslop@heydamir`. No chat: `/plugin marketplace add heydamir/unslop` e depois `/plugin install unslop@heydamir`.)*

3. **Elephant-Goldfish Model (EGM)** — [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) (Apache-2.0 · 23,4 mil ★)
   Plugin aberto do Google (requer Claude Code 2.1.271 ou mais novo): o Elefante planeja com todo o contexto e revisores Peixinho (com a memória zerada) caçam furos antes de virar código.
   ```bash
   claude plugin marketplace add google/elephant-goldfish-model
   claude plugin install egm@egm
   claude plugin enable egm@egm
   ```
   *(Confira sua versão com `claude --version`. Depois de reiniciar a sessão, os comandos no chat são `/egm:egm-brainstorm`, `/egm:egm-draft` e `/egm:egm-review`.)*

4. **Agent Reach** — [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (MIT · 115 mil ★)
   Ferramenta de terminal (instalada via `uv`, um instalador rápido de Python) que deixa o agente ler YouTube, GitHub e web direto sem conta; Reddit, LinkedIn, X, Facebook e Instagram entram como canais opcionais/experimentais com login.
   Pra instalar com o agente, cole no chat do Claude Code:
   ```text
   Instala o Agent Reach seguindo este guia oficial: https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md
   ```
   **Cuidado:** nunca instale pelo PyPI — repositório público do Python — (ou seja, nunca rode `pip install agent-reach` — não é o mesmo projeto). Use só o [guia oficial no GitHub](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md) e, para redes com login (X, Instagram, Facebook, LinkedIn e Reddit), use conta secundária.

5. **Claude Code Setup** — [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) (Apache-2.0 · 48,4 mil ★)
   Plugin oficial da Anthropic, **somente leitura**: analisa seu projeto sem mexer em arquivo nenhum e recomenda os 1–2 melhores hooks (regras automáticas), skills, subagentes e conectores MCP.
   ```bash
   claude plugin install claude-code-setup@claude-plugins-official
   ```

## Os outros 20 da lista

### Oficiais da Anthropic ([claude-plugins-official](https://github.com/anthropics/claude-plugins-official))
Instale qualquer um no terminal com `claude plugin install <nome>@claude-plugins-official` (ou no chat com `/plugin install <nome>@claude-plugins-official`):

| # | Plugin | O que faz |
|---|---|---|
| 6 | `feature-dev` | Planeja, arquiteta e revisa antes de escrever uma função grande |
| 7 | `code-review` | Revisão multi-agente focada em bugs reais |
| 8 | `pr-review-toolkit` | Revisa pedidos de alteração de código (Pull Requests) lendo as mudanças no contexto inteiro |
| 9 | `security-guidance` | Checa falhas de segurança enquanto o código é escrito |
| 10 | `frontend-design` | Diretrizes oficiais de design para telas limpas |
| 11 | `code-simplifier` | Enxuga código complicado sem quebrar nada |
| 12 | `hookify` | Monta regras automáticas (hooks) pra formatar código ou travar arquivos sensíveis |
| 13 | `skill-creator` | Cria e testa suas próprias skills |

### Skills e frameworks da comunidade

| # | Projeto | Link | O que faz |
|---|---|---|---|
| 14 | Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Fluxo estruturado com plano em etapas e testes (328 mil ★) |
| 15 | Matt Pocock Skills | [mattpocock/skills](https://github.com/mattpocock/skills) | Skills práticas de engenharia da ideia até ir pro ar (334 mil ★) |
| 16 | Anthropic Skills | [anthropics/skills](https://github.com/anthropics/skills) | Repositório oficial de Agent Skills da Anthropic (201 mil ★) |
| 17 | ECC | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Pacote completo de skills, memória, regras automáticas e segurança (312 mil ★) |
| 18 | UI/UX Pro Max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Regras de design de tela (UI/UX) para vários frameworks (155 mil ★) |
| 19 | Claude Mem | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memória persistente entre sessões (120 mil ★) |
| 20 | Trail of Bits | [trailofbits/skills](https://github.com/trailofbits/skills) | Auditoria de segurança e busca de falhas (8,4 mil ★) |
| 21 | Claude Code Templates | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Registro e comando de terminal com agentes, comandos, skills e hooks (34,2 mil ★) |

### Conectores MCP e utilitários essenciais

| # | Projeto | Link | O que faz |
|---|---|---|---|
| 22 | Context7 | [upstash/context7](https://github.com/upstash/context7) | Puxa documentação atualizada na versão exata da biblioteca (65,5 mil ★) |
| 23 | Chrome DevTools MCP | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Liga o agente direto ao inspetor do Chrome (DevTools) (59,6 mil ★) |
| 24 | Playwright MCP | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Dá navegador real pro agente abrir e testar sites (40,2 mil ★) |
| 25 | Repomix | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Empacota um repositório inteiro num arquivo limpo pra IA ler (29,4 mil ★) |

## O que é verdade e o que merece atenção
- **Não instale os 25 de uma vez:** comece com 2 ou 3 que resolvam sua dor principal (por exemplo: `claude-code-setup` + `ponytail` ou `unslop`). Plugin demais sem uso gasta seu limite e confunde a IA.
- **Faça backup antes:** se for editar arquivos de configuração na mão (como `~/.claude/settings.json`), salve uma cópia `.bak` antes.
- **Ponytail:** o teste publicado no README marca `-45%` tokens e `-53%` código (não "mais de 50% de economia em tudo"). Meça no seu projeto.
- **Claude Code Setup:** é somente leitura — ele recomenda, não apaga nada sozinho.
- **Agent Reach:** GitHub, YouTube e web funcionam direto; X, Instagram, Facebook, Reddit e LinkedIn pedem login e podem bloquear conta se abusar. Nunca rode `pip install agent-reach` (PyPI falso).

## O que eu conferi (28/11/2026)
- Todos os 25 repositórios e plugins conferidos ao vivo na API pública do GitHub, com licenças, estrelas e READMEs oficiais lidos no dia.
- O que não foi rodado nos testes: instalação dos plugins externos numa sessão real (foram conferidos os repositórios, licenças e READMEs oficiais no dia). Escolha só os 2 ou 3 que servem pro seu caso.

## O próximo passo
Foi com esse mesmo Claude Code que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=melhores-plugins-claude)
