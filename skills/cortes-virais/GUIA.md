# Cortes virais com o Claude: passo a passo

Pra quê: transformar um vídeo longo do YouTube (o teste foi com GTA 6) em 5 cortes verticais com início, fim, título e gancho.

## O jeito mais fácil: a IA faz tudo
Cole no Claude Code (ou no app do Claude), com a transcrição logo embaixo:

```text
Instala e roda pra mim a skill cortes-virais do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois acha os 5 melhores cortes deste vídeo: <link do vídeo>. A transcrição está aqui embaixo:
```

No app ou no site do Claude, troque a primeira frase por "Lê a skill em https://github.com/ojpdigital/skills-joaopedroiaa/blob/main/skills/cortes-virais/SKILL.md e segue". Ou cole só o prompt de [`PROMPT-CORTES.md`](PROMPT-CORTES.md) com a transcrição embaixo.

## 1. Acha o vídeo
No YouTube, no computador, procura "GTA 6" e escolhe um vídeo que está bombando agora (veja as visualizações e "há X horas"). Prefira gameplay ou live, que rende mais corte. Todo vídeo tem dono: dá o crédito do canal no corte. Vídeo de 8 a 40 minutos funciona melhor.

## 2. Copia a transcrição (no computador)
Abre o vídeo, toca em "...mais" na descrição e depois em "Mostrar transcrição". Seleciona o texto todo com os minutos e copia.
(Se o vídeo não tiver transcrição, esse vídeo não serve: escolhe outro.)

## 3. Cola no Claude com o prompt
Abre uma conversa nova no Claude, cola o prompt de [`PROMPT-CORTES.md`](PROMPT-CORTES.md) e, logo embaixo, cola a transcrição. Envia.

## 4. Recebe os 5 cortes
Em menos de um minuto ele responde, do mais forte pro mais fraco:
```
1) 07:59 a 08:49 (50s) TÍTULO
   gancho: a frase dos 2 primeiros segundos
   porque: 1 linha
```

## 5. Confere antes de cortar (30 segundos)
- Abre o vídeo no minuto de início de cada corte e vê se a frase começa onde ele disse.
- O fim que ele dá costuma ser o começo da fala seguinte: se sobrar um pedacinho da frase seguinte, tira meio segundo.

## 6. Corta no editor (grátis)
Corta no editor de vídeo que você já usa, começando cada corte na frase do gancho que o Claude deu. Conferi em capcut.com/pricing (19/11) que o CapCut tem plano grátis com edição básica; os passos dentro do CapCut e no celular eu NÃO testei. O que foi testado é do 1 ao 5, com o Claude.

## Testado em 19/11/2026
Vídeo: "GTA 6 - O INÍCIO do JOGO COMPLETO! (PS5 Pro Mundo Aberto)" (LipaoGamer, 23:50, 448 mil visualizações). A transcrição saiu pelo "Mostrar transcrição" do YouTube (157 linhas); o Claude devolveu os 5 cortes em 20,5 s, e os 10 tempos existem na transcrição. O resultado está em [`exemplo-cortes.txt`](exemplo-cortes.txt).

Respeite os direitos do vídeo original: corte de vídeo dos outros pede crédito e, em muitos casos, autorização de quem fez.

## No celular
O caminho é o mesmo (YouTube e Claude no navegador do celular), mas NÃO testei no celular. Se a transcrição não aparecer no app do YouTube, use o computador.

## O próximo passo

Corte é o começo. O que eu faço hoje é a IA criar o vídeo inteiro sem eu aparecer: foi assim que eu criei o Seu João, um senhor que não existe e posta todo dia. [Gravei uma aula mostrando como montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=cortes-virais)
