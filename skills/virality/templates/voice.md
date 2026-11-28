# voice.md

Salve a cópia preenchida em `~/.claude/virality/voice.md`. A skill virality lê antes de toda
reescrita. Se você já preencheu `~/.claude/youtube/voice.md` ou `~/.claude/linkedin/voice.md` dos
outros pacotes do Jake, comece por ele.

## Como capturar uma voz (o Claude faz, com 3 a 5 amostras)

1. Pegue 3 a 5 peças do PRÓPRIO criador: transcrições dos melhores vídeos primeiro (palavra
   falada vale mais que escrita), depois legendas ou posts. Não o jeito que ele queria soar.
2. Meça, não chute:
   - ritmo: `python3 tools/speech.py video_dele.srt` mostra as palavras por minuto. Use como `--wpm`.
     Se o vídeo vai sair com o clone da Avatrix, meça também uma fala do clone: é o ritmo dela que
     vale pro tempo do roteiro.
   - tamanho de frase: curta e seca, misturada ou longa. Cite duas frases típicas.
   - pessoa: mais "eu" (prova), mais "você" (instrução) ou "a gente".
   - contração ("tá", "pra", "cê"), palavrão, emoji, gíria. Sim ou não, com um exemplo de cada sim.
   - expressões da casa: qualquer trecho de 2 a 4 palavras que aparece em duas ou mais amostras.
   - como ele abre e como ele pede (a primeira frase de sempre e o pedido de sempre).
3. Escreva o perfil abaixo com frases de verdade das amostras, reescreva uma linha nessa voz e
   pergunte ao criador "é você?". Corrija o perfil pela resposta.

## O perfil

- **Nome / @:**
- **Ritmo:** ___ palavras por minuto (medido em: ___)
- **Soa assim (três frases de verdade, palavra por palavra):**
  1.
  2.
  3.
- **Tamanho de frase:**
- **Pessoa:** eu / você / a gente
- **Expressões da casa (manter):**
- **Palavras que eu nunca uso (tirar):**
- **Palavras que o humanizer tem que deixar em paz** (edite `tools/slop.json` pro `humanize.py`
  e o `detect.py`):
- **Palavrão / emoji / gíria:**
- **Como eu abro:**
- **Como eu peço (pedido do fim):**
- **Palavra em inglês na fala:** escreva como se fala, pra voz do clone não errar (ex.: "dirécti", "chórti")

## Provas que eu falo em voz alta

Números, resultados e histórias reais que o criador assina embaixo. A skill nunca inventa uma.
Se esta lista estiver vazia, o roteiro volta com `{{seu número}}`.

-
-

## Fora de cogitação

- Assuntos, clientes, números ou promessas que eu não posso usar:
