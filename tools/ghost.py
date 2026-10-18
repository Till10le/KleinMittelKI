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
    freigabe <slug> --art beitrag|newsletter --zitat "…"
                                  Tills Freigabe eintragen. NUR auf Tills ausdrückliche Anweisung im Chat.
    publish <slug> [--zeitpunkt ISO]
                                  Veröffentlichen/einplanen. Nur mit gültiger Freigabe. Nie mit E-Mail-Versand.
    newsletter <slug> --newsletter <newsletter-slug> --zeitpunkt ISO
                                  Newsletter-Ausgabe einplanen. Nur mit gültiger Freigabe (art newsletter).

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

FREIGABEN = ROOT / "redaktion" / "freigaben.jsonl"
INDEX_JSON = ROOT / "redaktion" / "blog-index.json"
INDEX_MD = ROOT / "redaktion" / "blog-index.md"
PUBLIC_SITE = "https://www.kleinmittelki.de"
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
            text = r.read().decode()
            return json.loads(text) if text else {}
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


def cmd_draft(a) -> None:
    folder = Path(a.ordner)
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

    bild = folder / (meta.get("vorschaubild") or "vorschaubild.png")
    if bild.exists() and state.get("vorschaubild_hash") != hashlib.sha256(bild.read_bytes()).hexdigest():
        url = upload(bild)
        state["vorschaubild_url"] = url
        state["vorschaubild_hash"] = hashlib.sha256(bild.read_bytes()).hexdigest()
    if state.get("vorschaubild_url"):
        post["og_image"] = post["twitter_image"] = state["vorschaubild_url"]
        if meta.get("titelbild", "ja") != "nein":
            post["feature_image"] = state["vorschaubild_url"]

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
        if existing:
            raise GhostFehler(f"Es gibt schon einen Beitrag mit Slug '{meta['slug']}' ({existing['status']}). "
                              f"Dublette? Sonst Slug ändern oder ghost.json mit der id anlegen.")
        res = api("POST", "posts/", body={"posts": [post]})
    p = res["posts"][0]
    state.update({"id": p["id"], "uuid": p["uuid"], "slug": p["slug"], "status": p["status"],
                  "updated_at": p["updated_at"], "vorschau": f"{PUBLIC_SITE}/p/{p['uuid']}/",
                  "admin": f"{base_url()}/ghost/#/editor/post/{p['id']}"})
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: state[k] for k in ("id", "status", "vorschau", "admin")}, ensure_ascii=False, indent=2))

# ---------- Freigabe-Sperre ----------

def _freigaben() -> list[dict]:
    if not FREIGABEN.exists():
        return []
    return [json.loads(l) for l in FREIGABEN.read_text().splitlines() if l.strip()]


def cmd_freigabe(a) -> None:
    if len(a.zitat.strip()) < 3:
        raise GhostFehler("Ohne wörtliches Zitat von Tills Freigabe wird nichts eingetragen.")
    p = find_post(a.ref)
    entry = {"art": a.art, "post_id": p["id"], "slug": p["slug"], "titel": p["title"],
             "updated_at": p["updated_at"], "zitat": a.zitat.strip(),
             "zeit": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
             "sitzung": os.environ.get("CLAUDE_CODE_REMOTE_SESSION_ID", "")}
    FREIGABEN.parent.mkdir(parents=True, exist_ok=True)
    with FREIGABEN.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps(entry, ensure_ascii=False, indent=2))


def _pruefe_freigabe(p: dict, art: str) -> dict:
    passend = [f for f in _freigaben() if f["post_id"] == p["id"] and f["art"] == art]
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


def cmd_publish(a) -> None:
    p = find_post(a.ref, formats="lexical")
    if p["status"] == "published":
        print("Bereits veröffentlicht.")
        return
    _pruefe_freigabe(p, "beitrag")
    lex, removed = _ohne_intern(p["lexical"])
    rest = _restliche_platzhalter(lex)
    if rest:
        raise GhostFehler(f"SPERRE: Offene Platzhalter im Beitrag: {rest}")
    tags = [{"name": t["name"]} for t in p.get("tags", []) if t["name"] != "#zur-freigabe"]
    update = {"lexical": lex, "tags": tags, "updated_at": p["updated_at"]}
    if a.zeitpunkt:
        update.update({"status": "scheduled", "published_at": a.zeitpunkt})
    else:
        update["status"] = "published"
    # Bewusst ohne newsletter-Parameter: Beiträge gehen nie per E-Mail raus.
    res = api("PUT", f"posts/{p['id']}/", body={"posts": [update]})
    q = res["posts"][0]
    print(json.dumps({"status": q["status"], "url": q.get("url"), "published_at": q.get("published_at"),
                      "intern_absaetze_entfernt": removed}, ensure_ascii=False, indent=2))


def cmd_newsletter(a) -> None:
    p = find_post(a.ref, formats="lexical")
    _pruefe_freigabe(p, "newsletter")
    lex, removed = _ohne_intern(p["lexical"])
    rest = _restliche_platzhalter(lex)
    if rest:
        raise GhostFehler(f"SPERRE: Offene Platzhalter: {rest}")
    tags = [{"name": t["name"]} for t in p.get("tags", []) if t["name"] != "#zur-freigabe"]
    update = {"lexical": lex, "tags": tags, "updated_at": p["updated_at"], "status": "scheduled",
              "published_at": a.zeitpunkt, "email_only": True}
    res = api("PUT", f"posts/{p['id']}/", body={"posts": [update]},
              query={"newsletter": a.newsletter, "email_segment": "all"})
    q = res["posts"][0]
    print(json.dumps({"status": q["status"], "published_at": q.get("published_at"),
                      "intern_absaetze_entfernt": removed}, ensure_ascii=False, indent=2))

# ---------- Blog-Index ----------

ZAHL = re.compile(r"[^.!?]*\b\d[\d.,]*\s?(?:%|Prozent|Prozentpunkte|Mio\.|Milliarden|Millionen)[^.!?]*[.!?]")


def _plain(html: str) -> str:
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html or "", flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    for a_, b_ in (("&nbsp;", " "), ("&amp;", "&"), ("&quot;", '"'), ("&#x27;", "'"), ("&lt;", "<"), ("&gt;", ">")):
        t = t.replace(a_, b_)
    t = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), t)
    return re.sub(r"\s+", " ", t).strip()


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
            "zahlen": [z.strip() for z in ZAHL.findall(text)][:15],
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
    s = sub.add_parser("freigabe"); s.add_argument("ref"); s.add_argument("--art", required=True, choices=["beitrag", "newsletter"])
    s.add_argument("--zitat", required=True); s.set_defaults(fn=cmd_freigabe)
    s = sub.add_parser("publish"); s.add_argument("ref"); s.add_argument("--zeitpunkt"); s.set_defaults(fn=cmd_publish)
    s = sub.add_parser("newsletter"); s.add_argument("ref"); s.add_argument("--newsletter", required=True)
    s.add_argument("--zeitpunkt", required=True); s.set_defaults(fn=cmd_newsletter)
    a = ap.parse_args(argv)
    try:
        a.fn(a)
    except GhostFehler as e:
        print(f"FEHLER: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
