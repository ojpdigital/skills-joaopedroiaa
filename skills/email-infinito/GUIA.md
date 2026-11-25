# Um e-mail só, um endereço pra cada cadastro

## O jeito mais fácil: a IA monta pra você
Cole no Claude Code (ou no app do Claude):

```text
Instala e roda pra mim a skill email-infinito do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois monta o truque do + no meu Gmail e gera o arquivo de filtros com o meu nome. Meu usuário do Gmail é: <o que vem antes do @>.
```

No app ou no site do Claude, troque a primeira frase por "Lê a skill em https://github.com/ojpdigital/skills-joaopedroiaa/blob/main/skills/email-infinito/SKILL.md e segue".

## 1. O ponto não muda nada no Gmail

O Gmail ignora o ponto antes do @. Se o seu e-mail é `joaosilva@gmail.com`, estes também chegam na sua caixa:

- `joao.silva@gmail.com`
- `jo.ao.sil.va@gmail.com`
- `j.o.a.o.s.i.l.v.a@gmail.com`

Quem diz é o próprio Google: "Se o remetente acrescentar pontos desnecessários ao seu endereço de e-mail, você receberá a mensagem mesmo assim." (Ajuda do Gmail, "Pontos são irrelevantes nos endereços do Gmail": https://support.google.com/mail/answer/7436150?hl=pt-BR)

Atenção: isso vale pra conta @gmail.com. E-mail de empresa ou escola no Google (seudominio.com) trata o ponto como parte do nome.

## 2. O sinal de + vira um endereço novo pra cada site

Tudo que vem depois de um `+` (até o @) é ignorado na entrega. O próprio Google ensina: "Basta adicionar um sinal de adição (+) e qualquer palavra antes de @ no seu endereço." (Centro de aprendizagem do Google Workspace, "Dicas para otimizar a caixa de entrada do Gmail": https://support.google.com/a/users/answer/9308648?hl=pt-BR). Então:

| Onde você vai se cadastrar | Use este endereço |
|---|---|
| Farmácia | `SEUNOME+farmacia@gmail.com` |
| Mercado | `SEUNOME+mercado@gmail.com` |
| Loja on-line | `SEUNOME+loja@gmail.com` |
| App de entrega | `SEUNOME+delivery@gmail.com` |
| Banco | `SEUNOME+banco@gmail.com` |
| Viagem | `SEUNOME+viagem@gmail.com` |
| Jogo | `SEUNOME+jogos@gmail.com` |
| Sorteio e promoção | `SEUNOME+sorteio@gmail.com` |
| Newsletter | `SEUNOME+news@gmail.com` |
| Aplicativo novo | `SEUNOME+app@gmail.com` |
| Trabalho e vaga | `SEUNOME+vagas@gmail.com` |
| Rede social | `SEUNOME+social@gmail.com` |

Como saber quem vazou: chegou spam? Abra o e-mail e olhe o campo **Para**. Se estiver `SEUNOME+farmacia@gmail.com`, foi o cadastro da farmácia que passou o seu e-mail pra frente.

Isso funciona quando o site repassa o endereço do jeito que você cadastrou; quem apaga o `+farmacia` antes de repassar some com o rastro.

Cuidado: alguns sites não aceitam o `+` no cadastro (dão erro de "e-mail inválido"). Nesses, use a versão com ponto do item 1.

## 3. Os filtros prontos (cada cadastro numa pasta sozinho)

O arquivo `filtros-gmail.xml` cria 12 marcadores, um por endereço da tabela acima.

1. Abra o `filtros-gmail.xml` num bloco de notas e troque `SEUNOME` pelo seu nome de usuário do Gmail (o que vem antes do @). Salve.
2. No Gmail pelo computador: engrenagem > **Ver todas as configurações** > aba **Filtros e endereços bloqueados**.
3. Lá embaixo: **Importar filtros** > **Escolher arquivo** > o `filtros-gmail.xml` > **Abrir arquivo**.
4. Marque os filtros e clique em **Criar filtros**.

Daqui pra frente, o que chegar em `SEUNOME+farmacia@gmail.com` cai no marcador **Cadastros/farmacia**, e assim por diante.

## 4. Receber no voce@seudominio.com.br de graça pela Cloudflare, se você já tem um domínio (Email Routing)

Serve pra ter `contato@seudominio.com.br` chegando no seu Gmail, sem pagar caixa de e-mail. Precisa de um domínio seu, com o DNS na Cloudflare (a conta da Cloudflare é grátis; o domínio você paga onde registrou).

1. No painel da Cloudflare: **Compute** > **Email Service** > **Email Routing**.
2. **Onboard Domain** > escolha o seu domínio. A Cloudflare mostra os registros que vai criar (MX pra receber, TXT de SPF e DKIM) > **Done**.
3. **Destination Addresses** > digite o seu Gmail > enviar. Abra o e-mail que chegar e clique em **Verify email address**.
4. Volte em **Email Routing** > o domínio > aba **Routing Rules** > **Create routing rule**: em **Email pattern** escreva o nome (ex.: `contato`), em **Action** escolha **Send to an email**, em **Destination** o seu Gmail > **Save**.
5. Pra ter um endereço por cadastro sem criar regra nenhuma: na mesma aba, ligue a **Catch-all rule** (fica **Active**) mandando pro seu Gmail. Aí `farmacia@seudominio.com.br`, `loja@seudominio.com.br` e qualquer outro nome chegam na sua caixa.
6. O `+` também funciona aqui (subaddressing): ligue em **Email Routing** > **Settings**. `contato+loja@seudominio.com.br` cai na regra do `contato`.

A mudança no DNS costuma valer em 5 a 15 minutos no domínio que já está na Cloudflare (até 24 h no pior caso).

Limite: o Email Routing só RECEBE e encaminha. Pra responder como `contato@seudominio.com.br` precisa de outro passo (envio pelo Gmail com servidor de saída), que não está aqui.

Fontes: https://developers.cloudflare.com/email-routing/get-started/enable-email-routing/ e https://developers.cloudflare.com/email-routing/setup/email-routing-addresses/ ("Email Routing supports subaddressing, also known as plus addressing, as defined in RFC 5233"; Catch-all: "forwards every email sent to your domain [...] to a single destination").

## Um passo além

Esse truque do + serve pra mais uma coisa: ter um e-mail pra cada perfil novo que você abrir, sem criar outra conta. Vai precisar disso se quiser criar um personagem com IA, como eu fiz com o Seu João, um senhor que não existe e posta todo dia sem eu aparecer. [Gravei uma aula mostrando como eu criei ele, do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=email-infinito)
