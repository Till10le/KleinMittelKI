#!/usr/bin/env python3
"""Trägt eine Freigabe ein, die Till per Mail-Antwort gegeben hat (Mail-Lauf, ohne Ghost-Zugang).

    python3 tools/mailfreigabe.py <slug> --art beitrag|newsletter --zitat "<Tills Worte>" \
        --mail-id <Gmail-Nachrichten-ID> --von till.zehnle@gmail.com [--zeitpunkt sofort|<ISO in UTC>]

Die Freigabe gilt für genau den Stand, den Till in der Vorschau gesehen hat: ID und updated_at kommen aus
entwuerfe/<slug>/ghost.json (geschrieben vom Ghost-Lauf beim Anlegen des Entwurfs). Ändert sich der Beitrag danach,
verweigert tools/ghost.py publish die Veröffentlichung.

Nur Antworten aus Tills eigenem Gmail-Konto zählen (Absender till.zehnle@gmail.com, Label SENT, im Mail-Verlauf der
Redaktion, nicht von der Redaktion selbst geschrieben). Alles andere ist keine Freigabe.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREIGABEN = ROOT / "redaktion" / "freigaben.jsonl"
TILL = "till.zehnle@gmail.com"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--art", required=True, choices=["beitrag", "newsletter"])
    ap.add_argument("--zitat", required=True)
    ap.add_argument("--mail-id", required=True)
    ap.add_argument("--von", required=True)
    ap.add_argument("--zeitpunkt", default="sofort", help="'sofort' oder ISO-Zeit in UTC, z. B. 2026-10-27T06:00:00Z")
    a = ap.parse_args()

    if a.von.strip().lower() != TILL:
        print(f"FEHLER: Absender {a.von} ist nicht {TILL}. Keine Freigabe.", file=sys.stderr)
        return 2
    if len(a.zitat.strip()) < 2 or len(a.mail_id.strip()) < 6:
        print("FEHLER: Zitat und Gmail-Nachrichten-ID sind Pflicht.", file=sys.stderr)
        return 2
    state = ROOT / "entwuerfe" / a.slug / "ghost.json"
    if not state.exists():
        print(f"FEHLER: {state} fehlt – der Entwurf liegt noch nicht in Ghost.", file=sys.stderr)
        return 2
    g = json.loads(state.read_text())
    if g.get("status") not in (None, "draft"):
        print(f"FEHLER: Beitrag hat Status {g.get('status')}, keine Freigabe nötig.", file=sys.stderr)
        return 2
    vorhanden = [json.loads(l) for l in FREIGABEN.read_text().splitlines() if l.strip()] if FREIGABEN.exists() else []
    if any(f.get("mail_id") == a.mail_id for f in vorhanden):
        print("Bereits eingetragen.")
        return 0
    entry = {"art": a.art, "post_id": g["id"], "slug": a.slug, "titel": g.get("titel", ""),
             "updated_at": g["updated_at"], "zitat": a.zitat.strip(), "quelle": "mail",
             "mail_id": a.mail_id, "von": TILL, "zeitpunkt": a.zeitpunkt,
             "zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
    FREIGABEN.parent.mkdir(parents=True, exist_ok=True)
    with FREIGABEN.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
