#!/usr/bin/env python3
"""Ghost-Werkzeug der KMK-Redaktion. Nur Python-Standardbibliothek.

Umgebung (Cloud-Umgebung „KMK-Ghost“):
    GHOST_URL            z. B. https://klein-mittel-ki.ghost.io
    GHOST_ADMIN_API_KEY  Admin API Key der Integration „KMK-Redaktion“ (Format id:secret)

Befehle:
    check                         Verbindung prüfen (nur lesen)
    list [--status S] [--limit N] Beiträge auflisten
    get <slug|id> [--raw]         Einen Beitrag lesen (--raw: alle Felder als JSON)
    upload <datei>                Bild hochladen, gibt die URL aus
    draft <entwurfsordner>        entwuerfe/<slug>/beitrag.md als ENTWURF anlegen oder aktualisieren
    index                         redaktion/blog-index.json und .md aus Ghost neu bauen
    freigabe <slug> --art beitrag|newsletter --zitat "…" [--quelle "…"]
                                  Tills Freigabe eintragen. NUR auf Tills ausdrückliche Anweisung im Chat –
                                  direkt oder wörtlich mit Zeitstempel weitergegeben von Head of KMI
                                  (dann --quelle "Head of KMI, Grok-Bot-Chat <Datum Uhrzeit>").
    kennzahlen                    Nur lesen (nur GET): Mitglieder, Newsletter-Abos, Öffnungs-/Klickrate je Versand,
                                  Beitragszahl. Gibt JSON aus, keine personenbezogenen Daten.
    publish <slug> [--zeitpunkt ISO]
                                  Veröffentlichen/einplanen. Nur mit gültiger Freigabe. Nie mit E-Mail-Versand.
    newsletter <slug> [--newsletter <newsletter-slug>] --zeitpunkt ISO
                                  Newsletter-Ausgabe einplanen. Nur mit gültiger Freigabe (art newsletter).
    referenz [--auch <slug> …]    Nur lesen: HTML aller veröffentlichten Beiträge nach redaktion/referenz/
    abarbeiten                    Alle offenen Freigaben ausführen (auch die per Mail von tools/mailfreigabe.py).
    testmail <newsletter-ordner>  Newsletter als Entwurf anlegen/aktualisieren (ohne INTERN) und Ghosts Testmail
                                  NUR an till.zehnle@gmail.com schicken. Plant nichts ein, verschickt nichts an Abonnenten.
    freigabe management/seo-paket.md --art seo --umfang T1-T9,L1-L6[,S1-S2] [--linkedin URL] --zitat "…" --quelle "…"
                                  Tills Freigabe für Punkte aus dem SEO-Paket (gebunden an den Inhalt dieser Punkte).
    seo [--ausfuehren | --live]   SEO-Paket umsetzen: nur Meta-Titel (T…), Links auf bestehende Ankertexte (L…) und
                                  LinkedIn/Website im Autorprofil (S…), nur freigegebene Punkte. Ohne Schalter Probe
                                  (nur lesen); --ausfuehren ändert und prüft danach live; --live prüft nur die Live-Seiten.

Es gibt bewusst keinen Löschbefehl.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import hmac
import json
import mimetypes
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import lexical  # noqa: E402
from mailfreigabe import inhalt_hash  # noqa: E402

FREIGABEN = ROOT / "redaktion" / "freigaben.jsonl"
INDEX_JSON = ROOT / "redaktion" / "blog-index.json"
INDEX_MD = ROOT / "redaktion" / "blog-index.md"
PUBLIC_SITE = "https://www.kleinmittelki.de"
TESTMAIL_AN = "till.zehnle@gmail.com"  # fest: Testmails gehen nie an eine andere Adresse
INTERN_PREFIX = "INTERN"


class GhostFehler(Exception):
    pass

# ---------- Verbindung ----------

def _ssl_context() -> ssl.SSLContext:
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    if not cafile and Path("/root/.ccr/ca-bundle.crt").exists():
        cafile = "/root/.ccr/ca-bundle.crt"
    return ssl.create_default_context(cafile=cafile) if cafile else ssl.create_default_context()


def _b64url(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def token() -> str:
    key = os.environ.get("GHOST_ADMIN_API_KEY", "")
    if ":" not in key:
        raise GhostFehler("GHOST_ADMIN_API_KEY fehlt oder hat nicht das Format id:secret. "
                          "Läuft die Sitzung in der Umgebung „KMK-Ghost“?")
    kid, secret = key.split(":", 1)
    now = int(time.time())
    header = _b64url(json.dumps({"alg": "HS256", "typ": "JWT", "kid": kid}, separators=(",", ":")).encode())
    payload = _b64url(json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}, separators=(",", ":")).encode())
    sig = hmac.new(bytes.fromhex(secret), f"{header}.{payload}".encode(), hashlib.sha256).digest()
    return f"{header}.{payload}.{_b64url(sig)}"


def base_url() -> str:
    url = os.environ.get("GHOST_URL", "").rstrip("/")
    if not url:
        raise GhostFehler("GHOST_URL fehlt. Läuft die Sitzung in der Umgebung „KMK-Ghost“?")
    return re.sub(r"/ghost$", "", url)


def api(method: str, path: str, query: dict | None = None, body: dict | None = None,
        raw: bytes | None = None, content_type: str | None = None) -> dict:
    url = f"{base_url()}/ghost/api/admin/{path.lstrip('/')}"
    if query:
        url += "?" + urllib.parse.urlencode({k: v for k, v in query.items() if v not in (None, "")})
    headers = {"Authorization": f"Ghost {token()}", "Accept-Version": "v5.0"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    elif raw is not None:
        data = raw
        headers["Content-Type"] = content_type or "application/octet-stream"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, context=_ssl_context(), timeout=60) as r:
            text = r.read().decode(errors="replace")
            if not text.strip():
                return {}
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                ziel = r.geturl()
                umgeleitet = f", umgeleitet nach {ziel}" if ziel != url else ""
                raise GhostFehler(f"Ghost antwortet {r.status} auf {method} {path} ohne JSON "
                                  f"(Content-Type {r.headers.get('Content-Type')}{umgeleitet}): {text[:300]}") from None
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        try:
            errs = json.loads(detail).get("errors", [])
            detail = "; ".join(f"{x.get('message')} {x.get('context') or ''}".strip() for x in errs) or detail
        except Exception:
            pass
        raise GhostFehler(f"Ghost antwortet {e.code} auf {method} {path}: {detail[:500]}") from None
    except urllib.error.URLError as e:
        raise GhostFehler(f"Ghost nicht erreichbar ({e.reason}). Ist die Domain in der Umgebung erlaubt?") from None

# ---------- Lesen ----------

def find_post(ref: str, formats: str = "lexical") -> dict:
    if re.fullmatch(r"[0-9a-f]{24}", ref):
        res = api("GET", f"posts/{ref}/", {"formats": formats, "include": "tags"})
    else:
        res = api("GET", f"posts/slug/{ref}/", {"formats": formats, "include": "tags"})
    return res["posts"][0]


def cmd_check(_a) -> None:
    site = api("GET", "site/")["site"]
    posts = api("GET", "posts/", {"limit": 1, "fields": "id,title,status"})
    total = posts.get("meta", {}).get("pagination", {}).get("total")
    print(json.dumps({"ok": True, "site": site.get("title"), "url": site.get("url"),
                      "beitraege_gesamt": total}, ensure_ascii=False, indent=2))


def cmd_list(a) -> None:
    q = {"limit": a.limit, "fields": "id,slug,title,status,published_at,updated_at", "include": "tags",
         "order": "updated_at desc"}
    if a.status != "all":
        q["filter"] = f"status:{a.status}"
    for p in api("GET", "posts/", q)["posts"]:
        tags = ", ".join(t["name"] for t in p.get("tags", []))
        print(f"{p['status']:<10} {str(p.get('published_at') or '')[:10]:<10} {p['slug']:<60} [{tags}]")


def cmd_get(a) -> None:
    p = find_post(a.ref, formats="lexical,html")
    if a.raw:
        print(json.dumps(p, ensure_ascii=False, indent=2))
        return
    print(json.dumps({k: p.get(k) for k in ["id", "uuid", "slug", "title", "status", "updated_at",
                                             "published_at", "custom_excerpt", "feature_image",
                                             "og_image", "url"]}
                     | {"tags": [t["name"] for t in p.get("tags", [])],
                        "zwischenueberschriften": lexical.headings_of(p["lexical"]) if p.get("lexical") else []},
                     ensure_ascii=False, indent=2))

# ---------- Bilder ----------

def upload(path: Path) -> str:
    if not path.exists():
        raise GhostFehler(f"Datei fehlt: {path}")
    boundary = uuid.uuid4().hex
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{path.name}\"\r\n"
            f"Content-Type: {mime}\r\n\r\n").encode() + path.read_bytes() + \
        (f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"purpose\"\r\n\r\nimage"
         f"\r\n--{boundary}--\r\n").encode()
    res = api("POST", "images/upload/", raw=body, content_type=f"multipart/form-data; boundary={boundary}")
    return res["images"][0]["url"]


def cmd_upload(a) -> None:
    print(upload(Path(a.datei)))

# ---------- Entwürfe ----------

def _lokale_bilder_hochladen(text: str, folder: Path, state: dict) -> str:
    """Ersetzt ![Alt](lokale-datei.png "…") durch die URL nach dem Upload (mit Cache in ghost.json)."""
    cache = state.setdefault("bilder", {})

    def repl(m):
        src = m.group("src")
        if src.startswith("http"):
            return m.group(0)
        path = (folder / src).resolve()
        if not path.exists():
            raise GhostFehler(f"Bild fehlt: {path}")
        h = hashlib.sha256(path.read_bytes()).hexdigest()
        if cache.get(src, {}).get("hash") != h:
            cache[src] = {"hash": h, "url": upload(path)}
        cap = f' "{m.group("cap")}"' if m.group("cap") is not None else ""
        return f'![{m.group("alt")}]({cache[src]["url"]}{cap})'

    return "\n".join(lexical.IMG.sub(repl, line.strip()) if lexical.IMG.match(line.strip()) else line
                     for line in text.split("\n"))


def _tags(meta: dict) -> list[dict]:
    names: list[str] = []
    if meta.get("kategorie"):
        names.append(meta["kategorie"])
    extra = meta.get("tags") or []
    names += extra if isinstance(extra, list) else [extra]
    if "#zur-freigabe" not in names:
        names.append("#zur-freigabe")
    seen, out = set(), []
    for n in names:
        if n and n not in seen:
            seen.add(n)
            out.append({"name": n})
    return out


def _titelbild_datei(folder: Path, meta: dict) -> Path | None:
    """Titelbild = Beitragsbild oben im Beitrag und Kachel in der Übersicht (tools/titelbild.py), NICHT die Titel-Kachel."""
    if str(meta.get("titelbild", "")).strip().lower() == "nein":
        return None
    name = meta.get("titelbild") or f"titel-{meta.get('slug') or folder.name}.jpg"
    bild = folder / name
    if not bild.exists():
        raise GhostFehler(f"Titelbild fehlt: {bild}. Mit tools/titelbild.py erzeugen (Einordnungs-Grafik, nicht der Titel). "
                          f"Ohne Titelbild nur mit 'titelbild: nein' im Frontmatter.")
    vorschau = folder / (meta.get("vorschaubild") or "vorschaubild.png")
    vorschau_jpg = vorschau.with_suffix(".jpg")
    h = hashlib.sha256(bild.read_bytes()).hexdigest()
    for v in (vorschau, vorschau_jpg):
        if v.exists() and hashlib.sha256(v.read_bytes()).hexdigest() == h:
            raise GhostFehler(f"{bild.name} ist die Titel-Kachel. Als Beitragsbild doppelt sie die Überschrift. "
                              f"Titelbild mit tools/titelbild.py bauen.")
    return bild


def _titelbild_hochladen(folder: Path, meta: dict, state: dict) -> str | None:
    bild = _titelbild_datei(folder, meta)
    if not bild:
        return None
    h = hashlib.sha256(bild.read_bytes()).hexdigest()
    if state.get("titelbild_hash") != h or not state.get("titelbild_url"):
        state["titelbild_url"] = upload(bild)
        state["titelbild_hash"] = h
    return state["titelbild_url"]


def cmd_draft(a) -> None:
    state = _draft(Path(a.ordner))
    print(json.dumps({k: state[k] for k in ("id", "status", "vorschau", "admin")}, ensure_ascii=False, indent=2))


def _draft(folder: Path) -> dict:
    md = folder / "beitrag.md"
    if not md.exists():
        raise GhostFehler(f"{md} fehlt")
    state_file = folder / "ghost.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    text = _lokale_bilder_hochladen(md.read_text(encoding="utf-8"), folder, state)
    meta, lex = lexical.build(text)
    newsletter = "#newsletter" in (meta.get("tags") or [])
    pflichtfelder = ("titel", "slug", "teaser") if newsletter else ("titel", "slug", "kategorie", "teaser")
    for pflicht in pflichtfelder:
        if not meta.get(pflicht):
            raise GhostFehler(f"Frontmatter-Feld fehlt: {pflicht}")
    post: dict = {"title": meta["titel"], "slug": meta["slug"], "lexical": lex,
                  "custom_excerpt": meta["teaser"], "tags": _tags(meta), "status": "draft"}
    if newsletter:
        post["email_subject"] = meta["titel"]
    if meta.get("meta_description"):
        post["meta_description"] = meta["meta_description"]
    if meta.get("fuer_kmu"):
        post["twitter_description"] = meta["fuer_kmu"]

    bild = folder / (meta.get("vorschaubild") or "vorschaubild.png")
    if bild.exists() and state.get("vorschaubild_hash") != hashlib.sha256(bild.read_bytes()).hexdigest():
        url = upload(bild)
        state["vorschaubild_url"] = url
        state["vorschaubild_hash"] = hashlib.sha256(bild.read_bytes()).hexdigest()
    if state.get("vorschaubild_url"):
        # Titel-Kachel nur zum Teilen (LinkedIn, WhatsApp …), nie als Beitragsbild: das Theme zeigt den Titel schon.
        post["og_image"] = post["twitter_image"] = state["vorschaubild_url"]
    if not newsletter:
        url = _titelbild_hochladen(folder, meta, state)
        if url:
            post["feature_image"] = url

    if state.get("id"):
        current = find_post(state["id"], formats="lexical")
        if current["status"] != "draft":
            raise GhostFehler(f"Beitrag ist bereits '{current['status']}'. Entwürfe dürfen nur Entwürfe überschreiben.")
        post["updated_at"] = current["updated_at"]
        res = api("PUT", f"posts/{state['id']}/", body={"posts": [post]})
    else:
        try:
            existing = find_post(meta["slug"])
        except GhostFehler:
            existing = None
        if existing and existing["status"] == "draft" and newsletter:
            # 01.11.2026 (Till freigegeben): Ein Lauf hatte den Newsletter-Entwurf angelegt, ghost.json aber nicht
            # committet (Testmail schlug fehl). Ohne Übernahme blockiert jeder weitere Lauf als „Dublette“.
            # Nur Newsletter-Entwürfe, nie veröffentlichte oder eingeplante Beiträge.
            print(f"Hinweis: Newsletter-Entwurf '{meta['slug']}' existiert schon (id {existing['id']}) – "
                  f"wird übernommen und aktualisiert.", file=sys.stderr)
            current = find_post(existing["id"], formats="lexical")
            post["updated_at"] = current["updated_at"]
            res = api("PUT", f"posts/{existing['id']}/", body={"posts": [post]})
        elif existing:
            raise GhostFehler(f"Es gibt schon einen Beitrag mit Slug '{meta['slug']}' ({existing['status']}). "
                              f"Dublette? Sonst Slug ändern oder ghost.json mit der id anlegen.")
        else:
            res = api("POST", "posts/", body={"posts": [post]})
    p = res["posts"][0]
    state.update({"id": p["id"], "uuid": p["uuid"], "slug": p["slug"], "titel": p["title"], "status": p["status"],
                  "updated_at": p["updated_at"], "vorschau": f"{PUBLIC_SITE}/p/{p['uuid']}/",
                  "admin": f"{base_url()}/ghost/#/editor/post/{p['id']}"})
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    return state

# ---------- Freigabe-Sperre ----------

def _freigaben() -> list[dict]:
    if not FREIGABEN.exists():
        return []
    return [json.loads(l) for l in FREIGABEN.read_text().splitlines() if l.strip()]


def cmd_freigabe(a) -> None:
    if len(a.zitat.strip()) < 3:
        raise GhostFehler("Ohne wörtliches Zitat von Tills Freigabe wird nichts eingetragen.")
    if a.art == "seo":
        return _seo_freigabe_eintragen(a)
    p = find_post(a.ref)
    entry = {"art": a.art, "post_id": p["id"], "slug": p["slug"], "titel": p["title"],
             "updated_at": p["updated_at"], "zitat": a.zitat.strip(),
             "quelle": (a.quelle or "Chat mit Till in dieser Claude-Sitzung").strip(),
             "zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
             "sitzung": os.environ.get("CLAUDE_CODE_REMOTE_SESSION_ID", "")}
    if a.art == "titelbild":
        # gebunden an die Bilddatei, die Till gesehen hat (nicht an den Textstand)
        folder = ROOT / "entwuerfe" / p["slug"]
        meta, _ = lexical.build((folder / "beitrag.md").read_text(encoding="utf-8"))
        bild = _titelbild_datei(folder, meta)
        if not bild:
            raise GhostFehler("Kein Titelbild im Entwurfsordner.")
        entry["datei_hash"] = hashlib.sha256(bild.read_bytes()).hexdigest()
    FREIGABEN.parent.mkdir(parents=True, exist_ok=True)
    with FREIGABEN.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps(entry, ensure_ascii=False, indent=2))


def _pruefe_freigabe(p: dict, art: str) -> dict:
    passend = [f for f in _freigaben() if f.get("post_id") == p["id"] and f["art"] == art]
    if not passend:
        raise GhostFehler(f"SPERRE: Keine Freigabe ({art}) für '{p['slug']}'. Erst Till fragen.")
    gueltig = [f for f in passend if f["updated_at"] == p["updated_at"]]
    if not gueltig:
        raise GhostFehler(f"SPERRE: Der Beitrag wurde nach Tills Freigabe geändert "
                          f"(freigegeben: {passend[-1]['updated_at']}, jetzt: {p['updated_at']}). Neu freigeben lassen.")
    return gueltig[-1]


def _ohne_intern(lex: str) -> tuple[str, int]:
    doc = json.loads(lex)
    kids = doc["root"]["children"]
    keep = []
    removed = 0
    for n in kids:
        txt = "".join(c.get("text", "") for c in n.get("children", []) if isinstance(c, dict))
        if n.get("type") == "paragraph" and txt.strip().startswith(INTERN_PREFIX):
            removed += 1
            continue
        keep.append(n)
    doc["root"]["children"] = keep
    return json.dumps(doc, ensure_ascii=False), removed


def _restliche_platzhalter(lex: str) -> list[str]:
    return sorted(set(re.findall(r"\[TILL:[^\]]*\]|\{\{[^}]*\}\}", lex)))


def _publish(p: dict, zeitpunkt: str | None) -> dict:
    _pruefe_freigabe(p, "beitrag")
    lex, removed = _ohne_intern(p["lexical"])
    rest = _restliche_platzhalter(lex)
    if rest:
        raise GhostFehler(f"SPERRE: Offene Platzhalter im Beitrag: {rest}")
    if p.get("feature_image") and p.get("feature_image") == p.get("og_image"):
        raise GhostFehler("SPERRE: Beitragsbild ist die Titel-Kachel (doppelte Überschrift). "
                          "Titelbild mit tools/titelbild.py bauen und Entwurf neu anlegen (ghost.py draft).")
    tags = [{"name": t["name"]} for t in p.get("tags", []) if t["name"] != "#zur-freigabe"]
    update = {"lexical": lex, "tags": tags, "updated_at": p["updated_at"]}
    if zeitpunkt and zeitpunkt != "sofort":
        update.update({"status": "scheduled", "published_at": zeitpunkt})
    else:
        update["status"] = "published"
    # Bewusst ohne newsletter-Parameter: Beiträge gehen nie per E-Mail raus.
    q = api("PUT", f"posts/{p['id']}/", body={"posts": [update]})["posts"][0]
    return {"slug": q["slug"], "status": q["status"], "url": q.get("url"),
            "published_at": q.get("published_at"), "intern_absaetze_entfernt": removed}


def _aktiver_newsletter() -> str:
    nls = api("GET", "newsletters/", {"filter": "status:active", "limit": "all"}).get("newsletters", [])
    if len(nls) != 1:
        raise GhostFehler(f"Es gibt {len(nls)} aktive Newsletter – bitte --newsletter angeben.")
    return nls[0]["slug"]


def _newsletter(p: dict, nl_slug: str | None, zeitpunkt: str, text_freigabe: dict | None = None) -> dict:
    if not zeitpunkt or zeitpunkt == "sofort":
        raise GhostFehler("Newsletter werden nur eingeplant: Zeitpunkt in UTC angeben (Dienstag 7:00 Uhr deutscher Zeit).")
    if text_freigabe is None:
        _pruefe_freigabe(p, "newsletter")
    # sonst: Freigabe des Mail-Texts; _newsletter_aus_text hat den Inhalt gegen den Hash geprüft
    # und den Entwurf eben selbst aus genau diesem Stand angelegt.
    lex, removed = _ohne_intern(p["lexical"])
    rest = _restliche_platzhalter(lex)
    if rest:
        raise GhostFehler(f"SPERRE: Offene Platzhalter: {rest}")
    tags = [{"name": t["name"]} for t in p.get("tags", []) if t["name"] != "#zur-freigabe"]
    update = {"lexical": lex, "tags": tags, "updated_at": p["updated_at"], "status": "scheduled",
              "published_at": zeitpunkt, "email_only": True}
    q = api("PUT", f"posts/{p['id']}/", body={"posts": [update]},
            query={"newsletter": nl_slug or _aktiver_newsletter(), "email_segment": "all"})["posts"][0]
    return {"slug": q["slug"], "status": q["status"], "published_at": q.get("published_at"),
            "intern_absaetze_entfernt": removed}


def cmd_publish(a) -> None:
    p = find_post(a.ref, formats="lexical")
    if p["status"] == "published":
        print("Bereits veröffentlicht.")
        return
    print(json.dumps(_publish(p, a.zeitpunkt), ensure_ascii=False, indent=2))


def cmd_newsletter(a) -> None:
    p = find_post(a.ref, formats="lexical")
    print(json.dumps(_newsletter(p, a.newsletter, a.zeitpunkt), ensure_ascii=False, indent=2))


def _newsletter_aus_text(f: dict) -> dict | None:
    """Till hat den Newsletter-Text per Mail freigegeben: Inhalt prüfen, Entwurf anlegen, einplanen."""
    folder = ROOT / "entwuerfe" / f["slug"]
    jetzt = inhalt_hash(folder)
    if jetzt != f.get("text_hash"):
        raise GhostFehler(f"SPERRE: Der Newsletter wurde nach Tills Freigabe geändert "
                          f"(freigegeben: {str(f.get('text_hash'))[:12]}, jetzt: {jetzt[:12]}). Neu freigeben lassen.")
    state_file = folder / "ghost.json"
    if state_file.exists():
        alt = json.loads(state_file.read_text())
        if alt.get("id"):
            cur = find_post(alt["id"], formats="lexical")
            if cur["status"] != "draft":
                return None  # schon eingeplant oder versendet
    state = _draft(folder)
    p = find_post(state["id"], formats="lexical")
    erg = _newsletter(p, None, f.get("zeitpunkt", ""), text_freigabe=f)
    erg["vorschau"] = state.get("vorschau")
    state.update({"status": erg["status"], "published_at": erg.get("published_at")})
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    return erg


def _zurueckziehen(f: dict) -> dict | None:
    """Till hat per Mail „stopp“ gesagt: eingeplanten Beitrag/Newsletter zurück auf Entwurf (nichts wird gelöscht)."""
    state_file = ROOT / "entwuerfe" / f["slug"] / "ghost.json"
    if not state_file.exists():
        return None
    p = find_post(json.loads(state_file.read_text())["id"], formats="lexical")
    if p["status"] == "draft":
        return None  # nichts eingeplant (oder schon zurückgezogen)
    if p["status"] != "scheduled":
        return {"slug": f["slug"], "status": p["status"], "hinweis": "stopp kam zu spät: bereits veröffentlicht/versendet"}
    q = api("PUT", f"posts/{p['id']}/", body={"posts": [{"status": "draft", "updated_at": p["updated_at"]}]})["posts"][0]
    return {"slug": q["slug"], "status": q["status"], "hinweis": "Einplanung zurückgezogen"}


def _titelbild_tauschen(f: dict) -> dict | None:
    """Till hat ein neues Titelbild für einen (auch veröffentlichten) Beitrag freigegeben: nur feature_image ändern."""
    folder = ROOT / "entwuerfe" / f["slug"]
    state_file = folder / "ghost.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    meta, _ = lexical.build((folder / "beitrag.md").read_text(encoding="utf-8"))
    bild = _titelbild_datei(folder, meta)
    if not bild:
        return None
    h = hashlib.sha256(bild.read_bytes()).hexdigest()
    if h != f.get("datei_hash"):
        raise GhostFehler(f"SPERRE: Titelbild wurde nach Tills Freigabe geändert ({bild.name}). Neu freigeben lassen.")
    p = find_post(f["post_id"], formats="lexical")
    if state.get("titelbild_hash") == h and p.get("feature_image") == state.get("titelbild_url"):
        return None  # schon getauscht
    url = _titelbild_hochladen(folder, meta, state)
    q = api("PUT", f"posts/{p['id']}/", body={"posts": [{"feature_image": url, "updated_at": p["updated_at"]}]})["posts"][0]
    state.update({"updated_at": q["updated_at"]})
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    return {"slug": q["slug"], "status": q["status"], "hinweis": f"Titelbild getauscht ({bild.name})"}


def cmd_abarbeiten(_a) -> None:
    """Führt die jeweils neueste Freigabe je Entwurf aus: veröffentlichen, einplanen, Newsletter aus Mail-Text, stopp."""
    ergebnisse = []
    gesehen = set()
    for f in reversed(_freigaben()):
        if f["art"] == "seo":
            continue  # SEO-Paket: nur über `ghost.py seo --ausfuehren`
        key = (f.get("slug") or f.get("post_id"), f["art"] == "titelbild")
        if key in gesehen:
            continue
        gesehen.add(key)
        try:
            if f["art"] == "titelbild":
                r = _titelbild_tauschen(f)
                if r:
                    ergebnisse.append(r)
                continue
            if f["art"] == "stopp":
                r = _zurueckziehen(f)
                if r:
                    ergebnisse.append(r)
                continue
            if f["art"] == "newsletter-text":
                r = _newsletter_aus_text(f)
                if r:
                    ergebnisse.append(r)
                continue
            p = find_post(f["post_id"], formats="lexical")
            if p["status"] != "draft":
                continue
            if f["art"] == "newsletter":
                ergebnisse.append(_newsletter(p, None, f.get("zeitpunkt", "")))
            else:
                ergebnisse.append(_publish(p, f.get("zeitpunkt")))
        except GhostFehler as e:
            ergebnisse.append({"slug": f.get("slug"), "fehler": str(e)})
    print(json.dumps({"ausgefuehrt": ergebnisse}, ensure_ascii=False, indent=2))

# ---------- Testmail (Till 25.10.2026: Newsletter vor der Freigabe so sehen, wie er ankommt) ----------

def cmd_testmail(a) -> None:
    folder = Path(a.ordner)
    meta, _ = lexical.build((folder / "beitrag.md").read_text(encoding="utf-8"))
    if "#newsletter" not in (meta.get("tags") or []):
        raise GhostFehler("Testmails nur für Newsletter. Beiträge gehen nie per E-Mail raus.")
    fingerabdruck = inhalt_hash(folder)
    state_file = folder / "ghost.json"
    vorher = json.loads(state_file.read_text()) if state_file.exists() else {}
    if vorher.get("id"):
        geplant = find_post(vorher["id"], formats="lexical")
        if geplant["status"] == "scheduled":
            # Till 27.10.2026: auch den schon eingeplanten Newsletter als Testmail sehen.
            # Nur lesen und Testmail auslösen – am eingeplanten Beitrag wird nichts geändert.
            lex, intern = _ohne_intern(geplant["lexical"])
            rest = _restliche_platzhalter(lex)
            if intern or rest:
                raise GhostFehler(f"SPERRE: Eingeplanter Newsletter enthält noch INTERN ({intern}) "
                                  f"oder Platzhalter {rest}. Keine Testmail, nichts geändert.")
            nl = _aktiver_newsletter()
            api("POST", f"email_previews/posts/{geplant['id']}/", query={"newsletter": nl},
                body={"emails": [TESTMAIL_AN], "newsletter": nl})
            vorher.update({"testmail_an": TESTMAIL_AN, "testmail_status": "scheduled",
                           "testmail_zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")})
            state_file.write_text(json.dumps(vorher, ensure_ascii=False, indent=2) + "\n")
            print(json.dumps({k: vorher.get(k) for k in ("slug", "status", "published_at", "testmail_an",
                                                          "testmail_zeit")}, ensure_ascii=False, indent=2))
            return
    state = _draft(folder)  # bricht ab, wenn der Newsletter in Ghost nicht mehr Entwurf ist
    p = find_post(state["id"], formats="lexical")
    lex, removed = _ohne_intern(p["lexical"])
    rest = _restliche_platzhalter(lex)
    if rest:
        raise GhostFehler(f"SPERRE: Offene Platzhalter: {rest}")
    if removed:
        p = api("PUT", f"posts/{p['id']}/", body={"posts": [{"lexical": lex, "updated_at": p["updated_at"]}]})["posts"][0]
    if p["status"] != "draft":
        raise GhostFehler(f"Newsletter ist '{p['status']}', keine Testmail.")
    # Till 02.11.2026: Die Testmail ist nur Zusatz. Der Entwurf in Ghost zählt; sein Stand wird vor dem
    # Testmail-Versuch festgehalten, damit der Begleitzettel auch ohne Testmail rausgehen kann.
    state.update({"updated_at": p["updated_at"], "entwurf_hash": fingerabdruck, "intern_absaetze_entfernt": removed})
    state.pop("testmail_fehler", None)
    (folder / "ghost.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    nl = _aktiver_newsletter()
    try:
        api("POST", f"email_previews/posts/{p['id']}/", query={"newsletter": nl},
            body={"emails": [TESTMAIL_AN], "newsletter": nl})
    except GhostFehler as e:
        state["testmail_fehler"] = str(e)[:500]
        (folder / "ghost.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        raise
    state.update({"testmail_hash": fingerabdruck, "testmail_an": TESTMAIL_AN,
                  "testmail_zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")})
    (folder / "ghost.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: state.get(k) for k in ("slug", "status", "vorschau", "entwurf_hash", "testmail_hash", "testmail_an",
                                                  "testmail_zeit")}, ensure_ascii=False, indent=2))

# ---------- Blog-Index ----------

SATZ_ENDE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"0-9])")
ZAHL = re.compile(r"\b\d[\d.,]*\s?(?:%|Prozent|Prozentpunkte|Mio\.|Millionen|Milliarden|Euro|€|×|-mal|mal so)")


def _zahlensaetze(text: str) -> list[str]:
    """Sätze mit belegten Zahlen (Prozent, Euro, Faktor …) – Tausenderpunkte trennen keine Sätze."""
    return [s.strip() for s in SATZ_ENDE.split(text) if ZAHL.search(s) and len(s) < 400]


def _plain(html: str) -> str:
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html or "", flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    for a_, b_ in (("&nbsp;", " "), ("&amp;", "&"), ("&quot;", '"'), ("&#x27;", "'"), ("&lt;", "<"), ("&gt;", ">")):
        t = t.replace(a_, b_)
    t = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), t)
    return re.sub(r"\s+", " ", t).strip()


def cmd_referenz(a) -> None:
    """Nur lesen: HTML und Metadaten aller veröffentlichten Beiträge nach redaktion/referenz/ (Vorbild für Aufbau und Grafiken)."""
    out = ROOT / "redaktion" / "referenz"
    out.mkdir(parents=True, exist_ok=True)
    posts = api("GET", "posts/", {"limit": "all", "formats": "html,lexical", "include": "tags",
                                  "filter": "status:[published,sent,scheduled]"})["posts"]
    for slug in a.auch or []:
        posts.append(find_post(slug, formats="html,lexical"))
    for p in posts:
        (out / f"{p['slug']}.html").write_text(p.get("html") or "", encoding="utf-8")
        meta = {k: p.get(k) for k in ("title", "slug", "status", "published_at", "custom_excerpt", "feature_image",
                                     "og_image", "twitter_description", "url", "email_only", "lexical")}
        meta["tags"] = [t["name"] for t in p.get("tags", [])]
        (out / f"{p['slug']}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(posts)} Beiträge nach {out} geschrieben")


def cmd_index(_a) -> None:
    posts = api("GET", "posts/", {"limit": "all", "formats": "html", "include": "tags",
                                  "order": "published_at desc"})["posts"]
    eintraege = []
    for p in posts:
        html = p.get("html") or ""
        links = re.findall(r'href="([^"]+)"', html)
        clean = sorted({re.sub(r"[?&]ref=kleinmittelki\.de", "", l) for l in links if l.startswith("http")})
        intern = [l for l in clean if "kleinmittelki.de" in l]
        quellen = [l for l in clean if "kleinmittelki.de" not in l]
        text = _plain(html)
        tags = [t["name"] for t in p.get("tags", [])]
        eintraege.append({
            "id": p["id"], "slug": p["slug"], "titel": p["title"], "status": p["status"],
            "veroeffentlicht": (p.get("published_at") or "")[:10], "geaendert": (p.get("updated_at") or "")[:10],
            "kategorie": next((t for t in tags if not t.startswith("#")), ""),
            "interne_tags": [t for t in tags if t.startswith("#")],
            "teaser": p.get("custom_excerpt") or "", "url": p.get("url"),
            "zwischenueberschriften": re.findall(r"<h2[^>]*>(.*?)</h2>", html),
            "quellen": quellen[:30], "interne_links": intern,
            "zahlen": _zahlensaetze(text)[:15],
            "woerter": len(text.split()),
        })
    INDEX_JSON.parent.mkdir(parents=True, exist_ok=True)
    stand = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    INDEX_JSON.write_text(json.dumps({"stand": stand, "anzahl": len(eintraege), "beitraege": eintraege},
                                     ensure_ascii=False, indent=2) + "\n")
    zeilen = [f"# Blog-Index\n\nStand: {stand} · {len(eintraege)} Beiträge (automatisch aus Ghost, nicht von Hand ändern)\n",
              "| Datum | Status | Kategorie | Titel | Quellen | Zahlen |", "|---|---|---|---|---|---|"]
    for e in eintraege:
        zeilen.append(f"| {e['veroeffentlicht'] or '–'} | {e['status']} | {e['kategorie']} | "
                      f"[{e['titel']}]({e['url']}) | {len(e['quellen'])} | {len(e['zahlen'])} |")
    INDEX_MD.write_text("\n".join(zeilen) + "\n")
    print(f"Index gebaut: {len(eintraege)} Beiträge -> {INDEX_JSON.relative_to(ROOT)}")

# ---------- Kennzahlen (nur lesen) ----------

def _anzahl(path: str, filt: str | None = None) -> int:
    """Nur GET: Gesamtzahl aus der Seitenangabe, ohne Datensätze auszugeben."""
    q = {"limit": 1, "fields": "id"}
    if filt:
        q["filter"] = filt
    return api("GET", path, q).get("meta", {}).get("pagination", {}).get("total", 0)


def _quote(teil: int | None, ganz: int | None) -> float | None:
    return round(100 * teil / ganz, 1) if teil is not None and ganz else None


def cmd_kennzahlen(_a) -> None:
    """Nur lesen (ausschließlich GET). Gibt nur Zahlen aus, keine Mitgliederdaten (keine Namen, keine Adressen)."""
    mitglieder = {"gesamt": _anzahl("members/"), "frei": _anzahl("members/", "status:free"),
                  "bezahlt": _anzahl("members/", "status:paid"), "geschenkt": _anzahl("members/", "status:comped")}
    newsletter = []
    for n in api("GET", "newsletters/", {"limit": "all", "include": "count.members,count.active_members,count.posts"})["newsletters"]:
        c = n.get("count") or {}
        newsletter.append({"slug": n["slug"], "name": n["name"], "status": n["status"],
                           "abos": c.get("members"), "abos_aktiv": c.get("active_members"), "ausgaben": c.get("posts")})
    versand = []
    for p in api("GET", "posts/", {"limit": "all", "filter": "status:[published,sent]", "formats": "mobiledoc",
                                   "include": "email,count.clicks", "order": "published_at desc"})["posts"]:
        e = p.get("email")
        if not e:
            continue
        zugestellt = e.get("delivered_count") or e.get("email_count")
        klicks = (p.get("count") or {}).get("clicks")
        versand.append({"datum": (e.get("submitted_at") or "")[:10], "slug": p["slug"], "titel": p["title"],
                        "empfaenger": e.get("email_count"), "zugestellt": e.get("delivered_count"),
                        "fehlgeschlagen": e.get("failed_count"), "geoeffnet": e.get("opened_count"),
                        "oeffnungsrate_prozent": _quote(e.get("opened_count"), zugestellt),
                        "klicker": klicks, "klickrate_prozent": _quote(klicks, zugestellt),
                        "oeffnungen_gemessen": e.get("track_opens"), "klicks_gemessen": e.get("track_clicks")})
    beitraege = {s_: _anzahl("posts/", f"status:{s_}") for s_ in ("published", "sent", "scheduled", "draft")}
    beitraege["gesamt"] = _anzahl("posts/")
    print(json.dumps({"stand": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                      "mitglieder": mitglieder, "newsletter": newsletter, "beitraege": beitraege,
                      "versand": versand,
                      "hinweis": "Öffnungsrate = geöffnet / zugestellt; Klickrate = Mitglieder mit mindestens einem Klick "
                                 "(Ghost count.clicks) / zugestellt. Öffnungen sind wegen Apple Mail Privacy Protection "
                                 "nur ein Näherungswert."},
                     ensure_ascii=False, indent=2))

# ---------- SEO-Paket (Till 22.11.2026 über Head of KMI: T1–T9 und L1–L6 umsetzen) ----------

SEO_PAKET = ROOT / "management" / "seo-paket.md"
TEXT_TYPEN = ("text", "extended-text")


def _seo_paket(pfad: Path = SEO_PAKET) -> dict:
    """Liest Meta-Titel (T…) und interne Links (L…) aus management/seo-paket.md."""
    titel, links, autor = {}, {}, {}
    gruppe = slug = None
    for zeile in pfad.read_text(encoding="utf-8").splitlines():
        m = re.match(r"###\s+(L\d+)\s+·\s+(\S+)", zeile)
        if m:
            gruppe, slug = m.group(1), m.group(2)
            continue
        if not zeile.startswith("| "):
            continue
        z = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if re.fullmatch(r"T\d+", z[0]) and len(z) == 6:
            titel[z[0]] = {"nr": z[0], "slug": z[1], "meta_title": z[4]}
        elif re.fullmatch(r"S\d+", z[0]) and len(z) == 4:
            autor[z[0]] = {"nr": z[0], "zeile": " | ".join(z[1:])}
        elif re.fullmatch(r"L\d+\.\d+", z[0]) and len(z) == 6 and gruppe and z[0].startswith(gruppe + "."):
            ziel = re.search(r"\]\((https://www\.kleinmittelki\.de/[^)\s]+)\)", z[4])
            if not ziel:
                raise GhostFehler(f"{z[0]}: Zielbeitrag ohne Link auf kleinmittelki.de")
            links[z[0]] = {"nr": z[0], "gruppe": gruppe, "slug": slug, "satz": z[2], "anker": z[3],
                           "url": ziel.group(1)}
    return {"titel": titel, "links": links, "autor": autor}


def _seo_umfang(text: str) -> list[str]:
    """„T1-T9,L1-L6“ → ['T1', …, 'T9', 'L1', …, 'L6'] (Gruppen, nicht Einzel-Links)."""
    out = []
    for teil in re.split(r"[,\s]+", text.replace("–", "-").strip()):
        if not teil:
            continue
        m = re.fullmatch(r"([TLS])(\d+)(?:-\1?(\d+))?", teil)
        if not m:
            raise GhostFehler(f"Umfang nicht lesbar: {teil!r} (erwartet z. B. T1-T9,L1-L6,S1-S2)")
        a, b = int(m.group(2)), int(m.group(3) or m.group(2))
        out += [f"{m.group(1)}{i}" for i in range(a, b + 1)]
    return out


def _seo_punkte(umfang: list[str], paket: dict) -> list[dict]:
    punkte = []
    for nr in umfang:
        if nr.startswith("T"):
            if nr not in paket["titel"]:
                raise GhostFehler(f"{nr} steht nicht in {SEO_PAKET.relative_to(ROOT)}")
            punkte.append({"art": "meta_title"} | paket["titel"][nr])
        elif nr.startswith("S"):
            if nr not in paket["autor"]:
                raise GhostFehler(f"{nr} steht nicht in {SEO_PAKET.relative_to(ROOT)}")
            punkte.append({"art": "autor", "slug": "author/till"} | paket["autor"][nr])
        else:
            teil = [l for l in paket["links"].values() if l["gruppe"] == nr]
            if not teil:
                raise GhostFehler(f"{nr} steht nicht in {SEO_PAKET.relative_to(ROOT)}")
            punkte += [{"art": "link"} | l for l in teil]
    return punkte


def _seo_hash(punkte: list[dict]) -> str:
    return hashlib.sha256(json.dumps(punkte, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def _seo_freigabe() -> dict:
    """Neueste Freigabe der Art seo; gilt nur, wenn die Punkte im Paket seitdem unverändert sind."""
    f = [x for x in _freigaben() if x.get("art") == "seo"]
    if not f:
        raise GhostFehler("SPERRE: Keine Freigabe (seo) für das SEO-Paket. Erst Till fragen.")
    f = f[-1]
    punkte = _seo_punkte(f["umfang"], _seo_paket())
    if _seo_hash(punkte) != f.get("paket_hash"):
        raise GhostFehler("SPERRE: Die freigegebenen Punkte in management/seo-paket.md wurden nach Tills Freigabe "
                          "geändert. Neu freigeben lassen.")
    return f | {"punkte": punkte}


def _text_von(n: dict) -> str:
    if n.get("type") in TEXT_TYPEN:
        return n.get("text", "")
    if n.get("type") == "linebreak":
        return "\n"
    return "".join(_text_von(c) for c in n.get("children", []) or [])


def _bloecke(n: dict):
    """Alle Knoten, deren Kinder Text tragen (Absatz, Überschrift, Listenpunkt, Zitat)."""
    kids = n.get("children", []) or []
    if any(c.get("type") in TEXT_TYPEN for c in kids):
        yield n
    for c in kids:
        yield from _bloecke(c)


def _link_setzen(doc: dict, l: dict) -> str:
    """Setzt einen Link auf den Ankertext im zitierten Satz. Text bleibt gleich. Gibt 'gesetzt' oder 'schon da' zurück."""
    treffer = [b for b in _bloecke(doc["root"]) if l["satz"] in _text_von(b)]
    if len(treffer) != 1:
        raise GhostFehler(f"{l['nr']}: Satz {len(treffer)}-mal gefunden (erwartet genau einmal): {l['satz'][:60]}…")
    block = treffer[0]
    voll = _text_von(block)
    if voll.count(l["satz"]) != 1:
        raise GhostFehler(f"{l['nr']}: Satz mehrfach im Absatz")
    if l["satz"].count(l["anker"]) != 1:
        raise GhostFehler(f"{l['nr']}: Ankertext nicht genau einmal im Satz")
    start = voll.index(l["satz"]) + l["satz"].index(l["anker"])
    ende = start + len(l["anker"])
    pos = 0
    kids = block["children"]
    for i, c in enumerate(kids):
        t = _text_von(c)
        if pos <= start and ende <= pos + len(t):
            if c.get("type") == "link":
                if c.get("url") == l["url"] and t == l["anker"]:
                    return "schon da"
                raise GhostFehler(f"{l['nr']}: Ankertext liegt schon in einem anderen Link ({c.get('url')})")
            if c.get("type") not in TEXT_TYPEN:
                raise GhostFehler(f"{l['nr']}: Ankertext liegt in einem Knoten vom Typ {c.get('type')}")
            a, b = start - pos, ende - pos
            neu = []
            if a > 0:
                neu.append(c | {"text": t[:a]})
            neu.append(lexical._link(l["url"], [c | {"text": t[a:b]}]))
            if b < len(t):
                neu.append(c | {"text": t[b:]})
            block["children"] = kids[:i] + neu + kids[i + 1:]
            return "gesetzt"
        pos += len(t)
    raise GhostFehler(f"{l['nr']}: Ankertext reicht über mehrere Formatierungen (z. B. fett/normal); nicht automatisch setzbar")


def _live(url: str) -> str:
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}seo-check={int(time.time())}", headers={"User-Agent": "KMK-Redaktion-Check"})
    with urllib.request.urlopen(req, context=_ssl_context(), timeout=60) as r:
        return r.read().decode(errors="replace")


def _nur_text(html: str | None) -> str:
    """Sichtbarer Text ohne Tags; anders als _plain ohne Leerzeichen an Tag-Grenzen (Link vor Satzzeichen)."""
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html or "", flags=re.S)
    return __import__("html").unescape(re.sub(r"<[^>]+>", "", t))


def _linkedin_name(url: str) -> str:
    m = re.fullmatch(r"https://(?:[a-z]{2,3}\.)?linkedin\.com/in/([A-Za-z0-9\-_%]+)/?", (url or "").strip())
    if not m:
        raise GhostFehler(f"LinkedIn-URL nicht erkannt: {url!r} (erwartet https://de.linkedin.com/in/<name>)")
    return m.group(1)


def _same_as(html: str) -> list[str]:
    """sameAs des Autors aus dem Article-JSON-LD einer Beitragsseite."""
    out = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(block)
        except json.JSONDecodeError:
            continue
        for x in d if isinstance(d, list) else [d]:
            autor = x.get("author") if isinstance(x, dict) else None
            for a_ in autor if isinstance(autor, list) else [autor]:
                if isinstance(a_, dict):
                    out += a_.get("sameAs") or []
    return out


def _seo_live_pruefen(punkte: list[dict], linkedin: str | None = None) -> list[dict]:
    """Nur lesen: öffentliche Seiten abrufen, <title>, Links und sameAs im Quelltext prüfen."""
    erg, cache = [], {}

    def seite(url: str) -> str:
        if url not in cache:
            cache[url] = _live(url)
        return cache[url]

    for pk in punkte:
        url = f"{PUBLIC_SITE}/{pk['slug']}/"
        try:
            if pk["art"] == "autor":
                if pk["nr"] != "S2":
                    continue  # S1 (Eintrag) wird über S2 (sameAs) live geprüft
                beispiel = next((x["slug"] for x in punkte if x["art"] != "autor"), "nicht-jedes-problem-braucht-ki")
                sa = _same_as(seite(f"{PUBLIC_SITE}/{beispiel}/"))
                name = _linkedin_name(linkedin) if linkedin else None
                ok = bool(name) and any(f"linkedin.com/in/{name}" in x for x in sa)
                erg.append({"nr": "S1/S2", "slug": beispiel, "live": "ok" if ok else "FEHLT", "sameAs": sa})
                continue
            html = seite(url)
        except Exception as e:  # noqa: BLE001
            erg.append({"nr": pk["nr"], "slug": pk["slug"], "live": "FEHLER", "grund": str(e)[:200]})
            continue
        if pk["art"] == "meta_title":
            m = re.search(r"<title>(.*?)</title>", html, re.S)
            ist = _plain(m.group(1)) if m else None
            erg.append({"nr": pk["nr"], "slug": pk["slug"], "live": "ok" if ist == pk["meta_title"] else "ABWEICHUNG",
                        "title_tag": ist})
        else:
            ok = any(_plain(x) == pk["anker"] for x in
                     re.findall(r'<a [^>]*href="' + re.escape(pk["url"]) + r'"[^>]*>(.*?)</a>', html, re.S))
            erg.append({"nr": pk["nr"], "slug": pk["slug"], "live": "ok" if ok else "FEHLT",
                        "anker": pk["anker"], "ziel": pk["url"]})
    return erg


def _seo_beitraege(punkte: list[dict], ausfuehren: bool, fehler: list[str]) -> list[dict]:
    """T… und L…: je Beitrag ein PUT, nur meta_title und lexical (Links); Text bleibt gleich."""
    je_beitrag: dict[str, list[dict]] = {}
    for pk in punkte:
        if pk["art"] != "autor":
            je_beitrag.setdefault(pk["slug"], []).append(pk)
    ergebnisse = []
    for slug, pks in je_beitrag.items():
        try:
            p = find_post(slug, formats="lexical,html")
            if p["status"] != "published":
                raise GhostFehler(f"{slug}: Status {p['status']}, nur veröffentlichte Beiträge")
            doc = json.loads(p["lexical"])
            update, schritte = {}, []
            for pk in pks:
                if pk["art"] == "meta_title":
                    if len(pk["meta_title"]) > 60:
                        raise GhostFehler(f"{pk['nr']}: Meta-Titel über 60 Zeichen")
                    if p.get("meta_title") == pk["meta_title"]:
                        schritte.append({"nr": pk["nr"], "ergebnis": "schon da"})
                    else:
                        update["meta_title"] = pk["meta_title"]
                        schritte.append({"nr": pk["nr"], "ergebnis": "setzen", "vorher": p.get("meta_title"),
                                         "nachher": pk["meta_title"]})
                else:
                    r = _link_setzen(doc, pk)
                    schritte.append({"nr": pk["nr"], "ergebnis": "setzen" if r == "gesetzt" else r,
                                     "anker": pk["anker"], "ziel": pk["url"]})
                    if r == "gesetzt":
                        update["lexical"] = json.dumps(doc, ensure_ascii=False)
            eintrag = {"slug": slug, "schritte": schritte}
            if update and ausfuehren:
                vorher_text = _nur_text(p.get("html"))
                update["updated_at"] = p["updated_at"]
                q = api("PUT", f"posts/{p['id']}/", body={"posts": [update]}, query={"formats": "html"})["posts"][0]
                eintrag.update({"geaendert": sorted(k for k in update if k != "updated_at"),
                                "updated_at": q["updated_at"], "status": q["status"],
                                "text_unveraendert": _nur_text(q.get("html")) == vorher_text})
                if not eintrag["text_unveraendert"]:
                    fehler.append(f"{slug}: Beitragstext weicht nach dem Setzen der Links ab – von Hand prüfen")
            elif update:
                eintrag["probe"] = "würde ändern: " + ", ".join(sorted(update))
            ergebnisse.append(eintrag)
        except GhostFehler as e:
            fehler.append(str(e))
    return ergebnisse


def _seo_autor(punkte: list[dict], linkedin: str | None, ausfuehren: bool, fehler: list[str]) -> dict | None:
    """S1: Feld LinkedIn im Autorprofil „till“. S2: sameAs prüfen; fehlt es, dieselbe URL ins Feld Website."""
    nrs = {pk["nr"] for pk in punkte if pk["art"] == "autor"}
    if not nrs:
        return None
    if not linkedin:
        fehler.append("S1/S2 freigegeben, aber keine LinkedIn-URL in der Freigabe")
        return None
    name = _linkedin_name(linkedin)
    u = api("GET", "users/slug/till/")["users"][0]
    erg = {"autor": "till", "linkedin_vorher": u.get("linkedin"), "website_vorher": u.get("website")}
    try:
        if "S1" in nrs and u.get("linkedin") != name:
            erg["S1"] = f"setzen: linkedin = {name}"
            if ausfuehren:
                u = api("PUT", f"users/{u['id']}/", body={"users": [{"linkedin": name}]})["users"][0]
                erg["linkedin_nachher"] = u.get("linkedin")
        elif "S1" in nrs:
            erg["S1"] = "schon da"
        if "S2" in nrs and ausfuehren:
            time.sleep(5)
            beispiel = next((pk["slug"] for pk in punkte if pk["art"] != "autor"), "nicht-jedes-problem-braucht-ki")
            sa = _same_as(_live(f"{PUBLIC_SITE}/{beispiel}/"))
            erg["sameAs_nach_S1"] = sa
            if any(f"linkedin.com/in/{name}" in x for x in sa):
                erg["S2"] = "sameAs enthält LinkedIn, Website nicht nötig"
            elif u.get("website") and u.get("website") != linkedin:
                fehler.append(f"S2: sameAs ohne LinkedIn, Feld Website ist schon belegt ({u.get('website')}) – nicht überschrieben")
            else:
                u = api("PUT", f"users/{u['id']}/", body={"users": [{"website": linkedin}]})["users"][0]
                erg["S2"] = f"sameAs ohne LinkedIn → Website = {linkedin}"
                erg["website_nachher"] = u.get("website")
    except GhostFehler as e:
        hinweis = (" – der Admin-Schlüssel der Integration darf das Autorprofil nicht ändern. Till trägt es in Ghost ein "
                   "(Einstellungen → Staff → Till Zehnle → LinkedIn), danach `ghost.py seo --live`.") if " 403 " in str(e) else ""
        fehler.append(f"Autorprofil: {e}{hinweis}")
    return erg


def cmd_seo(a) -> None:
    """SEO-Paket: Probe (nur lesen), --ausfuehren (nur freigegebene Punkte) oder --live (Gegenprobe, nur lesen)."""
    f = _seo_freigabe()
    punkte = f["punkte"]
    if a.live:
        print(json.dumps({"live": _seo_live_pruefen(punkte, f.get("linkedin"))}, ensure_ascii=False, indent=2))
        return
    fehler: list[str] = []
    out = {"freigabe": {"zitat": f["zitat"], "quelle": f["quelle"], "umfang": f["umfang"]},
           "modus": "ausgeführt" if a.ausfuehren else "Probe (nichts geändert)",
           "beitraege": _seo_beitraege(punkte, a.ausfuehren, fehler),
           "autorprofil": _seo_autor(punkte, f.get("linkedin"), a.ausfuehren, fehler)}
    if a.ausfuehren:
        time.sleep(5)
        out["live"] = _seo_live_pruefen(punkte, f.get("linkedin"))
    out["fehler"] = fehler
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if fehler:
        raise GhostFehler(f"{len(fehler)} Fehler, siehe oben")


def _seo_freigabe_eintragen(a) -> None:
    pfad = (ROOT / a.ref).resolve() if not Path(a.ref).is_absolute() else Path(a.ref)
    if pfad != SEO_PAKET.resolve():
        raise GhostFehler(f"SEO-Freigaben nur für {SEO_PAKET.relative_to(ROOT)}")
    if not a.umfang:
        raise GhostFehler("--umfang fehlt (z. B. T1-T9,L1-L6)")
    umfang = _seo_umfang(a.umfang)
    punkte = _seo_punkte(umfang, _seo_paket())
    if any(x.startswith("S") for x in umfang):
        _linkedin_name(a.linkedin or "")
    entry = {"art": "seo", "paket": str(SEO_PAKET.relative_to(ROOT)), "umfang": umfang,
             "punkte_anzahl": len(punkte), "paket_hash": _seo_hash(punkte), "zitat": a.zitat.strip(),
             "quelle": (a.quelle or "Chat mit Till in dieser Claude-Sitzung").strip(),
             "zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
             "sitzung": os.environ.get("CLAUDE_CODE_REMOTE_SESSION_ID", "")}
    if a.linkedin:
        entry["linkedin"] = a.linkedin.strip()
    with FREIGABEN.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps(entry, ensure_ascii=False, indent=2))

# ---------- CLI ----------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    s = sub.add_parser("list"); s.add_argument("--status", default="all", choices=["all", "draft", "published", "scheduled"])
    s.add_argument("--limit", default=30); s.set_defaults(fn=cmd_list)
    s = sub.add_parser("get"); s.add_argument("ref"); s.add_argument("--raw", action="store_true"); s.set_defaults(fn=cmd_get)
    s = sub.add_parser("upload"); s.add_argument("datei"); s.set_defaults(fn=cmd_upload)
    s = sub.add_parser("draft"); s.add_argument("ordner"); s.set_defaults(fn=cmd_draft)
    sub.add_parser("index").set_defaults(fn=cmd_index)
    s = sub.add_parser("referenz"); s.add_argument("--auch", nargs="*", help="zusätzliche Slugs (z. B. Vorlagen-Entwürfe)")
    s.set_defaults(fn=cmd_referenz)
    s = sub.add_parser("freigabe"); s.add_argument("ref")
    s.add_argument("--art", required=True, choices=["beitrag", "newsletter", "titelbild", "seo"])
    s.add_argument("--umfang", help="nur --art seo: Punkte aus management/seo-paket.md, z. B. T1-T9,L1-L6,S1-S2")
    s.add_argument("--linkedin", help="nur --art seo mit S1/S2: Tills LinkedIn-URL, wie er sie geschickt hat")
    s.add_argument("--zitat", required=True)
    s.add_argument("--quelle", help='Woher die Freigabe stammt, z. B. "Head of KMI, Grok-Bot-Chat 20.11.2026 18:08"')
    s.set_defaults(fn=cmd_freigabe)
    s = sub.add_parser("publish"); s.add_argument("ref"); s.add_argument("--zeitpunkt"); s.set_defaults(fn=cmd_publish)
    s = sub.add_parser("newsletter"); s.add_argument("ref"); s.add_argument("--newsletter")
    s.add_argument("--zeitpunkt", required=True); s.set_defaults(fn=cmd_newsletter)
    sub.add_parser("abarbeiten").set_defaults(fn=cmd_abarbeiten)
    s = sub.add_parser("testmail"); s.add_argument("ordner"); s.set_defaults(fn=cmd_testmail)
    sub.add_parser("kennzahlen").set_defaults(fn=cmd_kennzahlen)
    s = sub.add_parser("seo"); g_ = s.add_mutually_exclusive_group()
    g_.add_argument("--ausfuehren", action="store_true", help="freigegebene Punkte in Ghost umsetzen, danach live prüfen")
    g_.add_argument("--live", action="store_true", help="nur lesen: Live-Seiten gegenprüfen")
    s.set_defaults(fn=cmd_seo)
    a = ap.parse_args(argv)
    try:
        a.fn(a)
    except GhostFehler as e:
        print(f"FEHLER: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
