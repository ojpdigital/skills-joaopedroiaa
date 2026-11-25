# Achar clientes com o Claude (Sellbird)

O Sellbird é grátis e de código aberto: [github.com/ethanplusai/sellbird](https://github.com/ethanplusai/sellbird), licença AGPL-3.0, mais de 7 mil estrelas. Ele acha as empresas que precisam do que você oferece, lê o site de cada uma pra entender do que ela precisa, acha quem decide, confere o e-mail e escreve um e-mail diferente pra cada cliente, com o link da sua agenda pra marcar a reunião. Ele pensa pelo Claude Code no seu plano Pro ou Max (ou pelo Codex no ChatGPT), sem chave de API. E nenhum e-mail sai sem você aprovar.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta qualquer e cole:

```text
Instala e roda pra mim a skill achar-clientes do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois monta a minha primeira lista de clientes com o Sellbird.
```

Ele instala, te faz 4 perguntas (o que você oferece, quem é o seu cliente, em qual cidade, quem decide), acha as empresas de graça e te entrega a lista. Pra mandar e-mail ele para e te explica antes.

## Na mão
Precisa do git (git-scm.com), do Python 3.11 ou mais novo e do Claude Code logado num plano Pro ou Max. Eu testei no Linux; os comandos abaixo valem pra Linux e Mac (no Windows, o jeito mais fácil lá em cima resolve as diferenças). No Mac o Python que vem de fábrica é o 3.9: rode `brew install python@3.13` e use `python3.13` no lugar de `python3`.

1. Instalar:
```bash
git clone https://github.com/ethanplusai/sellbird.git && cd sellbird
python3 -m venv .venv && source .venv/bin/activate && pip install -e .
```
2. Contar o que você oferece: `sellbird train https://seusite.com.br` (ele lê o seu site e monta o cliente ideal). Sem site, abra `claude` dentro da pasta e diga "set up Sellbird for me": ele pergunta e monta. Esse passo usa o seu Claude logado; eu não consegui testar ele aqui (no meu teste eu escrevi o cliente ideal à mão no arquivo `sellbird.local.yaml`, com o [modelo que está na skill](SKILL.md#passo-3-o-cliente-ideal-com-ele-em-4-perguntas)). O tipo de negócio nesse arquivo vai em inglês ou espanhol (`dentist`, `lawyer`, `panaderia`...): a lista está na skill.
3. Achar as empresas, de graça:
```bash
sellbird signals --confirm free
sellbird discover
sellbird companies --out minha-lista.csv
```
4. Ver tudo no painel: `sellbird dashboard` (abre o link que ele mostrar; as empresas ficam em People > Companies).

## O meu teste (25/11/2026)
- Com "dentista em Campinas", o `sellbird discover` achou 51 clínicas e leu o site de 13, custo US$ 0 (fonte grátis: OpenStreetMap).
- O servidor principal do mapa grátis recusou a rede do meu servidor (erro "406"). Rodou quando eu troquei pra outro servidor do mesmo mapa; a skill explica como, se acontecer com você. Da rede de casa eu não testei.
- O que eu não testei: o `sellbird train` e a escrita e o envio dos e-mails. Esses passos rodam no seu Claude Code logado; aqui o Claude da máquina de teste não estava logado num plano. Então: testado até a lista de empresas.

## Pra não queimar o seu domínio
- Mande de um domínio separado do principal, nunca do e-mail do dia a dia.
- Aqueça a caixa por 2 a 3 semanas antes do primeiro envio (`sellbird warmup` diz se está pronta).
- Comece com 20 a 30 e-mails por dia por caixa.
- Deixe no modo aprovação: cada e-mail espera em Outbound > "Waiting for you" no painel (ou `sellbird outbox`) até você aprovar.
- Todo e-mail com o seu nome, o endereço da empresa e um jeito de sair da lista. Respeite a LGPD: nada de lista pronta de terceiros.
- Sem um verificador de e-mail ligado, o Sellbird não manda pra endereço que ele só adivinhou (`sellbird recommended` mostra qual o autor recomenda; tem opção com plano grátis).

## Onde a fonte grátis não chega
O mapa grátis acha negócio com endereço: dentista, clínica, advogado, contador, farmácia, supermercado, padaria, encanador, eletricista e mais alguns (no arquivo, com o nome em inglês ou espanhol que a skill lista). Academia, imobiliária, restaurante ou salão pedem uma das fontes pagas (`sellbird discover --providers` mostra o custo antes; a mais barata sai por uns US$ 0,37 a cada 1.000 empresas, com depósito mínimo de US$ 50 pra começar).

## O próximo passo
Achar cliente é a parte de ir atrás. O que eu faço com a IA é o contrário: conteúdo que traz a pessoa até mim sem eu aparecer. Foi com o Claude que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=achar-clientes)
