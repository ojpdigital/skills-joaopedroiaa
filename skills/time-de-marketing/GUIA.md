# Um time de marketing grátis dentro do Claude

**marketingskills**, do Corey Haines: 53 skills de marketing grátis (licença MIT) pro Claude Code.
Link: https://github.com/coreyhaines31/marketingskills

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code numa pasta nova e cole (troque pelo seu produto):

```text
Instala e roda pra mim a skill time-de-marketing do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois: ninguém sabe que o meu produto existe. Produto: <o que é>, <preço>, pra <quem>. Roda o conselho de marketing e me dá o plano de amanhã.
```

## Instalar na mão

O jeito que eu testei em 21/11/2026 (copiar as pastas pro projeto):

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
mkdir -p .claude/skills
cp -r marketingskills/skills/* .claude/skills/
```

Os jeitos que o autor recomenda (eu não testei estes dois):
- `npx skills add coreyhaines31/marketingskills -a claude-code`
- dentro do Claude Code: `/plugin marketplace add coreyhaines31/marketingskills` e depois `/plugin install marketing-skills`

## Usar

Você não precisa decorar o nome das 53. Conta o problema de marketing pro Claude, do jeito que você falaria com alguém, e ele puxa a skill que serve. No meu teste de 21/11, mandei só "Ninguém sabe que o meu produto existe" com o produto e o cliente, sem nome de skill, e ele escolheu sozinho a `marketing-plan` (plano em 3 movimentos: provar com 5 negócios, prospecção ativa, antes e depois + indicação). Pra rodar o conselho, eu pedi pelo nome:

> Ninguém sabe que o meu produto existe. Produto: serviço de posts com IA pra pequenos negócios do bairro (salão, pizzaria, pet shop), R$ 297 por mês. Rode o marketing-council sobre como conseguir os 10 primeiros clientes.

Algumas das 53:

| Skill | Pra quê |
|---|---|
| `copywriting` | escreve a copy da página, do anúncio, do e-mail |
| `cro` | arruma a página pra converter |
| `pricing` | quanto cobrar e como montar os planos |
| `offers` | monta a oferta |
| `cold-email`, `prospecting` | abordagem de cliente novo |
| `marketing-council` | o conselho (abaixo) |

## O conselho (marketing-council)

São 12 conselheiros simulados, cada um com o que publicou de verdade: Alex Hormozi, David Ogilvy, Seth Godin, Eugene Schwartz, Gary Halbert, Gary Vaynerchuk, Claude Hopkins, Russell Brunson, April Dunford, Byron Sharp, Rory Sutherland e Ann Handley. No modo normal senta de 3 a 5; no modo completo, os 12. O valor está em onde eles discordam.

## O meu teste (21/11)

Sentaram 4: Gary Halbert, Alex Hormozi, Gary Vaynerchuk e Seth Godin.
- **Hormozi:** oferta difícil de recusar e volume: 100 contatos por dia.
- **Godin discordou:** um nicho só, num bairro só, e virar referência ali.
- **Halbert:** procure quem já paga por isso e fale com eles hoje.
- **Plano de amanhã que ele me deu:** escolher um nicho e um bairro, fazer 3 posts de graça pra cada um dos 10 primeiros com o perfil real deles, oferecer os 12 posts do mês pelo WhatsApp, e postar o antes e depois no seu perfil. Se ninguém pagar depois de 50 abordagens, o problema é a oferta.

Lembrete que a própria skill dá: é simulação baseada no que eles escreveram, não a opinião real deles.

## E o próximo passo

Foi com o Claude também que eu criei o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. Se você quer ver como um personagem feito com IA vira um negócio de verdade, [eu mostro na aula](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=time-de-marketing).
