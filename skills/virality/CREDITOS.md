# Créditos e o que mudou

**Original:** a skill `virality` do pacote
[Jakeschincariol/master-skills](https://github.com/Jakeschincariol/master-skills), de Jake
Schincariol (@opusjake, opusjake.ai), licença MIT (texto em `LICENSE-original-MIT`). Baixada em
27/11/2026. O método é dele: os 6 passos, as regras duras, as 26 fórmulas de gancho, o painel de
notas, o ranking pela mediana do criador, o humanizer e o formato do roteiro.

**Adaptação:** João Pedro (@joaopedroiaa), 27/11/2026, pra quem fala português e grava com o
clone da Avatrix no lugar do HeyGen. Só o necessário:

| Onde | O que mudou | Por quê |
| --- | --- | --- |
| `SKILL.md`, `templates/` | Traduzidos pro português; exemplo do modelo de roteiro em reais | Público brasileiro |
| `SKILL.md`, passo 1 | Acrescentado "O tema: as perguntas que os clientes já fazem" | É o caminho que o próprio Jake mostra no vídeo do AVATAR (Claude acha as perguntas, a skill vira roteiro) |
| `SKILL.md`, passo 7 + `references/avatrix.md` | Novo: gerar o vídeo com o clone na Avatrix | No vídeo do Jake essa parte é no HeyGen |
| `tools/hookscore.py` | Listas de palavras e padrões em português SOMADOS aos do original (você, R$, mil, "nesse vídeo"...) | Em português a nota e o PAYOFF davam errado (R$ não contava como dinheiro, "você" não contava como falar com quem assiste) |
| `tools/hooks.json` | Padrões em português no fim do `match` de cada uma das 26 fórmulas | Pra dar nome à fórmula de gancho em português |
| `tools/slop.json` | Bloco `pt-falado` e 3 estruturas `pt-*` | Vícios de texto de IA em português |
| `tools/test_virality.py` | Aceita `FALA:` além de `SAY:` no modelo | O modelo foi traduzido |

**O que não mudou:** `collect.py`, `swipe.py`, `speech.py`, `title.py`, `humanize.py` e
`detect.py` (só ganharam uma linha de comentário), os pesos e a conta da nota do `hookscore.py`.
Conferido em 27/11/2026: os 78 ganchos em inglês da biblioteca saem com a mesma nota e a mesma
fórmula do original, e os 13 testes do pacote passam.

**Limites conhecidos:** a calibragem da nota (AUC 0,83 / 0,56) foi medida em inglês. O `speech.py`
lê "R$ 3.243" como número em inglês, então o tempo de fala de valor em reais sai aproximado:
confira com o áudio.
