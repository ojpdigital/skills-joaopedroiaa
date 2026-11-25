# Site pronto pra negócio que não tem site (Claude + Google Maps)

Na minha busca de hamburgueria em Juiz de Fora, 21 de 24 não tinham site próprio: na ficha aparece "Adicionar website" ou só o link do delivery. Com 3 prompts o Claude acha esses negócios, puxa os dados da ficha e monta um site de uma página com a cara do lugar, pra você mostrar pro dono.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta nova e cole (troque o tipo de negócio e a cidade pelos seus). A skill e o agent-browser são grátis; o Claude Code roda no plano pago do Claude ou com crédito de API.

```text
Instala e roda pra mim a skill site-pra-negocio do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois acha negócio sem site de hamburgueria em <sua cidade> e faz o site do melhor.
```

Ele precisa de um navegador pra abrir o Google Maps. Se o seu Claude Code ainda não tiver um, ele pode pedir pra instalar o Node e o agent-browser (grátis) e espera o seu ok antes, ou te passa os prompts 1 e 2 pra você colar na extensão Claude no Chrome e faz o site com o que você trouxer de volta.

## Na mão, com os 3 prompts
Os prompts 1 e 2 precisam de um Claude que abra páginas no navegador (a extensão Claude no Chrome, ou o Claude Code com navegador, que o jeito mais fácil acima instala pra você). O prompt 3 não precisa de navegador: é só texto (no meu teste ele rodou no Claude Code; no site do Claude eu não testei).

**Prompt 1. Achar quem não tem site.** Troque o que está entre `< >`:

```text
Pesquisa no Google Maps "<tipo de negócio> em <cidade>". Abre um por um os resultados com nota 4,5 ou mais (pelo menos os 20 primeiros) e olha o botão "Website" de cada ficha.
Classifica cada um em:
- SEM SITE: não tem botão de website (aparece "Adicionar website");
- SÓ LINK: o "website" é link de delivery (iFood, anota.ai, goomer, saipos, cardapioweb, menudino), WhatsApp, Instagram, Facebook, Linktree, bio.site ou beacons;
- TEM SITE: domínio próprio do negócio.
Me devolve uma tabela com: nome, nota, bairro, telefone, classificação e o que aparece no lugar do site. Põe primeiro os SEM SITE com a nota mais alta. No fim, a conta: quantos abriu, quantos SEM SITE, quantos SÓ LINK, quantos TEM SITE.
```

**Prompt 2. Puxar tudo de um negócio.** Escolha um SEM SITE com nota alta:

```text
Abre a ficha do "<nome do negócio>" no Google Maps e puxa tudo o que estiver lá, sem inventar nada:
nome exato, categoria, nota e número de avaliações, endereço completo, bairro, telefone, horário de cada dia da semana, serviços (comer no local, retirada, entrega), faixa de preço, o resumo das avaliações e as 8 avaliações mais úteis (frase curta e o nome de quem escreveu), pratos ou serviços mais citados, cardápio com preço se aparecer em foto ou no menu, Instagram, e o que as fotos mostram (fachada, ambiente, produtos, cores da marca).
O que não aparecer na ficha, escreve "não aparece na ficha". Entrega tudo num bloco de texto só, pronto pra copiar.
```

Se o Maps abrir em "visualização limitada" (sem avaliações e sem o horário da semana), entre na sua conta Google no Chrome e rode de novo (isso eu não testei na extensão).

**Prompt 3. Gerar o site.** Numa conversa nova, cole o bloco do prompt 2 e, logo abaixo:

```text
Com esses dados, faz o site deste negócio num arquivo HTML só (CSS dentro do arquivo, sem framework, abre direto no navegador e no celular).
Regras:
- Use só o que está nos dados. Prato, preço, foto, avaliação ou número que não estiver ali NÃO entra. Onde faltar cardápio, põe o botão "Peça o cardápio" que liga ou abre o WhatsApp do número da ficha.
- Primeira dobra: nome, a nota com as estrelas, uma frase curta do que o negócio é, e 2 botões: "Ligar/Pedir agora" (tel: ou WhatsApp) e "Como chegar" (link do Google Maps com o endereço).
- Depois: horário da semana (com "aberto agora"/"fechado agora" calculado no navegador), o que as pessoas dizem (só avaliações reais), endereço com o mapa embutido do Google, e rodapé com telefone e endereço.
- Cores e clima tirados da categoria e das fotos descritas (hamburgueria: escuro com laranja/vermelho de brasa; padaria: creme e marrom; barbearia: preto e dourado). Tipografia forte no título.
- Mobile primeiro: botões grandes, nada cortado em tela de 390 px.
- Responda só com o código completo do arquivo.
```

Copie o código da resposta num arquivo de texto e salve como `site-<nome>.html` (no Bloco de Notas do Windows, escolha "Todos os arquivos" em Tipo, senão ele vira `.html.txt`; no Mac, no TextEdit, antes de salvar vá em Formatar > Converter em Texto Simples). Abra com dois cliques no Chrome, aperte F12 e depois Ctrl+Shift+M (no Mac, Cmd+Shift+M) pra ver na largura de celular.

## O meu teste (25/11/2026)
- Pesquisei "hamburgueria em Juiz de Fora" no Google Maps e abri 24 fichas uma por uma: 3 com site próprio, 16 só com link de delivery, WhatsApp ou rede social, e 5 sem nada.
- O de nota mais alta entre os sem site: Carioca Hambúrgueres, 4,9, com "Adicionar website" na ficha.
- Com os dados da ficha, o prompt 3 gerou o site num HTML só, sem prato inventado (onde não tinha cardápio, o botão liga pro número da ficha), e eu conferi na largura de celular.
- O que eu não testei: a extensão Claude no Chrome (no meu teste foi o Claude Code mexendo no navegador, com os mesmos prompts) e a conversa com o dono. Nenhum negócio foi contatado.

## Antes de mostrar pro dono
- O site é uma prévia. Não publique em endereço de site (domínio, tipo nomedolugar.com.br) com o nome do negócio nem use a marca dele sem ele concordar.
- Um negócio por vez, pessoalmente ou pelo telefone da ficha. Nada de mensagem em massa.
- Os dados são do Google Maps do dia: confirme horário e telefone com o dono antes de pôr no ar.

## E o próximo passo
Fazer site pra quem não tem é um jeito de pôr o Claude pra trabalhar pra você. O meu é outro: foi com o Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=site-pra-negocio)
