#!/usr/bin/env python3
"""Gera dist/<skill>.zip de cada skill (o arquivo que se sobe no site do Claude).

Uso: python3 scripts/gerar-zips.py
Confere antes que a versão em skills/<skill>/VERSION é a mesma do marketplace.json
(é ela que faz o Claude Code entregar a atualização). Para anexar numa release:
  gh release create v<versão> dist/*.zip --title "..." --notes-file CHANGELOG.md
"""
import json, pathlib, sys, zipfile

raiz = pathlib.Path(__file__).resolve().parent.parent
plugins = json.loads((raiz / ".claude-plugin/marketplace.json").read_text())["plugins"]
dist = raiz / "dist"; dist.mkdir(exist_ok=True)
erros = 0
for p in plugins:
    nome = p["name"]; pasta = raiz / "skills" / nome
    v = (pasta / "VERSION").read_text().strip()
    if v != p.get("version"):
        print(f"ERRO {nome}: VERSION diz {v}, marketplace.json diz {p.get('version')}"); erros += 1; continue
    # o site do Claude recusa o upload com description acima de 1024 caracteres (medido em 14/11/2026)
    desc = next((l.split(":", 1)[1].strip() for l in (pasta / "SKILL.md").read_text().split("---")[1].splitlines()
                 if l.startswith("description:")), "")
    if not desc or len(desc) > 1024:
        print(f"ERRO {nome}: description do SKILL.md com {len(desc)} caracteres (o site aceita de 1 a 1024)"); erros += 1; continue
    destino = dist / f"{nome}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(pasta.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(raiz / "skills"))
    with zipfile.ZipFile(destino) as z:  # o site exige SKILL.md dentro da pasta da skill
        assert f"{nome}/SKILL.md" in z.namelist(), f"{nome}: SKILL.md fora do lugar"
    print(f"{destino.relative_to(raiz)}  v{v}")
sys.exit(1 if erros else 0)
