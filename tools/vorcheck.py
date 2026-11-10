#!/usr/bin/env python3
"""Vorab-Check des Redaktions-Laufs (Till 02.11.2026: leere Läufe sollen wenig kosten).

Entscheidet aus dem Repo-Stand, ob der Lauf voll arbeiten muss oder sofort enden kann. Liest nur, ändert nichts,
braucht kein Netz. Gmail und Ghost prüft der Lauf selbst (je ein Aufruf) und übergibt das Ergebnis:

    python3 tools/vorcheck.py --mail-ids <id,id,…> [--abarbeiten-leer] [--ghost-ok]

--mail-ids          IDs der neuesten Nachricht je Verlauf aus der Gmail-Suche (leer lassen, wenn keine Treffer)
--abarbeiten-leer   `ghost.py abarbeiten` meldete "ausgefuehrt": [] ohne Fehler
--ghost-ok          `ghost.py check` war ok

Ausgabe (JSON): {"lauf": "voll" | "pflege" | "leer", "gruende": [...]}
  voll   → docs/lauf.md ab Schritt 0.3 vollständig
  pflege → nur 7:47-Pflege (index, referenz), Commit nur bei Änderungen, keine Mail
  leer   → nichts zu tun: kein Commit, keine Mail, sofort beenden
Nur Python-Standardbibliothek.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import board  # noqa: E402

ARBEIT = {"freigegeben", "zurueck", "in-arbeit", "geprueft"}


def newsletter_offen(slug: str) -> str | None:
    folder = ROOT / "entwuerfe" / slug
    if not (folder / "beitrag.md").exists():
        return f"{slug}: newsletter-vorschlag ohne beitrag.md"
    state_file = folder / "ghost.json"
    if not state_file.exists():
        return f"{slug}: newsletter-vorschlag, ghost.json fehlt"
    from mailfreigabe import inhalt_hash
    if json.loads(state_file.read_text()).get("entwurf_hash") != inhalt_hash(folder):
        return f"{slug}: newsletter-vorschlag, entwurf_hash veraltet"
    return None


def letzter_status() -> str | None:
    """Status-Zeile des letzten Lauf-Abschnitts im neuesten Tagesbericht."""
    berichte = sorted(p for p in (ROOT / "redaktion" / "berichte").glob("20??-??-??.md"))
    if not berichte:
        return None
    text = berichte[-1].read_text(encoding="utf-8")
    teile = re.split(r"^## Lauf ", text, flags=re.M)
    if len(teile) < 2:
        return None
    m = re.search(r"^(?:Lauf [^\n]*?·\s*)?Status:\s*(.+)$", teile[-1], flags=re.M)
    return m.group(1).strip() if m else "keine Status-Zeile"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mail-ids", default="")
    ap.add_argument("--abarbeiten-leer", action="store_true")
    ap.add_argument("--ghost-ok", action="store_true")
    a = ap.parse_args(argv)

    gruende: list[str] = []
    jetzt = dt.datetime.now(ZoneInfo("Europe/Berlin"))
    morgens = jetzt.hour < 10  # Lauf 7:47

    # Teile, die nur zu bestimmten Zeiten laufen
    if morgens and jetzt.weekday() == 3:
        gruende.append("Donnerstag 7:47: Scout und Briefing")
    if morgens and jetzt.weekday() == 6:
        gruende.append("Sonntag 7:47: Sonntags-Teil")

    # Ghost
    if not a.ghost_ok:
        gruende.append("ghost.py check fehlgeschlagen (melden)")
    if not a.abarbeiten_leer:
        gruende.append("ghost.py abarbeiten hat etwas ausgeführt oder gemeldet (bestätigen)")

    # Post: neueste Nachricht je Verlauf, die die Redaktion weder geschickt noch verarbeitet hat
    mail = json.loads((ROOT / "redaktion" / "mail.json").read_text())
    bekannt = set(mail.get("eigene_ids", [])) | set(mail.get("verarbeitet", []))
    neu = [i for i in (x.strip() for x in a.mail_ids.split(",")) if i and i not in bekannt]
    if neu:
        gruende.append(f"neue Mail(s) von Till: {', '.join(neu)}")

    # Board
    for slug, status, *_ in board.eintraege(board.BOARD.read_text(encoding="utf-8")):
        if status in ARBEIT:
            gruende.append(f"{slug}: {status}")
        elif status == "newsletter-vorschlag":
            g = newsletter_offen(slug)
            if g:
                gruende.append(g)

    # Fehler im Vorlauf → dieser Lauf muss prüfen, ob er sich wiederholt
    st = letzter_status()
    if st and not st.startswith("Alles läuft"):
        gruende.append(f"Vorlauf meldete: {st}")

    # Uncommittete Reste eines abgebrochenen Laufs
    rest = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if rest:
        gruende.append("nicht committete Änderungen im Repo")

    lauf = "voll" if gruende else ("pflege" if morgens else "leer")
    print(json.dumps({"lauf": lauf, "zeit": jetzt.strftime("%a %H:%M"), "gruende": gruende}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
