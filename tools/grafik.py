#!/usr/bin/env python3
"""Rendert ein Erklär-Schaubild (HTML-Fragment mit Klassen aus grafik_basis.css) als PNG im CI.

    python3 tools/grafik.py entwuerfe/<slug>/g1.html --out entwuerfe/<slug>/kmk-<thema>-g1.png

Das Fragment enthält nur den Inhalt, z. B.:

    <div class="g">
      <p class="g-kicker">Grafik 01 / Begriffe</p>
      <p class="g-titel">Anbieter, Produkt, Modell: drei Ebenen</p>
      <div class="g-strich"></div>
      <div class="g-stapel">
        <div class="g-box"><p class="g-name">Anbieter</p><p class="g-text">…</p></div>
        <p class="g-pfeil">↓</p>
        <div class="g-box g-box--dunkel"><p class="g-name">Modell</p><p class="g-text">…</p></div>
      </div>
      <p class="g-quelle">Stand: 18.10.2026 · Eigene Darstellung</p>
    </div>

Ausgabe: 1600 px breit (doppelte Auflösung), auf 48 Farben reduziert. Danach das PNG ansehen!
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
CSS = ROOT / "tools" / "grafik_basis.css"

VERBOTEN = ["linear-gradient", "radial-gradient", "box-shadow", "<script", "font-family"]


def fonts_css() -> str:
    out = []
    for fam, prefix in (("Schibsted Grotesk", "schibsted-grotesk"), ("Instrument Sans", "instrument-sans")):
        for f in sorted(FONTS.glob(f"{prefix}-latin-*-normal.woff2")):
            w = f.name.split("-latin-")[1].split("-")[0]
            out.append(f"@font-face{{font-family:'{fam}';src:url('{f.as_uri()}') format('woff2');font-weight:{w};}}")
    return "".join(out)


def render(fragment: Path, out: Path) -> None:
    from playwright.sync_api import sync_playwright
    from PIL import Image
    inhalt = fragment.read_text(encoding="utf-8")
    for v in VERBOTEN:
        if v in inhalt:
            sys.exit(f"FEHLER: '{v}' ist im Schaubild nicht erlaubt (CI). Nur Klassen aus grafik_basis.css verwenden.")
    doc = (f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts_css()}{CSS.read_text()}</style>"
           f"</head><body>{inhalt}</body></html>")
    tmp = out.with_suffix(".tmp.html")
    tmp.write_text(doc, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 800, "height": 600}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        ueberlauf = pg.evaluate("""() => [...document.querySelectorAll('*')]
            .filter(e => e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).overflow !== 'visible').length""")
        pg.locator("body").screenshot(path=str(out))
        b.close()
    tmp.unlink()
    img = Image.open(out).convert("RGB").quantize(colors=48, method=Image.Quantize.MEDIANCUT)
    img.save(out, optimize=True)
    w, h = Image.open(out).size
    print(f"Schaubild: {out} ({w} × {h} px){' – WARNUNG: Text läuft über' if ueberlauf else ''}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fragment")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    render(Path(a.fragment), Path(a.out))
