#!/usr/bin/env python3
"""Vorschaubild 1200 × 630 im CI von KLEIN. MITTEL. KI.

    python3 tools/vorschaubild.py --kategorie "Studien & Zahlen" --titel "…" --out entwuerfe/<slug>/vorschaubild.png

Erzeugt zusätzlich <out>.jpg (Titelbild). Braucht Playwright mit Chromium und assets/logo.png
(wird beim ersten Lauf von storage.ghost.io geladen, falls die Domain erlaubt ist).
"""
from __future__ import annotations

import argparse
import html
import shutil
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
LOGO = ROOT / "assets" / "logo.png"
LOGO_URL = ("https://storage.ghost.io/c/21/ce/21ce7042-8409-412c-8993-487e5282e70b/"
            "content/images/2026/09/KMK-Logo-aus-Brandboard.png")
INK, LIME, GRAU = "#111111", "#D7FF00", "#45453F"


def ensure_logo(path: Path | None) -> Path:
    if path:
        return path
    if LOGO.exists():
        return LOGO
    try:
        ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt") if Path("/root/.ccr/ca-bundle.crt").exists() \
            else ssl.create_default_context()
        with urllib.request.urlopen(LOGO_URL, context=ctx, timeout=30) as r, LOGO.open("wb") as f:
            shutil.copyfileobj(r, f)
        return LOGO
    except Exception as e:
        sys.exit(f"FEHLER: Logo fehlt ({LOGO}) und konnte nicht geladen werden: {e}\n"
                 f"Lösung: storage.ghost.io in der Umgebung erlauben oder Logo als assets/logo.png einchecken.")


def page(kategorie: str, titel: str, logo: Path) -> str:
    def face(fam, file, w):
        return f"@font-face{{font-family:'{fam}';src:url('{(FONTS / file).as_uri()}') format('woff2');font-weight:{w};}}"
    fonts = "".join([face("Schibsted Grotesk", "schibsted-grotesk-latin-700-normal.woff2", 700),
                     face("Instrument Sans", "instrument-sans-latin-500-normal.woff2", 500),
                     face("Instrument Sans", "instrument-sans-latin-600-normal.woff2", 600)])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#fff;position:relative;overflow:hidden;font-family:'Instrument Sans'}}
.wrap{{position:absolute;inset:84px 84px 0 84px}}
.kat{{display:inline-block;font:600 24px/1 'Instrument Sans';letter-spacing:4px;text-transform:uppercase;color:{INK};
padding-bottom:12px;border-bottom:6px solid {LIME}}}
h1{{margin-top:40px;font:700 68px/1.1 'Schibsted Grotesk';color:{INK};max-width:1032px;letter-spacing:-0.5px}}
.logo{{position:absolute;left:84px;bottom:66px;width:340px}}
.url{{position:absolute;right:84px;bottom:74px;font:500 24px/1 'Instrument Sans';color:{GRAU}}}
.kante{{position:absolute;left:0;right:0;bottom:0;height:14px;background:{LIME}}}
</style></head><body><div class="wrap"><span class="kat">{html.escape(kategorie)}</span>
<h1 id="t">{html.escape(titel)}</h1></div>
<img class="logo" src="{logo.as_uri()}"><div class="url">kleinmittelki.de</div><div class="kante"></div></body></html>"""


FIT_JS = """() => { const h = document.getElementById('t'); let size = 68;
  const lines = () => Math.round(h.getBoundingClientRect().height / (size * 1.1));
  while (lines() > 3 && size > 48) { size -= 4; h.style.fontSize = size + 'px'; }
  const logoTop = document.querySelector('.logo').getBoundingClientRect().top;
  return {size, lines: lines(), ueberlappt: h.getBoundingClientRect().bottom > logoTop - 24}; }"""


def render(kategorie: str, titel: str, out: Path, logo: Path | None = None) -> dict:
    from playwright.sync_api import sync_playwright
    logo = ensure_logo(logo)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".html")
    tmp.write_text(page(kategorie, titel, logo), encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.goto(tmp.as_uri())
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        info = pg.evaluate(FIT_JS)
        pg.screenshot(path=str(out))
        pg.screenshot(path=str(out.with_suffix(".jpg")), type="jpeg", quality=90)
        b.close()
    tmp.unlink()
    if info["lines"] > 3 or info["ueberlappt"]:
        sys.exit(f"FEHLER: Titel passt nicht ({info}). Titel kürzen.")
    return info


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--kategorie", required=True)
    ap.add_argument("--titel", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--logo", help="anderes Logo (nur zum Testen)")
    a = ap.parse_args()
    info = render(a.kategorie, a.titel, Path(a.out), Path(a.logo) if a.logo else None)
    print(f"Vorschaubild: {a.out} (Schrift {info['size']} px, {info['lines']} Zeilen)")
