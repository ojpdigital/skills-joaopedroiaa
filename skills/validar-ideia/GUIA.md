# Teste a sua ideia de negócio no Claude antes de gastar

**Founder Skill**: 11 skills grátis (licença MIT) que funcionam como um time de startup dentro do Claude Code.
Link: https://github.com/Jakeschincariol/founder-skill

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta nova e cole (troque a ideia pela sua):

```text
Instala e roda pra mim a skill validar-ideia do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois testa a minha ideia no modo rápido: <o que eu vendo>, <preço>, pra <quem é o cliente>.
```

Ele instala as 11 skills do Founder Skill, roda o conselho e os 20 compradores simulados e te devolve as notas, quem topou e a objeção que mais travou.

## Instalar na mão (o jeito que eu testei em 21/11/2026)

Precisa do Claude Code e do Python 3.8 ou mais novo (sem instalar nada além disso). As skills são grátis; o Claude Code em si roda com plano pago do Claude ou crédito de API. No chat comum dá pra colar 1 SKILL.md e usar o método, mas sem os clientes simulados.

```bash
git clone https://github.com/Jakeschincariol/founder-skill.git
mkdir -p .claude/skills
cp -r founder-skill/skills/founder-* .claude/skills/
```

Isso instala no projeto (a pasta onde você abre o Claude Code). Pra valer em todo projeto, copie pra `~/.claude/skills/`.
Jeito mais curto, que o autor ensina (eu não testei esse): cole o link do repositório no Claude e escreva `install skill`.

## Usar

Abra o Claude Code na pasta e escreva a sua ideia com preço e cliente. Exemplo do que eu mandei:

> Minha ideia de negócio: um serviço de posts com IA pra pequenos negócios do bairro (salão, pizzaria, pet shop), R$ 297 por mês, 12 posts e 8 stories, eu crio tudo com ChatGPT e Canva. Cliente-alvo: dono de pequeno negócio local no Brasil, fatura R$ 15 a 60 mil por mês, cuida do Instagram sozinho no celular. Rode /founder-board e depois /founder-consumer --quick (20 compradores).

Ordem das 11 (cada uma lê o que a anterior escreveu na pasta `founder/`):
board → competitors → consumer → pricing → offer → cfo → marketing → brand → ops → launch → plan

| Comando | O que faz |
|---|---|
| `/founder-board` | 3 conselheiros (oferta, monopólio, produto, com os livros do Hormozi, do Peter Thiel e a biografia do Steve Jobs) dão nota e votam |
| `/founder-consumer` | cria compradores simulados (100 por padrão; `--quick` = 20), cada um com renda, rotina e objeção, e conta quem compra e por quê |
| `/founder-offer` | monta a oferta em cima das objeções e testa de novo nos mesmos compradores |
| `/founder-pricing`, `/founder-cfo` | faixa de preço e conta de margem |
| `/founder-plan` | junta tudo num plano com veredito: lucrativo, ainda não ou incompleto |

Dica: rode primeiro com `--quick` (20 compradores). Os 100 são 100 chamadas de agente e gastam bem mais do seu limite.

## O meu resultado (21/11, versão rápida)

- Conselho: oferta 4/10, monopólio 3/10, produto 4/10 (média 3,7). Motivo: qualquer um faz isso com ChatGPT e Canva, e a promessa era "post", não "cliente".
- 20 clientes simulados: **nenhum topou**. 14 travaram na confiança; um deles disse: "Ninguém me mostrou que post feito com IA traz cliente no meu WhatsApp."
- O que mudaria a cabeça deles: 1 mês de teste sem fidelidade, caso real de um negócio do bairro, e post feito com as fotos do próprio negócio.

Cuidado (o próprio painel avisa): cliente simulado não é cliente. Serve pra achar a objeção antes de gastar, não pra prever venda. O Claude sugeriu, no fim do meu teste, confirmar com 3 a 5 pessoas de verdade.

## E o próximo passo

Foi com o Claude também que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. Se você quer ver como um personagem feito com IA vira um negócio de verdade, [eu mostro na aula](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=validar-ideia).
