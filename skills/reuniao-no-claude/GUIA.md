# Gravar qualquer reunião de graça (sem robô) e ligar no Claude

O **Yogurt** ([FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt), licença MIT, aberto e gratuito) é uma alternativa local ao Granola, Otter e Fireflies. Ele grava o microfone e o som do seu computador em qualquer chamada (Google Meet, Teams, Zoom), sem nenhum robô entrar na sala, transcreve e resume tudo na sua máquina — sem conta e sem assinatura — e traz servidor MCP local (integração pra você consultar suas reuniões direto dentro do Claude).

Fonte: repositório e documentação oficiais do [FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt) (versão `v0.3.82`, conferido em 28/11/2026).

## O jeito mais fácil: o Claude configura com você
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill reuniao-no-claude do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa numa pasta temporária, lê o INSTALL.md e segue os passos. Depois me ajuda a baixar o Yogurt, ligar o modo português e conectar o MCP das reuniões aqui no Claude.
```

## Passo a passo na mão

### 1. Baixe o instalador oficial (mínimo 8 GB de memória RAM)
- **Mac (Apple Silicon — chip M1 ou mais novo; Mac Intel não é suportado — macOS 14.4+):** [Baixar Yogurt-mac-arm64.dmg](https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-mac-arm64.dmg) ou pelo terminal: `brew install --cask frigadehq/yogurt/yogurt`
- **Windows (10 versão 2004+ 64 bits):** [Baixar Yogurt-windows-x64-setup.exe](https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-windows-x64-setup.exe) (se aparecer aviso do Windows SmartScreen, clique em *Mais informações → Executar assim mesmo*)
- **Linux (Ubuntu 22.04+ 64 bits):** [Baixar Yogurt-linux-x86_64.AppImage](https://github.com/FrigadeHQ/yogurt/releases/latest/download/Yogurt-linux-x86_64.AppImage) (torne executável com `chmod +x Yogurt-linux-x86_64.AppImage` e abra com `./Yogurt-linux-x86_64.AppImage` ou duplo clique; se não abrir, rode no seu terminal `sudo apt install libfuse2` no Ubuntu 22.04 ou `sudo apt install libfuse2t64` no 24.04+).

### 2. Libere permissões e ative o português (pulo do gato)
- **Permissões:** libere microfone e áudio do sistema (no Mac aparece como **Gravação de Tela e Áudio do Sistema** / *Screen & System Audio Recording*). Lembre de avisar as pessoas da chamada que você vai gravar.
- **Português:** o Yogurt abre em inglês por padrão. Vá em **Settings → Language → Spoken language** e mude pra **Multi-language** (cobre 99 idiomas, incluindo português). Em **Settings → Summary language**, escolha **Portuguese (Português)**.
- Na primeira vez, o app baixa os modelos locais (`whisper.cpp` e `llama.cpp`). Depois disso, grava, transcreve e resume offline.

### 3. Conecte o MCP no Claude
1. No Yogurt, abra **Settings → AI apps** e ligue o acesso.
2. Copie o comando de conexão que aparece na tela.
3. **No Claude Code** (roda em qualquer pasta usando `--scope user`):
   ```bash
   claude mcp add --scope user yogurt -- <cole o comando de conexão do Yogurt aqui>
   ```
4. **No Claude Desktop** (Mac e Windows; no Linux use o Claude Code):
   - Abra o arquivo `claude_desktop_config.json` (Mac: `~/Library/Application Support/Claude/claude_desktop_config.json` · Windows: `%APPDATA%\Claude\claude_desktop_config.json`).
   - **Faça uma cópia `.bak` antes de editar.**
   - Adicione a entrada `yogurt` dentro de `mcpServers` (sem apagar outros servidores que já estiverem lá; se não houver argumentos, use `"args": []`) e reinicie o app:
     ```json
     {
       "mcpServers": {
         "yogurt": {
           "command": "<comando copiado do Yogurt>",
           "args": ["<argumentos, se houver>"]
         }
       }
     }
     ```
5. O acesso é **somente leitura** (o Claude lê notas e transcrições sem poder alterar nada). Lembre: o Yogurt é local, mas o texto que o Claude ler pelo MCP pode ir pro modelo online da Anthropic. Para desconectar depois, é só desligar a chave em **Settings → AI apps**.

## 9 prompts prontos de pós-reunião (cole no Claude)

1. **Resumo em 5 linhas:** `Lê minha última reunião no Yogurt e resume em 5 linhas diretas: objetivo, decisões fechadas e o que ficou travado.`
2. **Próximos passos com dono:** `Na minha última reunião no Yogurt, lista cada tarefa combinada com responsável, prazo citado e o trecho exato onde combinaram.`
3. **Mensagem de pós-reunião:** `Com base na minha última reunião no Yogurt, escreve uma mensagem curta pra eu mandar no WhatsApp confirmando o que fechamos e os próximos passos de cada um.`
4. **Decisão x conversa solta:** `Na minha última reunião no Yogurt, separa o que foi realmente decidido do que ficou só na ideia, sem dono ou sem data.`
5. **Objeções do cliente:** `Na minha última reunião no Yogurt, lista todas as objeções levantadas pelo cliente com as palavras exatas dele, mais os momentos em que demonstrou interesse.`
6. **Riscos e travas:** `Na minha última reunião no Yogurt, aponta os principais riscos e bloqueios citados que podem atrasar a entrega.`
7. **Pauta da próxima chamada:** `A partir da minha última reunião no Yogurt, monta uma pauta de 5 pontos pra próxima reunião começando pelas pendências que ficaram abertas.`
8. **Cruzamento da semana:** `Procura em todas as minhas reuniões dos últimos 7 dias no Yogurt tudo que falamos sobre [tema] e mostra o que mudou.`
9. **Conteúdo a partir da reunião:** `Na minha última reunião no Yogurt, extrai 3 dores reais e 3 frases fortes ditas lá pra virar ideia de vídeo curto ou post, sem citar nomes nem dados privados.`

## O que é verdade e o que merece atenção
- **Privacidade e aviso:** sempre avise quem está na chamada que você vai gravar. Enquanto usa só o Yogurt, nada sai do seu computador. Ao ligar o MCP no Claude, o texto que o Claude ler via MCP pode ir pro modelo online da Anthropic.
- **Mac vs Windows/Linux:** gravação sem robô, transcrição, resumo e MCP funcionam nos três sistemas. Detecção automática de nomes de falantes e integração direta com o app de Calendário são só no Mac (no Windows e Linux você usa link privado do calendário).
- **Memória:** mínimo 8 GB de RAM; com 16 GB ou mais ele baixa um modelo de resumo maior e mais detalhado. Computadores mais simples transcrevem logo após o fim da chamada.

## O que eu conferi (28/11/2026)
- Repositório oficial `FrigadeHQ/yogurt` (3.776★, licença MIT, versão `v0.3.82` de 27/11/2026) e documentação completa.
- Os 3 links diretos de download ativos no dia (Mac DMG 182 MB, Windows EXE 423 MB, Linux AppImage 535 MB).
- O que não foi testado ao vivo: abertura do aplicativo desktop e gravação de chamada real (documentação oficial e links dos instaladores conferidos no dia).

## O próximo passo
Foi ligando ferramentas abertas assim com o Claude que eu montei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=reuniao-no-claude)
