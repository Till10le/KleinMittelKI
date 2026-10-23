#!/usr/bin/env python3
"""Titelbild (Beitragsbild oben im Beitrag und Kachel in der Beitragsübersicht) im CI von KLEIN. MITTEL. KI.

    python3 tools/titelbild.py entwuerfe/<slug>/titelbild.html --kategorie "Entwicklungen" \
        --satz "Was der Chatbot sagt, sagt rechtlich der Betrieb." --out entwuerfe/<slug>/titel-<slug>.jpg

Nachgebaut nach den veröffentlichten Titelbildern (z. B. titel-ki-wissensmanagement.jpg,
titel-azubis-ki-empfehlung-betrieb.jpg): heller Paper-Grund, oben links „EINORDNUNG“, in der Mitte ein kleines
Schaubild, darunter EIN Satz, unten eine Linie mit Wortmarke links und Kategorie rechts. 1600 × 1000 px (JPG).

WICHTIG: Das Titelbild zeigt NIE den Beitragstitel. Der Titel steht im Theme direkt darüber – eine Titel-Kachel
als Beitragsbild doppelt die Überschrift. Die Titel-Kachel (tools/vorschaubild.py) ist nur fürs Teilen (og_image).

Das Fragment enthält nur das Schaubild in der Mitte, gebaut aus diesen Klassen (sonst nichts):

  Stufen/Rangfolge   <div class="t-stapel">
                       <div class="t-zeile"><span class="t-nr t-nr--lime">1</span>
                         <span class="t-balken t-balken--dunkel" style="--w:560px">Selbst nachschlagen<em>KI-Wissensdatenbank</em></span></div>
                       <div class="t-zeile"><span class="t-nr">2</span><span class="t-balken" style="--w:460px">Callcenter<em>Support</em></span></div>
                     </div>
  Frage + Liste      <div class="t-frage">Welcher Betrieb bildet hier gut aus?</div>
                     <div class="t-karte"><div class="t-li"><b>1.</b><i style="--w:220px"></i><mark>Empfohlen</mark></div>
                       <div class="t-li"><b>2.</b><i style="--w:220px"></i></div></div>
  Chat               <div class="t-chat"><div class="t-frage t-frage--rechts">Sind eure Ärzte Fachärzte?</div>
                       <div class="t-antwort"><small>Chatbot</small>Ja, beide sind Fachärzte.<mark>Erfunden</mark></div></div>
  Vorher → Nachher   <div class="t-paar"><div class="t-box">Vorher<em>…</em></div><div class="t-pfeil">→</div>
                       <div class="t-box t-box--dunkel">Nachher<em>…</em></div></div>
  Große Zahl         <div class="t-zahl">20<em>Fragen</em></div>

Lime nur als Badge (<mark>), Nummernfeld (.t-nr--lime) oder Zahl auf Schwarz. Keine eigenen Farben oder Schriften.
"""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
WORTMARKE = ROOT / "assets" / "logo-v4" / "SVG" / "kmk-wordmark-light-transparent.svg"
INK, LIME, GRAU, PAPER, LINIE = "#111111", "#D7FF00", "#45453F", "#F4F3EE", "#E2E2DE"
VERBOTEN = ["linear-gradient", "radial-gradient", "box-shadow", "<script", "font-family", "<img", "g-titel",
            "<h1", "<h2"]

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:800px;height:500px;background:{PAPER};color:{INK};font-family:'Instrument Sans';font-weight:500;
-webkit-font-smoothing:antialiased;overflow:hidden}}
.t{{position:relative;width:800px;height:500px;background:{PAPER}}}
.t-kicker{{position:absolute;left:45px;top:58px;font:600 11px/1 'Instrument Sans';letter-spacing:2.6px;text-transform:uppercase}}
.t-mitte{{position:absolute;left:45px;right:45px;top:96px;bottom:84px;display:flex;flex-direction:column;
align-items:center;justify-content:center;gap:26px}}
.t-satz{{font:500 17px/1.3 'Instrument Sans';text-align:center;max-width:620px}}
.t-fuss{{position:absolute;left:45px;right:45px;bottom:30px;border-top:1.5px solid {INK};padding-top:18px;
display:flex;justify-content:space-between;align-items:center}}
.t-fuss img{{height:22px;margin:-5px 0 -5px -6px}}
.t-fuss span{{font:600 10px/1 'Instrument Sans';letter-spacing:2.4px;text-transform:uppercase;color:{GRAU}}}
/* Stufen */
.t-stapel{{display:flex;flex-direction:column;gap:10px}}
.t-zeile{{display:flex;gap:12px;align-items:stretch}}
.t-nr{{width:36px;min-height:36px;border:1.5px solid {INK};display:flex;align-items:center;justify-content:center;
font:600 13px/1 'Instrument Sans';background:#fff}}
.t-nr--lime{{background:{LIME};border-color:{LIME}}}
.t-balken{{width:var(--w,420px);min-height:46px;border:1.5px solid {INK};background:#fff;display:flex;align-items:center;
justify-content:space-between;gap:16px;padding:0 16px;font:600 17px/1.2 'Instrument Sans'}}
.t-balken em{{font:600 9.5px/1 'Instrument Sans';letter-spacing:1.6px;text-transform:uppercase;font-style:normal;color:{GRAU}}}
.t-balken--dunkel{{background:{INK};color:#fff;border-color:{INK}}}
.t-balken--dunkel em{{color:{LIME}}}
/* Frage, Liste, Chat */
.t-frage{{background:{INK};color:#fff;font:600 18px/1.25 'Instrument Sans';padding:14px 26px;max-width:460px}}
.t-karte{{background:#fff;border:1px solid {LINIE};padding:16px 22px;width:420px;display:flex;flex-direction:column;gap:14px}}
.t-li{{display:flex;align-items:center;gap:16px;min-height:22px}}
.t-li b{{font:600 12px/1 'Instrument Sans';width:14px}}
.t-li i{{display:block;height:6px;width:var(--w,180px);background:#D5D5CF}}
mark{{background:{LIME};color:{INK};font:600 10px/1 'Instrument Sans';letter-spacing:1.6px;text-transform:uppercase;
padding:6px 10px;margin-left:auto}}
.t-chat{{display:flex;flex-direction:column;gap:14px;width:520px}}
.t-frage--rechts{{align-self:flex-end}}
.t-antwort{{align-self:flex-start;background:#fff;border:1.5px solid {INK};padding:12px 18px 14px;max-width:440px;
font:600 18px/1.3 'Instrument Sans';display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px}}
.t-antwort small{{flex-basis:100%;font:600 9.5px/1 'Instrument Sans';letter-spacing:1.6px;text-transform:uppercase;color:{GRAU}}}
.t-antwort mark{{margin-left:0}}
/* Vorher → Nachher, Zahl */
.t-paar{{display:flex;align-items:stretch;gap:0}}
.t-box{{width:250px;border:1.5px solid {INK};background:#fff;padding:14px 18px;font:600 18px/1.2 'Instrument Sans';
display:flex;flex-direction:column;justify-content:center}}
.t-box em{{font:500 13px/1.3 'Instrument Sans';font-style:normal;color:{GRAU};margin-top:4px}}
.t-box--dunkel{{background:{INK};color:#fff}}
.t-box--dunkel em{{color:#cfcfc6}}
.t-pfeil{{width:46px;display:flex;align-items:center;justify-content:center;font:700 24px/1 'Schibsted Grotesk'}}
.t-zahl{{background:{INK};color:{LIME};font:800 64px/1 'Schibsted Grotesk';padding:14px 26px;display:flex;align-items:baseline;gap:12px}}
.t-zahl em{{font:600 14px/1 'Instrument Sans';font-style:normal;letter-spacing:1.6px;text-transform:uppercase;color:#fff}}
"""


def fonts_css() -> str:
    out = []
    for fam, prefix in (("Schibsted Grotesk", "schibsted-grotesk"), ("Instrument Sans", "instrument-sans")):
        for f in sorted(FONTS.glob(f"{prefix}-latin-*-normal.woff2")):
            w = f.name.split("-latin-")[1].split("-")[0]
            out.append(f"@font-face{{font-family:'{fam}';src:url('{f.as_uri()}') format('woff2');font-weight:{w};}}")
    return "".join(out)


def page(fragment: str, kategorie: str, satz: str, kicker: str) -> str:
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts_css()}{CSS}</style></head><body>"
            f"<div class='t'><div class='t-kicker'>{html.escape(kicker)}</div>"
            f"<div class='t-mitte'>{fragment}<p class='t-satz'>{html.escape(satz)}</p></div>"
            f"<div class='t-fuss'><img src='{WORTMARKE.as_uri()}' alt=''><span>{html.escape(kategorie)}</span></div>"
            f"</div></body></html>")


def render(fragment: Path, kategorie: str, satz: str, out: Path, kicker: str = "Einordnung",
           titel: str | None = None) -> None:
    from playwright.sync_api import sync_playwright
    inhalt = fragment.read_text(encoding="utf-8")
    for v in VERBOTEN:
        if v in inhalt:
            sys.exit(f"FEHLER: '{v}' ist im Titelbild nicht erlaubt. Nur die t-Klassen aus tools/titelbild.py.")
    if titel and titel.strip().lower()[:40] in (inhalt + satz).lower():
        sys.exit("FEHLER: Das Titelbild wiederholt den Beitragstitel. Es braucht ein Schaubild und einen eigenen Satz.")
    if len(satz) > 70:
        sys.exit(f"FEHLER: Satz zu lang ({len(satz)} Zeichen, höchstens 70). Ein kurzer Merksatz.")
    out = out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp.html")
    tmp.write_text(page(inhalt, kategorie, satz, kicker), encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 800, "height": 500}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        info = pg.evaluate("""() => { const m = document.querySelector('.t-mitte'), r = m.getBoundingClientRect();
            const kinder = [...m.querySelectorAll('*')].map(e => e.getBoundingClientRect());
            return {ueber: kinder.some(k => k.top < r.top - 1 || k.bottom > r.bottom + 1 || k.left < r.left - 1 || k.right > r.right + 1),
                    satzZeilen: Math.round(m.querySelector('.t-satz').getBoundingClientRect().height / (17 * 1.3))}; }""")
        pg.screenshot(path=str(out), type="jpeg", quality=90)
        b.close()
    tmp.unlink()
    if info["ueber"]:
        sys.exit(f"FEHLER: Schaubild passt nicht in die Mitte ({out}). Weniger Inhalt oder kürzere Texte.")
    if info["satzZeilen"] > 2:
        sys.exit("FEHLER: Satz bricht auf mehr als zwei Zeilen um. Kürzen.")
    print(f"Titelbild: {out} (1600 × 1000 px). Jetzt ansehen!")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fragment")
    ap.add_argument("--kategorie", required=True)
    ap.add_argument("--satz", required=True, help="ein Merksatz unter dem Schaubild, nicht der Titel")
    ap.add_argument("--out", required=True, help="entwuerfe/<slug>/titel-<slug>.jpg")
    ap.add_argument("--kicker", default="Einordnung")
    ap.add_argument("--titel", help="Beitragstitel – nur zur Prüfung, dass er nicht im Bild steht")
    a = ap.parse_args()
    render(Path(a.fragment), a.kategorie, a.satz, Path(a.out), a.kicker, a.titel)
