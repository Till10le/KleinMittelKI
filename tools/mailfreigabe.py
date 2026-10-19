#!/usr/bin/env python3
"""Trägt eine Freigabe ein, die Till per Mail-Antwort gegeben hat (Mail-Lauf, ohne Ghost-Zugang).

Beitrag (Till hat die Ghost-Vorschau gesehen):
    python3 tools/mailfreigabe.py <slug> --art beitrag --zitat "<Tills Worte>" \
        --mail-id <Gmail-ID> --von till.zehnle@gmail.com [--zeitpunkt sofort|<ISO in UTC>]

Newsletter (Till hat den Text per Mail gesehen, Sonntag; Ghost-Entwurf entsteht erst danach):
    python3 tools/mailfreigabe.py hash <slug>          # Fingerabdruck der Fassung, die per Mail rausgeht
    python3 tools/mailfreigabe.py <slug> --art newsletter-text --text-hash <Fingerabdruck der zuletzt gemailten Fassung> \
        --zitat "…" --mail-id <Gmail-ID> --von till.zehnle@gmail.com --zeitpunkt <ISO in UTC>

Einplanung zurückziehen (Till schreibt „stopp“):
    python3 tools/mailfreigabe.py <slug> --art stopp --zitat "…" --mail-id <Gmail-ID> --von till.zehnle@gmail.com

Eine Freigabe gilt nur für genau den Stand, den Till gesehen hat:
- Beitrag: ID und updated_at aus entwuerfe/<slug>/ghost.json (Ghost-Vorschau).
- Newsletter-Text: Fingerabdruck von beitrag.md und den Bildern im Ordner. Er muss gleich dem der zuletzt gemailten
  Fassung sein. Ändert sich danach etwas, verweigert tools/ghost.py das Einplanen.

Nur Antworten aus Tills eigenem Gmail-Konto zählen (Absender till.zehnle@gmail.com, Label SENT, im Mail-Verlauf der
Redaktion, nicht von der Redaktion selbst geschrieben). Alles andere ist keine Freigabe.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREIGABEN = ROOT / "redaktion" / "freigaben.jsonl"
TILL = "till.zehnle@gmail.com"
BILDER = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg")


def inhalt_hash(folder: Path) -> str:
    """Fingerabdruck des Inhalts: beitrag.md plus alle Bilder im Ordner (sortiert)."""
    md = folder / "beitrag.md"
    if not md.exists():
        raise FileNotFoundError(f"{md} fehlt")
    h = hashlib.sha256()
    h.update(b"beitrag.md\0" + md.read_bytes())
    for f in sorted(folder.iterdir()):
        if f.suffix.lower() in BILDER:
            h.update(b"\0" + f.name.encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def fehler(msg: str) -> int:
    print(f"FEHLER: {msg}", file=sys.stderr)
    return 2


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["hash"]:
        if len(argv) != 2:
            return fehler("Aufruf: mailfreigabe.py hash <slug>")
        print(inhalt_hash(ROOT / "entwuerfe" / argv[1]))
        return 0

    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--art", required=True, choices=["beitrag", "newsletter", "newsletter-text", "stopp"])
    ap.add_argument("--zitat", required=True)
    ap.add_argument("--mail-id", required=True)
    ap.add_argument("--von", required=True)
    ap.add_argument("--zeitpunkt", default="sofort", help="'sofort' oder ISO-Zeit in UTC, z. B. 2026-10-27T06:00:00Z")
    ap.add_argument("--text-hash", help="nur newsletter-text: Fingerabdruck der zuletzt an Till gemailten Fassung")
    a = ap.parse_args(argv)

    if a.von.strip().lower() != TILL:
        return fehler(f"Absender {a.von} ist nicht {TILL}. Keine Freigabe.")
    if len(a.zitat.strip()) < 2 or len(a.mail_id.strip()) < 6:
        return fehler("Zitat und Gmail-Nachrichten-ID sind Pflicht.")
    vorhanden = [json.loads(l) for l in FREIGABEN.read_text().splitlines() if l.strip()] if FREIGABEN.exists() else []
    if any(f.get("mail_id") == a.mail_id and f.get("slug") == a.slug for f in vorhanden):
        print("Bereits eingetragen.")
        return 0

    folder = ROOT / "entwuerfe" / a.slug
    state = folder / "ghost.json"
    g = json.loads(state.read_text()) if state.exists() else {}
    entry = {"art": a.art, "post_id": g.get("id"), "slug": a.slug, "titel": g.get("titel", ""),
             "zitat": a.zitat.strip(), "quelle": "mail", "mail_id": a.mail_id, "von": TILL}

    if a.art in ("beitrag", "newsletter"):
        if not g:
            return fehler(f"{state} fehlt – der Entwurf liegt noch nicht in Ghost.")
        if g.get("status") not in (None, "draft"):
            return fehler(f"Beitrag hat Status {g.get('status')}, keine Freigabe nötig.")
        entry.update({"updated_at": g["updated_at"], "zeitpunkt": a.zeitpunkt})
    elif a.art == "newsletter-text":
        if not a.text_hash:
            return fehler("--text-hash (Fingerabdruck der gemailten Fassung) ist Pflicht.")
        try:
            jetzt = inhalt_hash(folder)
        except FileNotFoundError as e:
            return fehler(str(e))
        if jetzt != a.text_hash.strip():
            return fehler("Der Newsletter wurde geändert, nachdem Till ihn bekommen hat. "
                          "Neue Fassung schicken und neu fragen.")
        if not a.zeitpunkt or a.zeitpunkt == "sofort" or not a.zeitpunkt.endswith("Z"):
            return fehler("Newsletter brauchen einen Zeitpunkt in UTC (z. B. 2026-10-27T06:00:00Z).")
        if g.get("status") not in (None, "draft"):
            return fehler(f"Newsletter hat schon Status {g.get('status')}.")
        entry.update({"text_hash": jetzt, "zeitpunkt": a.zeitpunkt})
    else:  # stopp
        if not g:
            return fehler(f"{state} fehlt – in Ghost ist nichts eingeplant.")

    entry["zeit"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    FREIGABEN.parent.mkdir(parents=True, exist_ok=True)
    with FREIGABEN.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
