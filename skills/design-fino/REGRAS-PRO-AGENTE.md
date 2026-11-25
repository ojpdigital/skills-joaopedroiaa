Cola o bloco abaixo no `CLAUDE.md` (Claude Code) ou no `AGENTS.md` (Codex e outros) do seu projeto.

```markdown
## Regras de design (aplique em todo componente novo e quando eu pedir "revisa o design")

1. Raio concêntrico: elemento arredondado dentro de outro usa border-radius = raio de fora − padding (calc(var(--r) - var(--pad))).
2. Borda: nunca cinza sólido em hex sobre fundo colorido; use rgb(0 0 0 / .1) no claro e rgb(255 255 255 / .1) no escuro.
3. Cor: paletas em oklch() com o mesmo L e o mesmo C, variando só o matiz; nada de hsl() pra paleta.
4. Degradê: sempre com espaço de cor, linear-gradient(<ângulo> in oklch, ...), pra não passar por cinza no meio.
5. Ícone SVG de traço: stroke-width acompanha o peso do texto ao lado (400 → 1.5, 600 → 2, 700 → 2.5).
6. Carrossel ou lista com rolagem horizontal: mask-image: linear-gradient(to right, transparent, #000 12%, #000 88%, transparent).
7. Troca de ícone ou de rótulo (copiar/copiado, play/pause): transition de opacity, filter: blur(4px) e scale em 200 ms; nunca troca seca.
8. Modo escuro: profundidade por superfície mais clara (#0e0e10 → #1c1c1f → #2a2a2f), sem depender de box-shadow.
9. Altura de tela cheia: height: 100vh; height: 100dvh; (a 1ª é reserva). Nunca só 100vh em elemento com botão no rodapé.
10. Foto de produto com fundo branco sobre fundo colorido: mix-blend-mode: multiply.

Depois de aplicar, abra a página no navegador e confira cada item antes de dizer que terminou.
```
