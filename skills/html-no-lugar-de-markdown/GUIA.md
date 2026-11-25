# Pare de pedir Markdown: 5 prompts pra o Claude te entregar HTML

De onde vem a ideia: o post "Using Claude Code: The unreasonable effectiveness of HTML", do Thariq Shihipar, do time do Claude Code na Anthropic, publicado em 20/05/2026 (claude.com/blog, lido em 24/11). Ele escreve que parou de usar Markdown pra quase tudo e que outras pessoas do time do Claude Code estão fazendo o mesmo.

A ideia em 1 frase: o Markdown só mostra título, negrito e lista; o HTML mostra tabela, design, desenho (SVG), código, interação, fluxo, posição na tela e imagem. Quando você pede HTML, o Claude para de "descrever" o gráfico e desenha ele.

Como usar: cole o prompt no Claude (chat, Claude Code, Codex ou outro), salve a resposta como `arquivo.html` e abra no navegador (2 cliques no arquivo). No Claude Code ele já salva e você só abre.

Os 5 exemplos da pasta [`exemplos/`](exemplos/) foram gerados pelo Claude no chat em 24/11/2026, a partir destes mesmos prompts, e abertos no Chrome. O `0-o-mesmo-plano-em-markdown.md` é o exemplo 1 em Markdown, pra você comparar.

## O jeito mais fácil: a IA já trabalha assim
Abra o Claude Code (ou o Codex) na pasta do seu projeto e cole:

```text
Instala pra mim a skill html-no-lugar-de-markdown do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois deixa a regra fixa no meu CLAUDE.md e já me entrega em HTML um plano com 6 jeitos de abrir um vídeo sobre <seu tema>.
```

No site ou no app do Claude (modo conversa): cole o prompt do tipo que você quer, logo abaixo, e salve a resposta como `arquivo.html`.

## 1. Plano e exploração: várias opções lado a lado

```
Me dá 6 jeitos bem diferentes de abrir um reel sobre <tema>. Monta tudo num único arquivo HTML, em grade: um card por opção, com a fala dos 2 primeiros segundos, 2 etiquetas do tipo de gancho, uma barra com a força que você daria pra ele e o risco de cada um. Fundo claro, destaque em laranja.
```
Exemplo: `exemplos/1-plano-6-ganchos.html`.

## 2. Revisão: o que mudou, com nota do lado

```
Compara a versão antiga e a nova deste texto/código: <cola as duas>. Faz um HTML com o diff de verdade (o que saiu em vermelho, o que entrou em verde) e, do lado de cada trecho, uma nota curta colorida por gravidade: precisa olhar, vale conferir, ok.
```
Exemplo: `exemplos/2-revisao-de-mudancas.html`.

## 3. Design e protótipo: ajusta mexendo, não descrevendo

```
Faz um HTML com uma prévia de legenda animada de reel dentro de um celular e controles do lado: tamanho da letra, altura na tela, velocidade por palavra e cor de destaque. Mostra os valores escolhidos em JSON pra eu copiar.
```
Exemplo: `exemplos/3-prototipo-legenda.html` (mexa nos controles).

## 4. Relatório e explicação: com gráfico e diagrama desenhados

```
Escreve um relatório de 1 página em HTML comparando <A> e <B>: 3 números grandes no topo, um gráfico de barras em SVG que anima ao abrir e um diagrama de fluxo em SVG com setas mostrando como eu uso. Nada de imagem externa.
```
Exemplo: `exemplos/4-relatorio-com-grafico.html`.

## 5. Editor sob medida: organiza arrastando e exporta

```
Faz um HTML com estas ideias como cards arrastáveis em 4 colunas: Agora, Depois, Talvez e Corta. Um botão Exportar mostra em JSON o que ficou em cada coluna. Ideias: <lista>.
```
Exemplo: `exemplos/5-editor-de-ideias.html` (arraste um card e clique em Exportar).

## Pra deixar fixo no Claude Code (CLAUDE.md)

Cole no `CLAUDE.md` do seu projeto:

```
## Formato das entregas
- Plano, spec, relatório e resumo de mudanças saem num único arquivo .html (CSS e JS dentro do arquivo, sem nada externo), não em Markdown.
- Use tabela pra dado, SVG pra gráfico e diagrama, e controles (slider, botão, arrastar) quando eu tiver que escolher valores.
- Markdown só pra arquivo curto que o próprio agente lê (instrução, config).
```

A última linha é escolha minha, não do post: o Thariq diz que parou de usar Markdown pra quase tudo, mas se chama de "maximalista do HTML". Sobre gastar mais token, ele diz que o HTML gasta mais, mas que você lê muito mais e a resposta sai melhor.

## O próximo passo

Foi com esse mesmo Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. O HTML é ótimo pra você entender o que a IA fez; o que paga mesmo é a IA fazer o vídeo sem precisar de você. [Gravei uma aula mostrando como eu montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=html-no-lugar-de-markdown)
