# IA no seu celular, sem internet e de graça

O app se chama **Off Grid AI**. É de código aberto (licença MIT), tá no GitHub ([off-grid-ai/OGAM](https://github.com/off-grid-ai/OGAM)) e tem nas duas lojas. Ele baixa um modelo de IA pro celular e roda tudo ali dentro: depois do download, funciona no modo avião.

## Quer ajuda passo a passo?
Cole no Claude (app, site ou Claude Code):

```text
Lê a skill ia-no-celular do @joaopedroiaa em https://github.com/ojpdigital/skills-joaopedroiaa/blob/main/skills/ia-no-celular/SKILL.md e me guia, um passo de cada vez, pra rodar IA no meu celular sem internet. Meu celular é: <modelo do seu celular>.
```

Ele te diz de onde baixar, qual modelo cabe no seu aparelho e espera você fazer cada passo.

## 1. Instalar

- **iPhone:** App Store, "Off Grid AI - Private Local AI" (grátis, pede iOS 17 ou mais novo, 167 MB). https://apps.apple.com/br/app/off-grid-local-ai/id6759299882
- **Android:** Play Store, "Off Grid AI" (mais de 100 mil downloads). https://play.google.com/store/apps/details?id=ai.offgridmobile
- **Android sem loja:** o APK oficial fica nos Releases do GitHub: https://github.com/off-grid-ai/OGAM/releases/latest
- Baixe só desses três lugares. App "igual" em site estranho é onde mora vírus.

Na primeira vez, ele mede a memória (RAM) do seu celular e sugere o tamanho de modelo que cabe.

## 2. Qual modelo baixar (pela memória do celular)

Vá em **Models** e busque pelo nome. Os modelos "sem filtro" costumam ter no nome **Dolphin**, **abliterated** ou **uncensored**.

| Memória do celular | Modelo | Tamanho | O que eu vi no teste |
|---|---|---|---|
| 4 GB | Dolphin 3.0 Llama 3.2 **1B** (Q4_K_M) | 0,8 GB | rápido, mas o português sai confuso |
| 6 a 8 GB | Dolphin 3.0 Llama 3.2 **3B** (Q4_K_M) | 2,0 GB | responde em português e não se recusa; texto simples |
| 12 GB ou mais | modelo de 7-8B (Qwen 3, Llama 3.1) | 4-5 GB | não testei aqui |

Dica: comece pelo menor. Se ficar rápido, troca pelo de cima.

## 3. Usar sem internet

1. Baixe o modelo com Wi-Fi.
2. Ligue o modo avião.
3. Abra uma conversa nova e escolha o modelo baixado.

O app também gera imagem no celular (Stable Diffusion): você escreve o que quer e ele desenha. Nos celulares mais fracos demora mais.

## 4. Cuidados

- **"Sem censura" = o modelo não recusa a pergunta.** Ele também erra e inventa: confira antes de usar a resposta.
- Na App Store ele está marcado **18+**.
- No Android ele pede várias permissões (câmera, microfone, arquivos, calendário) porque tem voz, visão e ferramentas. Só libere a do recurso que você for usar.
- A versão **grátis** faz o chat, a imagem e a leitura de foto. A voz que fala de volta e as "ações" são da versão Pro (paga, opcional). Não precisa dela pra nada deste guia.
- O celular esquenta e a bateria cai mais rápido enquanto o modelo trabalha.

## O que eu testei antes de te mandar (23/11/2026)

- O app existe e é o mesmo nas lojas e no GitHub (App Store BR: grátis; GitHub `off-grid-ai/OGAM`, MIT).
- O APK oficial (v0.0.125, 290 MB) bate com a assinatura publicada no GitHub (sha256 `6c63d593…a9c4f7`) e usa o llama.cpp por dentro.
- Rodei os dois modelos Dolphin da tabela com a **internet cortada** (o `curl` no Google falha) pelo mesmo motor do app: o de 1B respondeu a 82 tokens (pedaços de palavra) por segundo e o de 3B a 19, num processador de computador.
- **Não testei dentro de um celular.** O teste foi no computador, com o mesmo motor e os mesmos modelos. No celular a velocidade depende do aparelho.

## O próximo passo

IA no celular é a base. Eu fui além: criei com IA um personagem, o Seu João, um senhor que não existe e posta vídeo todo dia sem eu aparecer. [Gravei uma aula mostrando na tela como eu montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=ia-no-celular)
