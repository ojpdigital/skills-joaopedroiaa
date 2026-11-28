# Seu clone viraliza por você: a skill virality com a Avatrix

A virality é a skill que o Jake Schincariol (@opusjake) divulga pra escrever
vídeo curto viral com o Claude. Ela é grátis, de código aberto (licença MIT), e o método é todo
dele: acha os vídeos que estão bombando no seu nicho, desmonta por que deram certo, reescreve no
seu jeito, mede o gancho e entrega o roteiro pronto. Eu traduzi pro português, ensinei as
ferramentas dela a ler português e troquei a gravação do HeyGen pelo seu clone na Avatrix.

O caminho, igual ao do vídeo:
1. Você faz o seu clone uma vez (fotos e voz).
2. O Claude acha as perguntas que os seus clientes vivem fazendo, sobre você ou sobre o seu
   concorrente.
3. A virality transforma a pergunta num roteiro viral.
4. O seu clone grava o vídeo. Você não pega na câmera.

## O jeito mais fácil: a IA faz tudo
Abra o Claude (Claude Code, site ou app) e cole:

```text
Instala pra mim a skill virality do @joaopedroiaa: o passo a passo está em https://raw.githubusercontent.com/ojpdigital/skills-joaopedroiaa/main/INSTALL.md, lê e segue. Depois liga o conector da Avatrix com o endereço https://avatrix.io/mcp e começa comigo: acha as perguntas que os meus clientes mais fazem.
```

No site ou no app do Claude, sem terminal: baixe o zip da skill na [página de versões](https://github.com/ojpdigital/skills-joaopedroiaa/releases/latest), suba em Configurações > Plugins > Adicionar > Fazer upload de plugin, e ligue a Avatrix em Configurações > Plugins > Adicionar > Adicionar conector personalizado, com o nome Avatrix e o endereço `https://avatrix.io/mcp`.

## 1. O seu clone (uma vez só)
Em [avatrix.io](https://avatrix.io): **Personagens > Novo personagem > Clonagem completa > Começar
a clonagem > Sou eu ou uma pessoa real**. A tela pede fotos de verdade em 7 ângulos e a sua voz,
gravada ali mesmo ou enviada (só a voz, sem música, de 10 segundos a 3 minutos; o ideal é 1
minuto), e a confirmação de que a pessoa autorizou. O clone é só seu: rosto e voz de outra
pessoa, não.

## 2. As perguntas dos seus clientes
Peça ao Claude: "acha as perguntas que os clientes mais fazem sobre mim e sobre <concorrente 1>,
<concorrente 2>". Ele procura em comentários, avaliações e fóruns públicos e devolve cada pergunta
com o link de onde saiu. As que você recebe no direct e no WhatsApp, você cola.

## 3. O roteiro
Escolha uma pergunta e digite `/virality` (ou "faz um roteiro viral dessa pergunta"). Na primeira
vez ele pede 3 a 5 vídeos ou legendas suas, pra aprender o seu jeito de falar. Ele devolve 5
ganchos com nota, o roteiro em batidas (fala, texto na tela e imagem), a legenda e a palavra pra
comentar. Número que ele não sabe vira `{{seu número}}`: ele nunca inventa.

## 4. O vídeo com o seu clone
- **No site da Avatrix:** Chat IA > Escolher personagem (o seu clone) > cola o roteiro e pede o
  vídeo. Pra mudar qualquer coisa, pede ali mesmo.
- **Pelo Claude com o conector:** ele gera a sua voz e o vídeo em blocos de até 15 segundos. Antes
  de gastar, ele mostra o preço em créditos e só gera quando você responde "sim".

Funciona pra qualquer assunto: explicação de produto, vídeo de vendas, notícia do seu nicho.

## O meu teste (27/11/2026)
- Baixei a skill original do GitHub do Jake e rodei os 13 testes dela: passam, com as mudanças.
- Os 78 ganchos em inglês da biblioteca dela saem com a mesma nota e a mesma fórmula de antes. Em
  português, a nota e o "resultado no começo" passaram a funcionar (antes R$ e "você" não contavam).
- Usei a skill pra escrever o roteiro do meu próprio vídeo do AVATAR: gancho com nota 83 (STRONG),
  texto com nota 86 de "cara de gente" (PASS), 38,9 segundos.
- Conferi as telas da Avatrix (Clonagem completa e Chat IA com Escolher personagem).
- O que eu não testei: gerar o vídeo com o clone até o fim (não gastei crédito) e a instalação no
  site do Claude.

## Bom saber
- Nada garante view. A skill aumenta a chance copiando o formato do que já está funcionando e
  acertando o gancho antes de gravar.
- Ela não entra na sua conta, não posta e não manda mensagem. Quem posta é você.
- O original, em inglês: [github.com/Jakeschincariol/master-skills](https://github.com/Jakeschincariol/master-skills). O que eu mudei está no `CREDITOS.md`.

## O próximo passo
Foi na Avatrix que eu criei o Seu João, um senhor que não existe e posta
vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando como ele foi montado do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=virality)
