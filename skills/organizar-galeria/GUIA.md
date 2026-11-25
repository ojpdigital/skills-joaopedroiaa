# Organize a sua galeria com o Claude (sem arrastar foto nenhuma)

O que vem aqui: `organizar.py` (separa e copia), `rotular.sh` (passa as folhas pro Claude), `PROMPT-MESTRE.md` (o que o Claude recebe).
Nada é movido nem apagado: o script só COPIA pra uma pasta nova. Os originais ficam do jeito que estavam.

## O jeito mais fácil: a IA faz tudo
Abra o Claude Code na pasta onde estão as fotos e cole:

```text
Instala e roda pra mim a skill organizar-galeria do @joaopedroiaa: clona https://github.com/ojpdigital/skills-joaopedroiaa, lê o INSTALL.md e segue os passos. Depois organiza as fotos da pasta <caminho da pasta> sem mover nem apagar nada.
```

Ele instala, prepara o Python, gera as folhas, rotula, mostra a conta e só copia quando você disser que pode. O passo a passo abaixo é o mesmo, à mão.

## Antes de começar (uma vez)

1. Python 3 (Mac e Linux já têm; no Windows, instale o WSL com Ubuntu e rode tudo lá dentro).
2. Pillow, num ambiente isolado (o `pip install` direto falha no Ubuntu 24 e no WSL com "externally-managed-environment"):
   ```
   python3 -m venv .venv && . .venv/bin/activate && pip install pillow
   ```
   No Ubuntu/WSL dá pra usar o pacote do sistema: `sudo apt install python3-pil`.
   Fotos HEIC do iPhone: `pip install pillow-heif` (dentro do mesmo `.venv`). Sem isso as HEIC aparecem como cinza na folha.
3. Claude Code instalado e logado (`claude` no terminal) para a rota 2A. Sem ele, use a rota 2B.

**O que eu testei e o que não:** testei no Linux (Ubuntu), com Claude Code, em 1.125 arquivos e depois em 10.000 arquivos. NÃO testei no Mac, no Windows sem WSL, no app do Claude (rota 2B), com HEIC nem com o celular direto. Os comandos são os mesmos no Mac; se algo falhar, me conta.

## Se as fotos estão no celular

Passe tudo pra uma pasta do computador (cabo, AirDrop, Google Fotos > baixar). Pode estar em subpastas (álbuns, Takeout do Google Fotos): o script entra em todas. Ponha numa pasta, por exemplo `galeria`. O script lê a pasta, não o celular.

## 1. Gerar as folhas de 16 miniaturas

```
python3 organizar.py folhas galeria saida
```
Mostra quantas imagens, vídeos e duplicadas achou (duplicada = arquivo idêntico, mesmo conteúdo, nome diferente) e cria `saida/folhas/folha-001.jpg`...

## 2A. Rota A: o Claude olha as folhas sozinho (Claude Code)

```
./rotular.sh saida 4
```
Ele manda 5 folhas por vez (4 ao mesmo tempo) e junta tudo em `saida/rotulos.json`. Em 1.125 arquivos levou cerca de 3 minutos; em 10.000 arquivos (527 folhas), com `./rotular.sh saida 8`, levou 12,6 minutos, mais 2 rodadas curtas pra refazer as folhas em que o Claude pulou uma miniatura.

**Se aparecer `LOTE ... FALHOU` ou `ATENÇÃO: ... lote(s) SEM rótulo`:** o limite do seu plano do Claude pode ter batido (galeria grande = muitas chamadas). Espere ou rode de novo `./rotular.sh saida 4`: ele refaz só os lotes que faltam, inclusive o lote em que o Claude deixou alguma miniatura sem resposta (o script confere as 16 de cada folha e não grava lote incompleto). Em galeria grande pode precisar de 2 ou 3 rodadas. O que ficar sem resposta cai na pasta `sem-rotulo`; só copie (passo 4) quando esse número for 0.

## 2B. Rota B: pelo app do Claude

Abra uma conversa, cole o `PROMPT-MESTRE.md`, anexe até 5 folhas de cada vez e peça o JSON. Junte as respostas num arquivo `saida/rotulos.json` no formato `{"folha-001": [...], "folha-002": [...]}`.

## 3. Ver a conta antes de copiar

```
python3 organizar.py aplicar galeria saida saida/rotulos.json
```
Mostra quantos arquivos vão pra cada pasta. Não copia nada ainda. Não gostou do nome de uma pasta? Troque a lista de pastas no `PROMPT-MESTRE.md` e rode o passo 2 de novo.

## 4. Copiar

```
python3 organizar.py aplicar galeria saida saida/rotulos.json --copiar
```
Cria `saida/organizada/<pasta>/` com as cópias e `saida/tags.csv` (arquivo, pasta, tags).

## 5. Achar qualquer foto

```
python3 organizar.py procurar saida retrato
```

## Limites que eu medi

- Folha com miniatura pequena demais pro Claude ler (print de tela com letra miúda) vira palavra solta na tag, não frase.
- O Claude erra: confira a conta do passo 3 e abra 2 ou 3 pastas antes de apagar qualquer coisa do original.

## O próximo passo

Organizar é o começo. O que eu faço hoje é a IA criar o conteúdo inteiro sem eu aparecer: foi assim que eu criei o Seu João, um senhor que não existe e posta todo dia. [Gravei uma aula mostrando como montei ele do zero.](https://tutorialdaia.site/aula/?utm_source=github&utm_medium=skill&utm_campaign=organizar-galeria)
