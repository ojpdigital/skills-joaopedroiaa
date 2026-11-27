# Personagem com IA: a ficha e os prompts

Um personagem de IA é uma pessoa que não existe, com rosto, voz e jeito de falar sempre iguais, que aparece todo dia nos seus vídeos no seu lugar. Serve pro seu perfil ou pro seu negócio (loja, pet shop, clínica, restaurante). Aqui estão a ficha e os 6 prompts pra criar o seu, do zero, colando no Claude ou no ChatGPT.

## O que você vai precisar
- O Claude ou o ChatGPT. Os prompts são só texto e rodam em qualquer plano dos dois, inclusive no gratuito, dentro do limite de mensagens dele.
- Pra fazer o vídeo: um gerador de imagem que aceite foto de referência (você sobe uma foto e ele faz a mesma pessoa em outra cena), um gerador de voz e um gerador de vídeo de avatar (você sobe uma foto e um áudio e ele faz a pessoa da foto falar). Existem vários. O preço deles muda o tempo todo: muitos têm teste ou plano grátis com limite e cobram pra usar mais. Veja o preço no site antes de assinar qualquer um.

## O jeito mais fácil: a IA faz com você
No Claude Code, numa pasta nova, cole (troque o negócio e a cidade pelos seus):

```text
Instala e roda pra mim a skill personagem-com-ia do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois cria um personagem de IA pro meu pet shop em Goiânia.
```

No site do Claude, cole: "Lê a skill em https://github.com/ojpdigital/skills-joaopedroiaa/blob/main/skills/personagem-com-ia/SKILL.md e segue. Quero um personagem de IA pro meu <negócio> em <cidade>." Se ele (ou o ChatGPT) disser que não consegue abrir o link, use os prompts abaixo, um por vez.

A IA te faz 5 perguntas, monta a ficha do personagem e vai passo a passo até o primeiro roteiro.

## Na mão, com os 6 prompts
Abra uma conversa nova no Claude ou no ChatGPT e cole um prompt por vez, na ordem. Onde estiver `[cole a ficha aqui]`, cole a ficha que saiu do prompt 1. Guarde a ficha num lugar fácil (um documento ou uma nota no celular): você vai usar ela em todo vídeo.

### 1. A ficha do personagem
Cole e responda as perguntas. No fim sai a ficha: nome, idade, de onde vem, jeito de falar, bordão, o que ele ensina, o que ele nunca diz, a aparência, a voz.

```text
Você vai me ajudar a criar um personagem de IA que vai postar vídeo curto todo dia no meu lugar (Reels, TikTok, Shorts).
Primeiro me entrevista: faz estas 5 perguntas, UMA DE CADA VEZ, e espera a minha resposta antes da próxima. Se eu responder "não sei", me dá 3 sugestões curtas e eu escolho.
1. O personagem é pro meu perfil pessoal ou pra um negócio? Se for negócio: qual, em qual cidade, o que ele oferece e o que tem de diferente de verdade? Se for perfil pessoal: sobre o que é o perfil?
2. Pra quem o personagem fala: quem é a pessoa que eu quero que assista (idade, onde mora, o que ela procura)?
3. Que personagem eu imagino? Idade, homem ou mulher, de onde vem, jeito (engraçado, carinhoso, bravo, sabe-tudo...).
4. O que ele vai ensinar ou mostrar todo dia? (dicas, bastidores, dúvidas que os clientes sempre fazem, novidades)
5. O que ele nunca pode falar? (ex.: preço que muda, promessa de resultado, falar mal de concorrente, palavrão, política)

Depois das 5 respostas, me devolve a ficha preenchida neste formato. Não inventa fato do meu negócio: preço, horário, serviço, endereço ou área de atendimento que eu não disse fica [CONFIRMAR].

FICHA DO PERSONAGEM
- Nome:
- Idade:
- De onde vem:
- Quem é (3 frases de história; deixa claro que é um personagem criado com IA, não um funcionário ou cliente de verdade):
- Para quem fala:
- O que ensina ou mostra (5 temas que rendem vídeo toda semana):
- Jeito de falar (ritmo e 3 palavras ou expressões típicas dele):
- Bordão de abertura (até 4 palavras; ele fala no começo de todo vídeo):
- Bordão de fechamento (até 7 palavras; ele fala antes do "comenta"):
- O que ele nunca diz:
- Aparência fixa (rosto, cabelo, pele, olhos, corpo, a roupa de sempre da cabeça aos pés e um acessório marca registrada):
- Cenário fixo (onde ele aparece em todo vídeo):
- Voz (homem ou mulher, idade que a voz aparenta, sotaque, velocidade, timbre):
- Dados do negócio que ele pode citar (só o que eu disse):

Regras: o personagem não pode ter o rosto, o nome ou a voz de uma pessoa real ou famosa. Nada de promessa de ganho, de cura ou de resultado garantido.
```

### 2. O rosto fixo
Esse prompt escreve a descrição da foto-base (a foto oficial do personagem) pra você colar num gerador de imagem.

```text
Com a ficha abaixo, escreve o prompt da FOTO-BASE do personagem, pra eu colar num gerador de imagem.
O prompt tem, nesta ordem: tipo de foto (foto realista, como tirada com um celular bom, vertical 9:16); enquadramento (do peito pra cima, de frente, olhando direto pra câmera, boca fechada com um leve sorriso); o rosto em detalhe (formato, idade aparente, pele, rugas ou marcas, olhos, sobrancelha, nariz, boca, cabelo, barba ou bigode); a roupa de sempre e o acessório marca registrada; o cenário fixo atrás dele, um pouco desfocado; a luz (natural, suave, de frente); e no fim: "sem texto, sem logotipo, sem marca d'água, mãos fora do quadro".
Me entrega o prompt em português e em inglês (alguns geradores entendem melhor em inglês), cada um num bloco pra copiar.
Depois escreve mais 2 prompts curtos pras fotos de apoio, que eu vou gerar usando a foto-base como referência: 1) o mesmo personagem de corpo inteiro, no mesmo cenário; 2) o mesmo personagem de três quartos (rosto levemente virado). Os dois começam com "Mesma pessoa da foto de referência, mesmo rosto, mesma roupa, mesmo cenário".
O rosto não pode lembrar nenhuma pessoa real ou famosa.

FICHA:
[cole a ficha aqui]
```

A regra que faz o personagem nunca mudar de cara:
- Gere de 4 a 8 opções da foto-base, escolha a melhor e nunca mais troque. Gere as 2 fotos de apoio subindo a foto-base como referência.
- Guarde as 3 numa pasta só. Toda imagem nova dele sai com a foto-base subida como referência. Nunca gere o rosto do zero de novo: cada vez que você gera do zero, sai uma pessoa diferente.
- Todo vídeo sai de uma dessas fotos, com a mesma roupa e o mesmo cenário.

### 3. A voz
Uma voz só, sempre a mesma. Três caminhos:
1. Escolher uma voz pronta na biblioteca de vozes de um gerador de voz.
2. Desenhar uma voz nova a partir de uma descrição (alguns geradores fazem isso).
3. Clonar a sua própria voz, gravando uns minutos.

Não clone a voz de outra pessoa (funcionário, parente, famoso, locutor) sem autorização dela, por escrito.

Esse prompt descreve a voz pra você buscar e te dá uma frase de teste pra comparar as candidatas:

```text
Com a ficha abaixo, me ajuda a escolher a voz do personagem.
1. Escreve a descrição da voz em uma linha, do jeito que se busca numa biblioteca de vozes (ex.: "homem, 60 anos, sotaque do interior, fala calma, voz grave e rouca"), em português e em inglês.
2. Escreve uma frase de teste de uns 15 segundos, no jeito de falar dele, com o bordão de abertura e o de fechamento, pra eu ouvir as vozes candidatas falando a mesma coisa.
3. Me dá 3 critérios pra escolher entre as candidatas.
4. Monta a linha que eu vou guardar na ficha depois de escolher: "Voz: <nome ou código da voz> | ferramenta: <qual> | velocidade: <x> | outras configurações: <x>".

FICHA:
[cole a ficha aqui]
```

Escolheu? Anote na ficha o nome da voz e as configurações, e use sempre igual.

### 4. O roteiro a partir de um viral
Ache um vídeo que viralizou no seu nicho (o prompt 6 te ajuda) e pegue o texto falado: copie a legenda automática do app ou digite ouvindo. Se você usa o Claude Code, a skill [desmontar-viral](../desmontar-viral) deste repositório tira a transcrição sozinha. O prompt reescreve o vídeo com a mesma estrutura e o mesmo tempo, na voz do seu personagem, com os exemplos do seu negócio, sem copiar o texto.

```text
Você vai reescrever um vídeo que viralizou no meu nicho pro meu personagem, sem copiar o texto.
Abaixo estão a FICHA do personagem e a TRANSCRIÇÃO do viral. Faz assim:
1. Divide a transcrição em frases e dá a função de cada uma (gancho, apresentação, lista, prova, oferta, fechamento, chamada pra ação...) e o número de palavras.
2. Escreve uma frase nova pra cada frase do original: mesma função, mesma ordem, e até 3 palavras a mais ou a menos que a original. O total do roteiro novo fica até 15% maior ou menor que o original, pra o vídeo ter o mesmo tempo.
3. Quem fala é o personagem: no jeito de falar e com as expressões da ficha. O bordão de abertura entra antes da primeira frase (conta no total). O bordão de fechamento substitui a frase de fechamento do original; se o original não tiver uma, ele entra logo antes da chamada pra ação. A última frase é sempre "Comenta <PALAVRA> ..." e é a única que pode fugir da regra das 3 palavras (até 10 palavras); se eu ainda não escolhi a palavra, escreve [PALAVRA].
4. Troca os exemplos do viral pelos do meu negócio, usando só os dados da ficha. Produto, serviço, preço, horário ou endereço que não está na ficha não entra; se a estrutura pedir um, escreve [CONFIRMAR: o que falta]. Se a ficha põe limite (só em tal bairro, só pra tal porte, só em tal dia), a frase diz o limite.
5. Não copia: nenhum trecho de 5 palavras seguidas igual ao original, e nenhum nome, marca, slogan ou bordão do vídeo original.
6. Me entrega:
   a) a tabela: nº | função | frase original | palavras | frase nova | palavras;
   b) o total de palavras do original e do novo, e o tempo de cada um (conta 2,5 palavras por segundo);
   c) o roteiro final só com as falas, uma por linha, pronto pra colar no gerador de voz;
   d) a lista do que ficou [CONFIRMAR], pra eu checar antes de gravar.

FICHA:
[cole a ficha aqui]

TRANSCRIÇÃO DO VIRAL:
[cole a transcrição aqui]
```

Se o roteiro ficar comprido demais, peça: "encurta pra caber em <tantos> segundos, sem mudar a ordem".

### 5. O "comenta" e o direct
O vídeo fecha com "comenta <palavra>" e quem comenta recebe no direct uma coisa útil: no pet shop, a tabela de preço do banho e tosa; na clínica, o link pra agendar uma avaliação; no restaurante, o cardápio do dia.

```text
Com a ficha e o roteiro abaixo, monta o fechamento do vídeo e a mensagem do direct.
1. Me sugere 3 palavras pro "comenta": uma palavra só, curta, sem acento, ligada ao que a pessoa vai receber (ex.: BANHO, TABELA, AVALIACAO). Eu escolho uma.
2. Escreve a última fala do vídeo na voz do personagem, até 10 palavras: "Comenta <PALAVRA> que eu te mando <o que ela recebe>".
3. Escreve a mensagem do direct que chega pra quem comentou, até 600 caracteres: começa com o personagem cumprimentando a pessoa pelo nome ({nome}), entrega a coisa útil na hora (ex.: pet shop: a tabela de preço do banho e tosa por porte; clínica: o link pra agendar uma avaliação; restaurante: o cardápio do dia; perfil pessoal: a lista ou o passo a passo que o vídeo prometeu), diz o próximo passo (agendar, responder com uma informação, chamar no WhatsApp), diz como falar com uma pessoa da equipe, e termina com o bordão de fechamento.
4. Regras: preço, horário, link e endereço só da ficha; o que faltar vira [PREENCHER]. Sem promessa de ganho, de cura ou de resultado, e sem pressa falsa ("só hoje", "últimas vagas") se não for verdade.

FICHA:
[cole a ficha aqui]

ROTEIRO:
[cole o roteiro aqui]
```

Onde aparece `{nome}`, entra o nome de quem comentou: troque na mão ou deixe a ferramenta trocar sozinha. A palavra e o direct se repetem enquanto você entregar a mesma coisa; rode o prompt 5 de novo só quando mudar.

Você pode responder o direct na mão ou com uma ferramenta de resposta automática de comentário pra direct (tem grátis e paga; veja o preço antes).

### 6. A rotina: 1 viral por dia vira 1 vídeo
Rode uma vez pra saber onde procurar e o que postar na semana:

```text
Com a ficha abaixo, me dá:
1. 10 termos de busca pra eu achar, no Reels, no TikTok e no Shorts, vídeos que viralizaram no meu nicho (o que o meu cliente pesquisaria, não o nome da minha loja).
2. 5 sinais de que um vídeo é bom pra eu usar de modelo (ex.: visualizações muito acima do número de seguidores do perfil, comentários com perguntas, fala do começo ao fim, até 60 segundos).
3. Os 5 temas da ficha virando 7 ideias de vídeo pra esta semana, uma por dia, cada uma com o gancho da primeira frase. As ideias respeitam o "O que ele nunca diz" da ficha.

FICHA:
[cole a ficha aqui]
```

Todo dia:
1. Ache 1 viral do seu nicho e guarde o link.
2. Pegue o texto falado dele.
3. Rode o prompt 4 com a ficha e troque a [PALAVRA] pela palavra do direct que está valendo.
4. Confira preço, horário e serviço com quem sabe.
5. Gere o áudio com a voz de sempre.
6. Gere o vídeo com a foto-base de sempre e o áudio.
7. Ponha legenda, marque que é conteúdo feito com IA (o rótulo de IA do Instagram e do TikTok) e poste.
8. Responda os comentários e mande o direct.

## O meu teste (26/11/2026)
- Pedi "quero um personagem pra divulgar meu pet shop em Goiânia" e respondi a entrevista com dados inventados. Saiu o Vô Dito, um avô goiano de 67 anos que abre com "Ô trem bão, sô!" e fecha com "Bicho cheiroso é bicho feliz, uai!".
- O roteiro saiu de um viral real de pet shop: 70 palavras no original, 78 no novo (uns 31 segundos), mesma ordem frase a frase, e nenhum trecho de 5 palavras seguidas igual.
- Está tudo na pasta [exemplo-pet-shop](exemplo-pet-shop): a [ficha](exemplo-pet-shop/ficha.md), a [foto-base](exemplo-pet-shop/foto-base.txt) e o [roteiro com o direct](exemplo-pet-shop/roteiro.md).
- O que eu não testei aqui: gerar a foto, a voz e o vídeo. Neste teste foram só os prompts de texto.

## Pra fazer do jeito certo
- O personagem é inventado: marque o vídeo como feito com IA quando a rede oferecer o rótulo, e não ponha ele dando depoimento como se fosse cliente ou funcionário de verdade.
- Nada de rosto ou voz de pessoa real ou famosa sem autorização dela.
- Preço, horário e serviço só entram se você confirmou. O que a IA não souber, ela marca [CONFIRMAR] ou [PREENCHER].
- Clínica, veterinário, dentista ou estética: sem promessa de cura ou de resultado; siga as regras de propaganda do conselho da sua profissão.

## O próximo passo
É assim que eu fiz o Seu João, um senhor de 70 anos da roça que não existe e já passou de 355 mil seguidores. Se quiser ver como eu montei ele do zero, eu gravei uma aula: o link chega no direct.
