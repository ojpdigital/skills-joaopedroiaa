# 10 ajustes finos de design, com o código pronto

Código pronto, com antes e depois de cada um (as fotos estão em [`antes-e-depois/`](antes-e-depois/); 9 abertos no Chrome, o 9 (dvh) vem da doc da MDN e a foto dele é simulação).

## 1. Raio concêntrico
Borda arredondada dentro de outra não usa o mesmo raio. O de dentro é o de fora menos o espaçamento.
```css
.card { --r: 40px; --pad: 24px; border-radius: var(--r); padding: var(--pad); }
.card > img { border-radius: calc(var(--r) - var(--pad)); } /* 16px */
```

## 2. Borda com transparência
Cinza sólido (`#d4d4d4`) fica sujo em cima de cor. Preto com transparência pega a cor do fundo.
```css
.chip { border: 1px solid rgb(0 0 0 / .1); }
/* no escuro: */ .dark .chip { border-color: rgb(255 255 255 / .1); }
```

## 3. Paleta em OKLCH
No HSL, amarelo e azul com o mesmo "50%" não têm o mesmo brilho pro olho. No OKLCH o L é o brilho que a gente vê: mesma luz, só troca o matiz.
```css
:root { --c1: oklch(70% .13 25); --c2: oklch(70% .13 145); --c3: oklch(70% .13 230); --c4: oklch(70% .13 320); } /* C .13 cabe no sRGB; acima disso a tela comum corta a cor */
```

## 4. Degradê em OKLCH
`linear-gradient(90deg, blue, yellow)` passa por um cinza no meio. Com `in oklch` ele passa pelo ciano e pelo verde.
```css
.barra { background: linear-gradient(90deg, blue, yellow); background: linear-gradient(90deg in oklch, blue, yellow); } /* a 1ª é reserva */
```

## 5. Ícone no peso do texto
Ícone de traço fino do lado de texto em negrito parece largado. Iguala o traço ao peso da fonte.
```css
.menu { font-weight: 700; }
.menu svg { stroke-width: 2.5; }   /* 400 → 1.5 · 600 → 2 · 700 → 2.5 */
```

## 6. Carrossel com máscara
Em vez do corte seco na borda, o conteúdo some aos poucos.
```css
.trilho { overflow-x: auto; mask-image: linear-gradient(to right, transparent, #000 12%, #000 88%, transparent); }
```

## 7. Desfoque na troca de ícone
Troca de "Copiar" pra "Copiado": os dois passam por um desfoque de 200 ms.
```css
.bt span { transition: opacity .2s, filter .2s, transform .2s; }
.bt .sai { opacity: 0; filter: blur(4px); transform: scale(.92); }
.bt .entra { opacity: 1; filter: blur(0); transform: scale(1); }
```

## 8. Profundidade no modo escuro
Sombra quase não aparece no fundo escuro. Quem dá profundidade é a superfície mais clara.
```css
.dark { --fundo: #0e0e10; --sup-1: #1c1c1f; --sup-2: #2a2a2f; }
.dark .card { background: var(--sup-1); box-shadow: none; }
.dark .card.destaque { background: var(--sup-2); }
```

## 9. Altura dinâmica no celular
`100vh` é a altura com a barra do navegador escondida; quando a barra aparece, ela cobre o fim da tela (o botão some). `100dvh` acompanha a barra.
```css
.tela-cheia { height: 100vh; height: 100dvh; } /* a 1ª linha fica de reserva pra navegador antigo */
```

## 10. Fundo branco da foto some com multiply
Foto de produto com fundo branco em cima de um fundo colorido: `multiply` deixa o branco transparente.
```css
.vitrine { background: #efe6d8; }
.vitrine img { mix-blend-mode: multiply; }
```
Atenção: o branco DENTRO do produto (rótulo) também tinge. Serve pra produto sem branco importante.

