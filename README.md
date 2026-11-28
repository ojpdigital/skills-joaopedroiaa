# Skills do @joaopedroiaa para o Claude

As skills que eu entrego no Instagram, prontas pra usar. Você cola uma mensagem no Claude e ele instala e já faz o trabalho. Cada skill tem também um guia passo a passo, se você preferir fazer à mão.

| Palavra no Instagram | Skill | O que faz | Guia |
|---|---|---|---|
| FOTOS | [organizar-galeria](skills/organizar-galeria) | Organiza milhares de fotos em pastas por assunto, com tags e duplicadas, sem mover nem apagar nada | [GUIA](skills/organizar-galeria/GUIA.md) |
| CORTES | [cortes-virais](skills/cortes-virais) | Acha os 5 melhores cortes de um vídeo longo do YouTube, com início, fim, título e gancho | [GUIA](skills/cortes-virais/GUIA.md) |
| DESIGN | [design-fino](skills/design-fino) | As 10 regras que deixam uma tela feita por IA com cara de produto profissional | [GUIA](skills/design-fino/GUIA.md) |
| EMAIL | [email-infinito](skills/email-infinito) | Infinitos e-mails num Gmail só, com filtros prontos que separam tudo sozinho | [GUIA](skills/email-infinito/GUIA.md) |
| FOUNDER | [validar-ideia](skills/validar-ideia) | Testa uma ideia de negócio antes de você gastar tempo e dinheiro com ela | [GUIA](skills/validar-ideia/GUIA.md) |
| MARKETING | [time-de-marketing](skills/time-de-marketing) | Um time de marketing dentro do Claude: copy, SEO, anúncio, e-mail e conselho de estratégia | [GUIA](skills/time-de-marketing/GUIA.md) |
| CLAUDE | [claude-do-seu-jeito](skills/claude-do-seu-jeito) | O Claude aprende quem você é, monta o seu segundo cérebro e cria a sua primeira skill | [GUIA](skills/claude-do-seu-jeito/GUIA.md) |
| VIRAL | [desmontar-viral](skills/desmontar-viral) | Desmonta um vídeo viral em gancho, cenas, falas e o porquê de ter funcionado | [GUIA](skills/desmontar-viral/GUIA.md) |
| CELULAR | [ia-no-celular](skills/ia-no-celular) | Roda uma IA no seu celular, sem internet e de graça | [GUIA](skills/ia-no-celular/GUIA.md) |
| VOX | [video-estilo-vox](skills/video-estilo-vox) | Vídeo explicativo animado no estilo Vox a partir de um roteiro, em mp4 | [GUIA](skills/video-estilo-vox/GUIA.md) |
| HTML | [html-no-lugar-de-markdown](skills/html-no-lugar-de-markdown) | O Claude entrega relatório e plano em página HTML bonita em vez de texto corrido | [GUIA](skills/html-no-lugar-de-markdown/GUIA.md) |
| ARMADILHA | [armadilha-anti-copia](skills/armadilha-anti-copia) | Protege o seu site ou app contra cópia por IA sem mudar nada pro usuário | [GUIA](skills/armadilha-anti-copia/GUIA.md) |
| SITE | [site-pra-negocio](skills/site-pra-negocio) | Acha no Google Maps negócio bem avaliado sem site e faz o site dele pra você mostrar pro dono | [GUIA](skills/site-pra-negocio/GUIA.md) |
| CLIENTES | [achar-clientes](skills/achar-clientes) | Monta a sua primeira lista de clientes com o Sellbird, de graça, sem nenhum e-mail sair sem você aprovar | [GUIA](skills/achar-clientes/GUIA.md) |
| ESTUDIO | [estudio-de-animacao](skills/estudio-de-animacao) | 3 skills grátis que viram o Claude Code num estúdio de animação: história, cenas, narração, música, 3D e efeito sonoro | [GUIA](skills/estudio-de-animacao/GUIA.md) |
| PLUGIN | [plugin-superpowers](skills/plugin-superpowers) | O Superpowers: o Claude pergunta antes, mostra o plano em partes e só anda com o seu ok | [GUIA](skills/plugin-superpowers/GUIA.md) |
| PERSONAGEM | [personagem-com-ia](skills/personagem-com-ia) | A ficha e os prompts pra criar um personagem de IA que posta vídeo todo dia no seu lugar, pro seu perfil ou o seu negócio | [GUIA](skills/personagem-com-ia/GUIA.md) |
| TOKEN | [economizar-tokens](skills/economizar-tokens) | O modo oficial do Claude Code em que o Sonnet trabalha e o Opus só aconselha, com os subagentes no Haiku, pro limite durar mais | [GUIA](skills/economizar-tokens/GUIA.md) |
| RECRIAR | [recriar-qualquer-coisa](skills/recriar-qualquer-coisa) | O Craft Anything: estuda um site, jogo ou app e o Claude Code monta a sua versão, conferindo com o original | [GUIA](skills/recriar-qualquer-coisa/GUIA.md) |
| DARK | [canal-dark-3d](skills/canal-dark-3d) | Monta o seu Short de canal dark em 3D no formato "X vs Y": a ideia, o roteiro em fases, as cenas em corte com as etiquetas, a narração e a pergunta do próximo desafio | [GUIA](skills/canal-dark-3d/GUIA.md) |
| AVATAR | [virality](skills/virality) | A skill virality do Jake Schincariol em português: as perguntas dos seus clientes viram roteiro viral com o gancho medido, e o seu clone grava na Avatrix sem você pegar na câmera | [GUIA](skills/virality/GUIA.md) |

## O jeito mais fácil: cole uma mensagem no Claude

Abra o Claude Code (no terminal ou no app) na pasta onde você quer trabalhar e cole a mensagem abaixo, trocando `<nome da skill>` pelo nome da tabela e o fim pelo que você quer:

```text
Instala e roda pra mim a skill <nome da skill> do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois <o que você quer que ele faça>.
```

Exemplo:

```text
Instala e roda pra mim a skill validar-ideia do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois valida a minha ideia: um app que lembra o idoso de tomar remédio pelo WhatsApp.
```

O que o Claude faz com a mensagem está no [INSTALL.md](INSTALL.md): baixa este repositório, copia só a skill que você pediu pra pasta `.claude/skills` do seu projeto e já faz a tarefa. Ele não pede senha e não paga nada sem você dizer "sim". Cada GUIA já traz a mensagem pronta da sua skill.

Usa o Codex, o Cursor ou outra IA que roda no terminal? A mesma mensagem funciona: ela lê o INSTALL.md e segue.

## No site ou no app do Claude (modo conversa)

Lá o Claude não clona repositório. Tem dois jeitos:

1. Mais rápido: cole na conversa "Lê a skill em https://github.com/ojpdigital/skills-joaopedroiaa/blob/main/skills/<nome da skill>/SKILL.md e segue" e depois o que você quer.
2. Pra deixar instalada: baixe o zip da skill na [página de versões](https://github.com/ojpdigital/skills-joaopedroiaa/releases/latest) (por exemplo `validar-ideia.zip`), vá em Personalização > Skills > Adicionar skill > Fazer upload e escolha o zip, sem abrir.

No site funcionam inteiras: cortes-virais (sem o corte do arquivo), email-infinito, claude-do-seu-jeito, ia-no-celular, html-no-lugar-de-markdown, personagem-com-ia e canal-dark-3d. As outras instalam ferramentas ou mexem em arquivos do seu computador e precisam do Claude Code; no site elas te explicam o caminho, mas não rodam.

## Ou na mão, pelo sistema de plugins do Claude Code

```bash
claude plugin marketplace add ojpdigital/skills-joaopedroiaa
claude plugin install validar-ideia@skills-joaopedroiaa --scope project
```

Troque `validar-ideia` pelo nome da skill. Pra atualizar: `claude plugin update <nome>@skills-joaopedroiaa`.

## Perguntas comuns

**Quanto custa?** As skills são de graça. Algumas usam projetos abertos de outras pessoas (o link de cada um está no GUIA). O que você precisa ter é o Claude: o Claude Code roda no plano pago do Claude ou com crédito de API. Nenhuma skill gasta dinheiro sem você dizer "sim".

**Preciso saber programar?** Não. Você cola a mensagem e o Claude faz o resto. Se ele pedir pra instalar algo (Python, Node, ffmpeg), ele te diz o que é e espera o seu ok.

**Deu erro no meio.** Cole o erro na mesma conversa e peça "resolve e continua". Se não andar, abra o GUIA da skill e siga à mão.

**O que mudou em cada versão?** Está no [CHANGELOG](CHANGELOG.md).

## Quem fez

Eu sou o João Pedro ([@joaopedroiaa](https://www.instagram.com/joaopedroiaa/)). Eu testo essas ferramentas e mostro no Instagram o que funciona de verdade. O que eu faço hoje com IA é o Seu João: um senhor que não existe e posta todo dia sem eu aparecer. [Gravei uma aula mostrando como montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=readme&utm_campaign=skills)
