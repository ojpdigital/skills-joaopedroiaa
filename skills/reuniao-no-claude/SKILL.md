---
name: reuniao-no-claude
description: Guia o usuário para instalar o Yogurt (alternativa aberta e grátis ao Granola, sem robô na chamada), configurar transcrição em português, conectar o servidor MCP local no Claude Desktop ou Claude Code e rodar 9 prompts prontos de pós-reunião. Use quando ele pedir "gravar reunião sem robô", "instalar Yogurt", "ligar reuniões no Claude", "MCP de reunião", "prompts de pós-reunião" ou colar o link desta skill.
---

# Gravar qualquer reunião de graça, sem robô, e ligar no Claude (Yogurt + MCP)

Como chamar: "me ajuda a instalar o Yogurt e ligar as minhas reuniões aqui no Claude" (ou, depois de instalado: "usa os prompts de pós-reunião do Yogurt").

O que é (fonte oficial: `https://github.com/FrigadeHQ/yogurt`, licença MIT, versão `v0.3.82`, conferido em 28/11/2026):
- **Yogurt** é um aplicativo aberto e gratuito para **Mac (Apple Silicon — chip M1 ou mais novo; Mac Intel não é suportado — macOS 14.4+), Windows (10 versão 2004+ 64 bits) e Linux (Ubuntu 22.04+ 64 bits)**, com mínimo de **8 GB de memória RAM** (16 GB+ para o modelo maior de resumo).
- Grava microfone e som da chamada (Google Meet, Microsoft Teams, Zoom ou qualquer app) **sem colocar nenhum robô na sala**. Sempre avise quem está na chamada que você vai gravar.
- Roda transcrição (`whisper.cpp` / Apple SpeechAnalyzer no Mac) e resumo (`llama.cpp`) **localmente no computador**, sem conta e sem assinatura. Depois de baixar os modelos na primeira vez, funciona offline.
- Traz um **servidor MCP local** (desligado por padrão, somente leitura) para o Claude consultar suas reuniões, transcrições e notas.

Regras: fale português simples; avise antes de qualquer comando o que ele faz; não peça senha e nunca rode `sudo` pelo agente; não altere arquivo de configuração fora da pasta do projeto sem pedir "sim" e criar uma cópia `.bak` antes; avise claramente sobre privacidade (o Yogurt é local, mas ao ligar no Claude, o texto lido via MCP pode ir pro modelo online da Anthropic).

## Passo 1. Identificar o sistema e passar o link oficial
Detecte o sistema do usuário (ou pergunte: Mac, Windows ou Linux) e passe somente os links oficiais da última release no GitHub:
- **Mac (Apple Silicon — chip M1 ou mais novo, macOS 14.4+; Mac Intel não é suportado):** `https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-mac-arm64.dmg` (ou via Homebrew: `brew install --cask frigadehq/yogurt/yogurt`)
- **Windows (10 versão 2004+ 64 bits):** `https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-windows-x64-setup.exe` (se aparecer tela de aviso do Windows SmartScreen, clique em *Mais informações → Executar assim mesmo*)
- **Linux (Ubuntu 22.04+ 64 bits):** `https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-linux-x86_64.AppImage`
  - Torne o `.AppImage` executável (`chmod +x Yogurt-linux-x86_64.AppImage`). Se não abrir por falta de FUSE 2, peça pro usuário rodar no próprio terminal (não rode `sudo` pelo agente): `sudo apt install libfuse2` (Ubuntu 22.04) ou `sudo apt install libfuse2t64` (Ubuntu 24.04+).

## Passo 2. Permissões e idioma português (essencial pro Brasil)
1. **Permissões no Mac:** liberar Microfone e **Gravação de Tela e Áudio do Sistema** (*Screen & System Audio Recording*) pra ouvir os dois lados. Calendário, Notificações e Acessibilidade (nomes de quem fala) são opcionais e exclusivos do Mac (no Windows/Linux, o calendário conecta por link privado).
2. **Trocar pra português:** por padrão o Yogurt vem em inglês (`English`). Peça pro usuário ir em **Settings → Language → Spoken language** e escolher **Multi-language** (transcreve 99 idiomas, incluindo português, e acompanha até quando misturam idiomas na mesma chamada). Em **Settings → Summary language**, escolher **Portuguese (Português)**.
3. **Aguardar o download inicial dos modelos:** a gravação libera logo após a configuração inicial; o modelo de resumo termina de baixar em segundo plano.

## Passo 3. Conectar o MCP local no Claude
1. No Yogurt, abrir **Settings → AI apps** e ligar o acesso local.
2. Copiar o comando de conexão que o próprio Yogurt mostra na tela.
3. Avisar o usuário: o acesso é **somente leitura** (o Claude lê reuniões, notas, transcrições e detalhes do calendário, sem alterar nada), mas o conteúdo lido pode ser enviado pro modelo online da Anthropic. Para cortar o acesso a qualquer momento, basta desligar em **Settings → AI apps**.
4. Perguntar onde ele quer conectar:
   - **Claude Code:** rodar `claude mcp add --scope user yogurt -- <comando de conexão copiado do Yogurt>` (somente após o "sim" dele; `--scope user` faz funcionar em qualquer pasta).
   - **Claude Desktop (Mac e Windows; no Linux use Claude Code):**
     - Caminhos do arquivo: Mac `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows `%APPDATA%\Claude\claude_desktop_config.json`.
     - Pedir "sim" antes de mexer no arquivo (fica fora da pasta do projeto). Se já existir, fazer cópia `claude_desktop_config.json.bak`; se não existir, criar do zero.
     - Inserir a entrada `yogurt` dentro de `mcpServers` com `command` e `args` copiados do Yogurt, conferir que o JSON ficou válido e pedir pro usuário reiniciar o Claude Desktop.

## Passo 4. Rodar um dos 9 prompts de pós-reunião
Assim que o MCP estiver ligado (ou colando uma transcrição exportada em Markdown do Yogurt), ofereça os 9 prompts prontos (todos já citam o Yogurt pra funcionar até em conversa nova):
1. **Resumo executivo em 5 linhas:** "Lê minha última reunião no Yogurt e resume em 5 linhas diretas: objetivo, decisões fechadas e o que travou."
2. **Próximos passos por pessoa:** "Na minha última reunião no Yogurt, lista cada tarefa combinada com responsável, prazo citado e o trecho exato onde foi combinado."
3. **Mensagem de pós-reunião:** "Com base na minha última reunião no Yogurt, escreve uma mensagem curta pra mandar no WhatsApp ou e-mail confirmando o que fechamos e o próximo passo de cada um."
4. **Decisões x pendências:** "Na minha última reunião no Yogurt, separa o que foi realmente decidido do que ficou só na conversa sem dono ou sem data."
5. **Objeções e sinais de compra (reunião comercial):** "Na minha última reunião no Yogurt, lista todas as objeções que o cliente levantou, com as palavras exatas dele, e os pontos em que demonstrou interesse."
6. **Riscos e bloqueios:** "Na minha última reunião no Yogurt, aponta o que pode atrasar ou travar o projeto com base no que foi falado."
7. **Pauta da próxima reunião:** "A partir da minha última reunião no Yogurt, monta uma pauta de 5 tópicos pra próxima chamada começando pelas pendências abertas."
8. **Cruzamento entre reuniões da semana:** "Procura em todas as minhas reuniões dos últimos 7 dias no Yogurt tudo que falamos sobre [tema] e me mostra o que mudou de uma pra outra."
9. **Transformar reunião em conteúdo:** "Na minha última reunião no Yogurt, extrai 3 dores reais e 3 frases fortes ditas lá que viram roteiro de vídeo curto ou post (sem citar nomes nem dados privados)."

## O que foi conferido (28/11/2026)
- Repositório oficial `FrigadeHQ/yogurt` (3.776★, MIT, versão `v0.3.82` de 27/11/2026), documentação completa (`README.md` e `docs/README.md`) e links diretos ativos no dia dos três instaladores (Mac DMG 182 MB, Windows EXE 423 MB, Linux AppImage 535 MB).
- O que não foi testado na revisão desta skill: abertura do aplicativo desktop e gravação de chamada real (apenas documentação oficial e links dos instaladores foram conferidos). Se o usuário perguntar, avise com clareza.
