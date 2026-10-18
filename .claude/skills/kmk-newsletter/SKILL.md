---
name: kmk-newsletter
description: Aufbau, Ton und Ablauf des wöchentlichen Newsletters von KLEIN. MITTEL. KI. (Dienstag 7 Uhr, nur per E-Mail) – vom Sonntags-Entwurf bis zur Einplanung nach Tills Freigabe.
---

# Newsletter

Versprechen auf der Seite: „KI verstehen. Ohne jeden Tag alles lesen zu müssen.“ Wöchentlich, Dienstag 7:00 Uhr,
über Ghost, nur per E-Mail. Der Hauptbeitrag der Woche geht zur selben Zeit online.

## Ablauf

1. **Sonntagabend** (Routine): Entwurf schreiben – `entwuerfe/newsletter-JJJJ-MM-TT/beitrag.md` mit Tag `#newsletter`,
   Kategorie leer lassen. Als Ghost-Entwurf anlegen. Vorher prüfen, ob es für diesen Dienstag schon einen gibt (keine Dubletten).
   Themen der Vorwoche nicht wiederholen (frühere `newsletter-*`-Ordner und Index lesen).
2. **Till** liest die Vorschau und antwortet „Newsletter ja“ oder mit Änderungen.
3. Chefredakteur: Freigabe der Art `newsletter` eintragen, dann
   `python3 tools/ghost.py newsletter <slug> --newsletter <slug-des-newsletters> --zeitpunkt <Dienstag 7:00 in UTC>`.

## Aufbau einer Ausgabe

- INTERN-Absatz oben (wird beim Einplanen entfernt): vorgeschlagene Stellen, Checkliste
- Im Frontmatter: `titel` = Betreff (höchstens 60 Zeichen, sachlich, kein Clickbait), `teaser` = Vorschautext
  (höchstens 90 Zeichen). Zwei Alternativen für beides in den INTERN-Absatz.
- Einstieg: 2–3 Sätze in Tills Stimme (als Vorschlag markieren, wenn nicht von Till)
- `## 01 · Neu auf dem Blog` – jeder neue Beitrag als Bookmark-Karte mit 1–2 Sätzen Nutzen. Kein neuer Beitrag → Abschnitt weglassen.
- `## 02 · Kurz eingeordnet` – 2–3 Meldungen: was passiert ist (1–2 Sätze), „Für deinen Betrieb heißt das: …“ (1–2 Sätze,
  konkret: Rolle, Prozess, Entscheidung), Link zur Originalquelle
- Zahlenblock „Eine Zahl, genau gelesen“ (HTML-Block, siehe unten), nur mit belegter Zahl
- `## Ein Gedanke zum Mitnehmen` – höchstens 40 Wörter
- Button-Absatz: [Alle Beiträge auf kleinmittelki.de](https://www.kleinmittelki.de/)
- Schluss (wörtlich): „Wenn du jemanden kennst, für den diese Themen gerade relevant sind: Leite die Mail gern weiter.
  Und wenn dich eine Frage rund um KI im Betrieb beschäftigt, antworte einfach auf diese Mail.“ Dann „Bis bald“ und „Till“.

## Zahlenblock (HTML)

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#111111;margin:24px 0"><tr><td style="padding:24px 26px"><p style="margin:0 0 6px;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#D7FF00;font-weight:700">Eine Zahl, genau gelesen</p><p style="margin:0;font-size:44px;line-height:1.1;font-weight:800;color:#D7FF00">{{ZAHL}}</p><p style="margin:10px 0 0;font-size:16px;line-height:1.5;color:#F4F3EE">{{WAS SIE AUSSAGT}}</p><p style="margin:10px 0 0;font-size:13px;line-height:1.5;color:#B8B8B0">Genau gelesen: {{LESART}}. Quelle: {{QUELLE, DATUM}}.</p></td></tr></table>
```

OFFEN: Die echte Vorlage aus Ausgabe 1 und 2 liegt in Ghost. Beim ersten Lauf eine frühere Ausgabe mit
`tools/ghost.py get <slug> --raw` lesen und diesen Block durch die echte Vorlage ersetzen (als Vorschlag an Till).

## Ton

Wie im Blog (`kmk-schreibstil`), aber noch kürzer. Kein „Hallo zusammen“, keine Gefühlswörter, keine Werbung.
