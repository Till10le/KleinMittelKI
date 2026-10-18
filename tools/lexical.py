#!/usr/bin/env python3
"""Macht aus einem beitrag.md Ghosts Editor-Format (Lexical-JSON).

Unterstützte Syntax im Beitragstext (alles andere wird ein normaler Absatz):

    ## Zwischenüberschrift            -> H2 (### -> H3)
    Absatz mit **fett**, *kursiv* und [Link](https://…)
    - Punkt / 1. Punkt                 -> Aufzählung / nummerierte Liste
    ![Alt-Text](https://bild.png "Bildunterschrift")   -> Bildkarte (allein in einer Zeile)
    ```html … ```                      -> HTML-Karte (Grafik-Bausteine)
    :::bookmark URL | Titel | Herausgeber | Beschreibung   -> Bookmark-Karte (Quelle)
    ---                                -> Trennlinie

Kopf der Datei (Frontmatter zwischen zwei Zeilen mit ---):

    titel: …
    slug: …
    kategorie: Studien & Zahlen
    tags: [#empfehlung]
    teaser: …
    fuer_kmu: …            (nur Aktuell)
    vorschaubild: vorschaubild.png

Aufruf zum Testen:  python3 tools/lexical.py entwuerfe/<slug>/beitrag.md
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------- Frontmatter ----------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n")
    meta: dict = {}
    end = None
    current_list_key = None
    for i, line in enumerate(parts[1:], start=1):
        if line.strip() == "---":
            end = i
            break
        if not line.strip() or line.lstrip().startswith("#!"):
            continue
        m_item = re.match(r"^\s*-\s+(.*)$", line)
        if m_item and current_list_key:
            meta[current_list_key].append(_unquote(m_item.group(1)))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not m:
            raise ValueError(f"Frontmatter-Zeile {i} nicht lesbar: {line!r}")
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            meta[key] = []
            current_list_key = key
            continue
        current_list_key = None
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [_unquote(v.strip()) for v in inner.split(",") if v.strip()] if inner else []
        else:
            meta[key] = _unquote(val)
    if end is None:
        raise ValueError("Frontmatter wird nicht mit --- geschlossen")
    return meta, "\n".join(parts[end + 1:])


def _unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v

# ---------- Lexical-Knoten ----------

def _text(t: str, fmt: int = 0) -> dict:
    return {"detail": 0, "format": fmt, "mode": "normal", "style": "", "text": t,
            "type": "extended-text", "version": 1}


def _link(url: str, children: list) -> dict:
    return {"children": children, "direction": "ltr", "format": "", "indent": 0, "type": "link",
            "version": 1, "rel": None, "target": None, "title": None, "url": url}


INLINE = re.compile(r"(\*\*(?P<b>.+?)\*\*|\*(?P<i>[^*]+?)\*|\[(?P<lt>[^\]]+)\]\((?P<lu>[^)\s]+)\))")


def inline(s: str) -> list:
    """Wandelt **fett**, *kursiv* und [Text](URL) in Lexical-Kinder um."""
    out: list = []
    pos = 0
    for m in INLINE.finditer(s):
        if m.start() > pos:
            out.append(_text(s[pos:m.start()]))
        if m.group("b") is not None:
            out.extend(_with_format(inline(m.group("b")), 1))
        elif m.group("i") is not None:
            out.extend(_with_format(inline(m.group("i")), 2))
        else:
            out.append(_link(m.group("lu"), inline(m.group("lt"))))
        pos = m.end()
    if pos < len(s):
        out.append(_text(s[pos:]))
    return [n for n in out if n.get("type") != "extended-text" or n["text"] != ""]


def _with_format(nodes: list, fmt: int) -> list:
    for n in nodes:
        if n["type"] == "extended-text":
            n["format"] |= fmt
        elif n["type"] == "link":
            _with_format(n["children"], fmt)
    return nodes


def paragraph(s: str) -> dict:
    return {"children": inline(s), "direction": "ltr", "format": "", "indent": 0,
            "type": "paragraph", "version": 1}


def heading(s: str, level: int) -> dict:
    return {"children": inline(s), "direction": "ltr", "format": "", "indent": 0,
            "type": "extended-heading", "version": 1, "tag": f"h{level}"}


def listnode(items: list[str], ordered: bool) -> dict:
    children = []
    for n, it in enumerate(items, start=1):
        children.append({"children": inline(it), "direction": "ltr", "format": "", "indent": 0,
                         "type": "listitem", "version": 1, "value": n})
    return {"children": children, "direction": "ltr", "format": "", "indent": 0, "type": "list",
            "version": 1, "listType": "number" if ordered else "bullet", "start": 1,
            "tag": "ol" if ordered else "ul"}


def html_card(html: str) -> dict:
    return {"type": "html", "version": 1, "html": html.strip()}


def image_card(src: str, alt: str, caption: str) -> dict:
    return {"type": "image", "version": 1, "src": src, "width": None, "height": None, "title": "",
            "alt": alt, "caption": caption, "cardWidth": "regular", "href": ""}


def bookmark_card(url: str, title: str, publisher: str, desc: str) -> dict:
    return {"type": "bookmark", "version": 1, "url": url,
            "metadata": {"icon": "", "title": title, "description": desc, "author": "",
                         "publisher": publisher, "thumbnail": ""},
            "caption": ""}


def divider() -> dict:
    return {"type": "horizontalrule", "version": 1}

# ---------- Parser ----------

IMG = re.compile(r'^!\[(?P<alt>[^\]]*)\]\((?P<src>\S+)(?:\s+"(?P<cap>[^"]*)")?\)$')


def to_nodes(body: str) -> list:
    lines = body.split("\n")
    nodes: list = []
    para: list[str] = []
    items: list[str] = []
    ordered = False
    i = 0

    def flush_para():
        if para:
            nodes.append(paragraph(" ".join(x.strip() for x in para)))
            para.clear()

    def flush_list():
        if items:
            nodes.append(listnode(list(items), ordered))
            items.clear()

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("```html"):
            flush_para(); flush_list()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            if i >= len(lines):
                raise ValueError("HTML-Block wird nicht mit ``` geschlossen")
            nodes.append(html_card("\n".join(buf)))
            i += 1
            continue
        if stripped == "":
            flush_para(); flush_list()
        elif stripped.startswith("### "):
            flush_para(); flush_list(); nodes.append(heading(stripped[4:], 3))
        elif stripped.startswith("## "):
            flush_para(); flush_list(); nodes.append(heading(stripped[3:], 2))
        elif stripped.startswith("# "):
            raise ValueError("H1 nicht erlaubt: Der Titel steht im Frontmatter.")
        elif stripped == "---":
            flush_para(); flush_list(); nodes.append(divider())
        elif stripped.startswith(":::bookmark"):
            flush_para(); flush_list()
            fields = [f.strip() for f in stripped[len(":::bookmark"):].split("|")]
            fields += [""] * (4 - len(fields))
            if not fields[0].startswith("http"):
                raise ValueError(f"Bookmark ohne URL: {stripped}")
            nodes.append(bookmark_card(*fields[:4]))
        elif IMG.match(stripped):
            flush_para(); flush_list()
            m = IMG.match(stripped)
            nodes.append(image_card(m.group("src"), m.group("alt"), m.group("cap") or ""))
        elif re.match(r"^[-*]\s+", stripped):
            flush_para()
            if items and ordered:
                flush_list()
            ordered = False
            items.append(re.sub(r"^[-*]\s+", "", stripped))
        elif re.match(r"^\d+[.)]\s+", stripped):
            flush_para()
            if items and not ordered:
                flush_list()
            ordered = True
            items.append(re.sub(r"^\d+[.)]\s+", "", stripped))
        else:
            flush_list()
            para.append(stripped)
        i += 1
    flush_para(); flush_list()
    return nodes


def build(md_text: str) -> tuple[dict, str]:
    """Gibt (Frontmatter, Lexical-JSON-String) zurück."""
    meta, body = parse_frontmatter(md_text)
    root = {"root": {"children": to_nodes(body), "direction": "ltr", "format": "", "indent": 0,
                     "type": "root", "version": 1}}
    return meta, json.dumps(root, ensure_ascii=False)


def headings_of(lexical: str) -> list[str]:
    root = json.loads(lexical)["root"]["children"]
    return ["".join(c.get("text", "") for c in n["children"]) for n in root if n["type"] == "extended-heading"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    meta, lex = build(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps({"frontmatter": meta, "zwischenueberschriften": headings_of(lex),
                      "knoten": len(json.loads(lex)["root"]["children"])}, ensure_ascii=False, indent=2))
