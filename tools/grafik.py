#!/usr/bin/env python3
"""Rendert ein Erklär-Schaubild (HTML-Fragment mit Klassen aus grafik_basis.css) als PNG im CI.

    python3 tools/grafik.py entwuerfe/<slug>/g1.html --out entwuerfe/<slug>/kmk-<thema>-g1.png

Das Fragment enthält nur den Inhalt im Karten-System der veröffentlichten Schaubilder, z. B.:

    <div class="g">
      <div class="g-kicker">Woher die Unterschiede kommen</div>
      <h1 class="g-titel">Vier Stufen, vier Mal eigene Entscheidungen</h1>
      <div class="g-stufen">
        <div class="g-stufe"><div class="g-nr">01</div>
          <div><h3>Daten</h3><p><b>Womit lernt das Modell?</b> Die Mischung prägt, was es kann.</p></div></div>
      </div>
      <div class="g-fuss"><span>Vereinfachte Darstellung · Quelle: …</span><b>kleinmittelki.de</b></div>
    </div>

Pflicht: .g-kicker, .g-titel, .g-fuss (mit „kleinmittelki.de“). Die Lime-Kante unten setzt das Skript selbst.
Bausteine und Beispiele: tools/grafik_basis.css und Skill kmk-ci-grafik.
Mit --social zusätzlich eine Hochformat-Kachel 1080 × 1350 (<name>-social.png) für LinkedIn/Instagram.
Ausgabe: 1600 px breit (doppelte Auflösung), auf 48 Farben reduziert. Danach das PNG ansehen!
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
CSS = ROOT / "tools" / "grafik_basis.css"

# Hochformat 4:5 für LinkedIn/Instagram: dieselbe Karte, 800 × 1000 CSS-px, Fußzeile unten → 1080 × 1350 px
SOCIAL_CSS = (".g{min-height:1000px;display:flex;flex-direction:column}.g-kicker{align-self:flex-start}"
              ".g-titel{font-size:46px}.g-titel+*{margin-top:auto}.g-fuss{margin-top:auto}")

VERBOTEN = ["linear-gradient", "radial-gradient", "box-shadow", "<script", "font-family"]


def fonts_css() -> str:
    out = []
    for fam, prefix in (("Schibsted Grotesk", "schibsted-grotesk"), ("Instrument Sans", "instrument-sans")):
        for f in sorted(FONTS.glob(f"{prefix}-latin-*-normal.woff2")):
            w = f.name.split("-latin-")[1].split("-")[0]
            out.append(f"@font-face{{font-family:'{fam}';src:url('{f.as_uri()}') format('woff2');font-weight:{w};}}")
    return "".join(out)


def render(fragment: Path, out: Path, social: bool = False) -> None:
    from playwright.sync_api import sync_playwright
    from PIL import Image
    inhalt = fragment.read_text(encoding="utf-8")
    for pflicht, name in (('class="g"', "Rahmen .g"), ("g-kicker", "Kicker"), ("g-titel", "Titel"), ("g-fuss", "Fußzeile")):
        if pflicht not in inhalt:
            sys.exit(f"FEHLER: {name} fehlt. Jede Grafik hat Kicker, Titel und Fußzeile (Skill kmk-ci-grafik).")
    if "kleinmittelki.de" not in inhalt:
        sys.exit("FEHLER: Die Fußzeile braucht rechts <b>kleinmittelki.de</b>.")
    if "g-kante" not in inhalt:
        k = inhalt.rfind("</div>")
        inhalt = inhalt[:k] + '<div class="g-kante"></div>' + inhalt[k:]
    for v in VERBOTEN:
        if v in inhalt:
            sys.exit(f"FEHLER: '{v}' ist im Schaubild nicht erlaubt (CI). Nur Klassen aus grafik_basis.css verwenden.")
    extra = SOCIAL_CSS if social else ""
    doc = (f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts_css()}{CSS.read_text()}{extra}</style>"
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
        pg.locator(".g").first.screenshot(path=str(out))
        b.close()
    tmp.unlink()
    img = Image.open(out).convert("RGB")
    if social:
        if img.height > 2000:
            print("WARNUNG: Für die Social-Kachel zu viel Inhalt (höher als 4:5) – Text kürzen oder Kachel weglassen.")
        img = img.resize((1080, round(img.height * 1080 / img.width)), Image.LANCZOS)
    img = img.quantize(colors=48, method=Image.Quantize.MEDIANCUT)
    img.save(out, optimize=True)
    w, h = Image.open(out).size
    print(f"Schaubild: {out} ({w} × {h} px){' – WARNUNG: Text läuft über' if ueberlauf else ''}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fragment")
    ap.add_argument("--out", required=True)
    ap.add_argument("--social", action="store_true",
                    help="zusätzlich <name>-social.png im Hochformat 1080 × 1350 für LinkedIn/Instagram")
    a = ap.parse_args()
    render(Path(a.fragment), Path(a.out))
    if a.social:
        out = Path(a.out)
        render(Path(a.fragment), out.with_name(out.stem + "-social.png"), social=True)
