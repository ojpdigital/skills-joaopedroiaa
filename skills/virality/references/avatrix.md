# Passo 7 em detalhe: o vídeo com o seu clone na Avatrix

Este arquivo troca a parte do HeyGen do vídeo do Jake pela Avatrix. O roteiro que chega aqui é o
`virality/<slug>/roteiro.md` do passo 6, já aprovado. Telas do site conferidas em 27/11/2026; o
formato do pedido de vídeo é o mesmo da skill `fabrica-de-reels` da Avatrix (avatrix-io/skills).

## O que não muda

- Preço antes, gasto só com "sim". Toda chamada paga (`generate_voice`, `generate_video`,
  `generate_batch`) vai antes com `get_cost: true`. Uma linha: "O vídeo inteiro: ~N créditos
  (falas + vídeo). Posso gerar? Responde sim." Passou do combinado: pare e pergunte.
- O clone é do próprio usuário, ou de alguém que autorizou. Nunca outra pessoa.
- Nada é postado por aqui. O vídeo vai pro usuário.

## A. O clone (uma vez só, no site)

O HeyGen pede um vídeo curto seu falando. Na Avatrix são fotos e a voz:

1. avatrix.io > **Personagens** > **Novo personagem** > **Clonagem completa** > **Começar a clonagem**.
2. Passo "Quem": **Sou eu ou uma pessoa real** ("Fotos de verdade em 7 ângulos e a voz gravada na
   hora ou enviada. Pede a confirmação de que a pessoa autorizou.") e o nome do personagem.
3. Passo "Fotos": as fotos de verdade nos ângulos que a tela pedir.
4. Passo "Voz": grava ali mesmo ou envia um áudio só com a voz, sem música, de 10 s a 3 min (o
   ideal é 1 min).
5. Passo "Revisão" e salvar.

A conta tem teto de 20 personagens. Cheia, a própria tela avisa ("Apague um em Personagens pra
clonar"): nunca apague personagem do usuário por ele; diga o aviso e deixe ele escolher.

Depois, no conector: `list_influencers` e `get_influencer` no clone. A linha "Voz fixa" tem que
mostrar a voz dele. Vazia: o clone não terminou; peça pra ele conferir o passo "Voz" no site.

## B. Pelo site, sem conector (o caminho do vídeo do Jake)

1. **Chat IA** > em "Pergunte qualquer coisa", clica em **Escolher personagem** e escolhe o clone.
2. Cola o roteiro (as linhas FALA, na ordem, e o que deve aparecer em cada batida) e pede: "faz
   esse vídeo comigo falando, 9:16, com a minha voz".
3. O Chat IA mostra o plano e o preço antes de gerar; a geração acontece ali no chat. Pra mudar
   qualquer coisa, pede ali mesmo, por texto.

Diga ao usuário que esse caminho é do site: o preço e os botões são os que aparecem na tela dele.

## C. Pelo conector (o Claude gera)

Pré-requisito: a Avatrix ligada no Claude (conector `https://avatrix.io/mcp`; no site do Claude,
Configurações > Plugins > Adicionar > Adicionar conector personalizado, nome Avatrix; no Claude Code,
`claude mcp add --transport http avatrix "https://avatrix.io/mcp"` e `/mcp` pra entrar na conta). O único passo
que é do usuário é entrar na conta da Avatrix e clicar em Permitir. Sem conector: caminho B.

1. **Blocos de até 15 s.** O Persona Pro aceita áudio de até 15 s por vídeo. Divida as FALAs do
   roteiro em blocos que cabem nisso pelo `speech.py` (com o ritmo da voz do clone; voz clonada
   sai em 1,2 sem `speed`). Corte sempre entre frases, nunca no meio.
2. **As falas:** um `generate_batch` de `generate_voice`, uma frase por pedido, `text` = a frase
   como se fala (número por extenso, sem símbolo: "três mil", não "3.000"), `influencerId` = o
   clone, **sem `voiceId`** (assim sai a voz da ficha). Cotação do lote antes. Junte as frases de
   cada bloco num áudio só (`join_audio`, não cobra; ou ffmpeg com 0,35 s entre frases).
3. **O vídeo de cada bloco:** `generate_video` com `model: avatrix-persona-pro`,
   `mode: audio_to_video`, `referenceImages`: a foto do clone (a URL que `list_influencers`
   devolve), `audioUrl`: o áudio do bloco, `aspectRatio: 9:16`, `resolution: 1080p`, e o `prompt`
   no formato abaixo. A duração é a do áudio. Primeiro o bloco mais corrido, sozinho: mostre e
   espere o "gostei" antes dos outros (num lote, com a cotação antes).
4. **Juntar:** no Claude Code, `ffmpeg` com os blocos na ordem; no site, o Editor da Avatrix.
   Os textos de TELA do roteiro entram na edição, não no prompt do vídeo.
5. Quer a montagem completa, com conferência de boca, ritmo e rosto? A skill `fabrica-de-reels`
   da Avatrix faz isso com o mesmo clone.

### O pedido do vídeo (Persona Pro, 1 pessoa falando)

Em inglês, com a fala em português dentro de `<d>`, palavra por palavra a do áudio (sem a fala
escrita, a ferramenta recusa antes de cobrar):

```
subject_definitions:
<Subject 1> is the person in <Picture 1> (<Nome>): <idade>, <3 traços que se veem>, <roupa>. Any other picture shows <Subject 1> from another angle.
<Subject 2> is the <lugar> in <Picture 1>: <3 ou 4 objetos do lugar>.
<Audio 1> is the complete Brazilian Portuguese speech track: <Subject 1> (S1) speaks it.

summary:
[reference generation + audio reuse] The target video is one handheld selfie shot of <Subject 1> in <Subject 2>, speaking the line carried by <Audio 1>.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - facial identity and clothes stay exactly the same for the whole shot.
<Subject 2> (appears in [Shot 1]): fully_preserved - the place and the light stay the same, with no invented elements.
<Audio 1>: fully_copy - <Audio 1> is reused 1:1 as the target video's complete final audio track.

detailed_description:
Raw, realistic phone-camera look with natural daylight from a window, real skin texture. The phone is held at arm's length with a slight natural sway and no cuts. Only <Subject 1> speaks. No subtitles or on-screen text.
[Shot 1] Medium close-up, eyes to the lens. <Subject 1> <3 ou 4 gestos marcados em palavras da fala: "on '<palavra>' <he|she> raises one hand; on '<palavra>' <he|she> nods">. <Subject 1> (S1) says with natural synchronized mouth movement, in the exact voice and timing of <Audio 1>, <d>[Portuguese] <a fala do bloco, palavra por palavra a do áudio></d> The character says this line only once. After the last word, the character stays silent with the mouth closed until the video ends. Hands are well formed with five fingers each.

overall_soundscape:
The complete soundtrack is <Audio 1> reused 1:1, with no added music or sound effects.

non_diegetic_music:
N/A
```

Emoção vai como o que o corpo faz ("eyebrows raised, half smile"), nunca adjetivo. Não escreva o
que você não quer na cena: negação desenha a coisa.

## Quando a Avatrix recusa

- Recusa por causa do pedido (falta a fala em `<d>`, áudio acima de 15 s, foto ruim): conserte e
  mande de novo no mesmo modelo.
- O Persona Pro não aparece no `list_models` ou está fora: o Avatrix Avatar Pro com o mesmo áudio
  (`mode: audio_to_video`, `resolution: 720p`), com cotação e "sim" de novo. Diga quais blocos
  saíram por ele.
- A ferramenta diz que a voz do clone sumiu da conta: PARE e diga isso. Nunca outra voz no lugar.
- Saldo baixo: diga quanto falta. Não compre crédito por ele.

## Não testado

- O caminho B (Chat IA com o personagem escolhido e o roteiro colado) não foi gerado até o fim
  na adaptação: as telas foram conferidas, nenhum crédito foi gasto.
- Os blocos de vídeo não foram gerados nesta skill; o formato do pedido é o testado na
  `fabrica-de-reels`.
