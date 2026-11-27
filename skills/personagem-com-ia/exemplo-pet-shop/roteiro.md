> EXEMPLO. Saída do teste da skill (26/11/2026), com a ficha do Vô Dito (personagem e pet shop inventados pra este exemplo). A transcrição de entrada é de um vídeo real de pet shop que viralizou, usada só como modelo de estrutura. Nenhum áudio ou vídeo foi gerado neste teste.

# Roteiro a partir de um viral (prompts 4, 5 e 6)

## Entrada: a transcrição do viral
"Quer encontrar tudo pro seu pet em um só lugar? Vem conhecer o Pet Shop JK. Aqui tem rações pra cães e gatos, inclusive opções a granel e diversas marcas. Você também encontra petiscos, coleiras, caminhas, brinquedos e acessórios pra deixar seu melhor amigo feliz. E ainda tem banho e tosa, além de produtos de jardinagem. Pet Shop JK, cuidado e carinho pro seu pet. Chama a gente no WhatsApp."

## a) Frase a frase (prompt 4)

| nº | função | frase original | palavras | frase nova | palavras |
|---|---|---|---|---|---|
| 0 | bordão de abertura | (não tem) | 0 | Ô trem bão, sô! | 4 |
| 1 | gancho (pergunta da dor) | Quer encontrar tudo pro seu pet em um só lugar? | 10 | Cansou de rodar Goiânia atrás de coisa pro seu bicho? | 10 |
| 2 | apresentação (nome e convite) | Vem conhecer o Pet Shop JK. | 6 | Chega no Pé de Pequi, no Setor Bueno. | 8 |
| 3 | lista 1 (o produto principal) | Aqui tem rações pra cães e gatos, inclusive opções a granel e diversas marcas. | 14 | Aqui tem ração pra cachorro e pra gato, de várias marcas, e a granel também. | 15 |
| 4 | lista 2 (o resto da loja) | Você também encontra petiscos, coleiras, caminhas, brinquedos e acessórios pra deixar seu melhor amigo feliz. | 15 | Tem petisco, coleira, caminha e brinquedo pra deixar o bicho todo prosa. | 12 |
| 5 | lista 3 (o serviço e o extra) | E ainda tem banho e tosa, além de produtos de jardinagem. | 11 | Banho e tosa? A gente busca e devolve no Bueno e no Marista. | 13 |
| 6 | fechamento (slogan → bordão) | Pet Shop JK, cuidado e carinho pro seu pet. | 9 | Bicho cheiroso é bicho feliz, uai! | 6 |
| 7 | chamada pra ação | Chama a gente no WhatsApp. | 5 | Comenta BANHO que eu te mando a tabela do banho. | 10 |

## b) Tempo
- Original: 70 palavras, uns 28 segundos.
- Novo: 78 palavras, uns 31 segundos (11% a mais, dentro dos 15%).
- Conferido: nenhum trecho de 5 palavras seguidas (nem de 4) igual ao original; nenhum nome ou slogan do vídeo original.

## c) Roteiro final (pra colar no gerador de voz)
Ô trem bão, sô!
Cansou de rodar Goiânia atrás de coisa pro seu bicho?
Chega no Pé de Pequi, no Setor Bueno.
Aqui tem ração pra cachorro e pra gato, de várias marcas, e a granel também.
Tem petisco, coleira, caminha e brinquedo pra deixar o bicho todo prosa.
Banho e tosa? A gente busca e devolve no Bueno e no Marista.
Bicho cheiroso é bicho feliz, uai!
Comenta BANHO que eu te mando a tabela do banho.

## d) Pra checar antes de gravar
- Nenhum [CONFIRMAR] no roteiro: todos os fatos estão na ficha.
- Corrigido na conferência: a primeira versão da frase 5 dizia "a gente busca e devolve ele cheiroso em casa", sem o limite de bairro da ficha. Quem mora fora do Bueno e do Marista ia achar que tinha busca. Virou "no Bueno e no Marista".

## O "comenta" e o direct (prompt 5)
1. **Palavras sugeridas:** BANHO, TABELA, TOSA. Escolhida no exemplo: BANHO.
2. **Última fala:** "Comenta BANHO que eu te mando a tabela do banho." (10 palavras)
3. **Mensagem do direct** (524 caracteres):

```text
Oi, {nome}! Aqui é o Vô Dito, do Pet Shop Pé de Pequi. Tá aqui a tabela do banho e tosa, uai:
Pequeno: banho R$ [PREENCHER] | banho e tosa R$ [PREENCHER]
Médio: banho R$ [PREENCHER] | banho e tosa R$ [PREENCHER]
Grande: banho R$ [PREENCHER] | banho e tosa R$ [PREENCHER]
Gato: [CONFIRMAR se atende e o preço]
Busca e entrega no Setor Bueno e no Marista: [CONFIRMAR o valor].
Pra marcar, me responde com o nome e o porte do seu bicho. Quer falar com a equipe? Chama no WhatsApp [PREENCHER].
Bicho cheiroso é bicho feliz, uai!
```

Sem preço inventado (o dono preenche), sem promessa e sem pressa falsa.

## A rotina (prompt 6)
**10 termos de busca pra achar viral do nicho:** banho e tosa; tosa higiênica; cachorro no calor; como tirar carrapato do cachorro; ração pra filhote; cachorro com medo de banho; tosa bebê; gato tomando banho; dica pra quem tem cachorro; pet shop Goiânia.

**5 sinais de um bom viral pra usar de modelo:**
1. Visualizações muito acima do número de seguidores do perfil (10 vezes ou mais).
2. Comentários com perguntas ("quanto custa?", "faz em gato?").
3. Uma pessoa falando do começo ao fim, sem depender de imagem que você não tem.
4. Até 60 segundos.
5. Postado nos últimos 3 meses.

**7 ideias pra esta semana (com o gancho):**
1. Seg (calor): "Tosar cachorro peludo no calor de Goiânia: pode ou não pode?"
2. Ter (ração): "Filhote comendo ração de adulto? Para tudo."
3. Qua (carrapato): "Três lugares onde o carrapato se esconde no seu cachorro."
4. Qui (bastidor): "Ó o que acontece com o seu bicho aqui dentro do banho."
5. Sex (balcão): "A pergunta que mais me fazem no balcão essa semana."
6. Sáb (calor): "Seu cachorro lambe a pata o dia inteiro? Olha isso."
7. Dom (balcão): "Banho toda semana estraga o pelo? Vou te contar."

Observação: as ideias 3 e 6 tocam em saúde; o vídeo termina com "na dúvida, leva no veterinário" e não cita remédio nem diagnóstico (está no "nunca diz" da ficha).
