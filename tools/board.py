#!/usr/bin/env python3
"""Themenboard schlank halten (Till 02.11.2026: leere Läufe sollen wenig kosten).

Befehle:
    status          Kurzliste „slug  status“ aller Einträge unter „## Aktiv“ (statt das ganze Board zu lesen)
    zeige <slug>    Nur diesen einen Eintrag ausgeben
    kuerzen         Lange „Verlauf“-Zeilen kürzen: im Board bleiben die letzten 3 Einträge, ältere wandern
                    wörtlich nach redaktion/verlauf/<slug>.md (angehängt, nie gelöscht). Mehrfach aufrufbar.

Nur Python-Standardbibliothek.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "redaktion" / "themenboard.md"
VERLAUF = ROOT / "redaktion" / "verlauf"
BEHALTEN = 3
VERWEIS = "(ältere Einträge: redaktion/verlauf/{slug}.md)"
TRENNER = re.compile(r" · (?=\d{4}-\d{2}-\d{2}\b)")


def eintraege(text: str) -> list[tuple[str, str, int, int]]:
    """(slug, status, zeile_start, zeile_ende) für jeden ### -Eintrag nach „## Aktiv“ bis „## Archiv“ (inklusive)."""
    zeilen = text.split("\n")
    out, aktiv, cur = [], False, None
    for i, z in enumerate(zeilen):
        if z.startswith("## "):
            aktiv = z.strip() in ("## Aktiv", "## Archiv")
            if cur:
                out.append((*cur, i))
                cur = None
            continue
        if aktiv and z.startswith("### "):
            if cur:
                out.append((*cur, i))
            cur = [z[4:].split()[0], "", i]
        elif cur and z.startswith("- Status:") and not cur[1]:
            cur[1] = z.split(":", 1)[1].strip().strip("`")
    if cur:
        out.append((*cur, len(zeilen)))
    return [tuple(e) for e in out]


def cmd_status() -> int:
    text = BOARD.read_text(encoding="utf-8")
    for slug, status, *_ in eintraege(text):
        print(f"{slug}  {status}")
    return 0


def cmd_zeige(slug: str) -> int:
    text = BOARD.read_text(encoding="utf-8")
    zeilen = text.split("\n")
    for s, _st, a, e in eintraege(text):
        if s == slug:
            print("\n".join(zeilen[a:e]).rstrip())
            return 0
    print(f"{slug}: nicht im Board")
    return 1


def cmd_kuerzen() -> int:
    text = BOARD.read_text(encoding="utf-8")
    zeilen = text.split("\n")
    slug_von = {}
    for slug, _s, a, e in eintraege(text):
        for i in range(a, e):
            slug_von[i] = slug
    geaendert = []
    for i, z in enumerate(zeilen):
        if not z.startswith("- Verlauf:") or i not in slug_von:
            continue
        slug = slug_von[i]
        rumpf = z[len("- Verlauf:"):].strip()
        verweis = VERWEIS.format(slug=slug)
        if rumpf.startswith(verweis):
            rumpf = rumpf[len(verweis):].strip()
        teile = TRENNER.split(rumpf)
        if len(teile) <= BEHALTEN:
            continue
        alt, neu = teile[:-BEHALTEN], teile[-BEHALTEN:]
        VERLAUF.mkdir(parents=True, exist_ok=True)
        datei = VERLAUF / f"{slug}.md"
        kopf = "" if datei.exists() else f"# Verlauf {slug}\n\nÄltere Einträge aus dem Themenboard, wörtlich (nichts gelöscht).\n\n"
        with datei.open("a", encoding="utf-8") as f:
            f.write(kopf + "".join(f"- {t}\n" for t in alt))
        zeilen[i] = f"- Verlauf: {verweis} " + " · ".join(neu)
        geaendert.append(f"{slug}: {len(alt)} ältere Einträge → {datei.relative_to(ROOT)}")
    if geaendert:
        BOARD.write_text("\n".join(zeilen), encoding="utf-8")
    print("\n".join(geaendert) or "nichts zu kürzen")
    return 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["status"]:
        return cmd_status()
    if argv[:1] == ["zeige"] and len(argv) == 2:
        return cmd_zeige(argv[1])
    if argv[:1] == ["kuerzen"]:
        return cmd_kuerzen()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
