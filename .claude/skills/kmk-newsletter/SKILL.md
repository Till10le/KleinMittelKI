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

Übernommen aus den Ausgaben 2 (13.10.2026) und 3 (20.10.2026) in Ghost, ausgelesen am 18.10.2026.
Ausgabe 1 hatte noch einen anderen Aufbau und gilt nicht als Vorlage.

- INTERN-Absatz oben (wird beim Einplanen entfernt): vorgeschlagene Stellen, Checkliste
- Im Frontmatter: `titel` = Betreff in der Form `#<Nummer>: <Thema>` (höchstens 60 Zeichen, sachlich, kein Clickbait),
  `teaser` = Vorschautext, eine Aufzählung dessen, was drinsteht (Ausgabe 2 und 3: 105–130 Zeichen, z. B. „Was nach dem
  Chatbot kommt, wie ein Industriebetrieb sein Wissen sichert, eine Zahl zu KI-Agenten in der EU und ein Gedanke für
  deinen Betrieb.“). Zwei Alternativen für beides in den INTERN-Absatz. Nummer = letzte Ausgabe im Index + 1.
- Einstieg: „Hallo,“ als eigener Absatz, dann ein Absatz „in dieser Ausgabe geht es um …“ (1–3 Sätze, Tills Stimme,
  als Vorschlag markieren, wenn nicht von Till)
- Nummerierte Abschnitte `## 01 · …`, `## 02 · …` – je neuer Beitrag ein Abschnitt. Überschrift mit Art und Thema:
  `Neu im Blog: …`, `Selbst ausprobiert: …` (Praxistest), `Aktuell eingeordnet: …` (Nachricht).
  Darunter 2–3 kurze Absätze (Worum geht es, was ist der Haken, was steht im Beitrag), dann die Bookmark-Karte:
  `:::bookmark <URL> | <Titel> | KLEIN. MITTEL. KI. | <Teaser>`
- `## 0X · Eine Zahl, genau gelesen` – Zahlenblock (HTML, unten), nur mit belegter Zahl
- `## 0X · Ein Gedanke zum Mitnehmen` – ein Absatz, höchstens 40 Wörter, greift die Themen der Ausgabe auf
- Button: `:::button Alle Beiträge auf kleinmittelki.de | https://www.kleinmittelki.de/`
- Trennlinie `---`
- Schluss (wörtlich): „Wenn du jemanden kennst, für den diese Themen gerade wichtig sind, leite die Mail gern weiter.
  Und wenn dich eine Frage rund um KI im Betrieb beschäftigt, antworte einfach auf diese Mail.“
  Dann je ein Absatz „Bis bald“ und „Till“.

## Zahlenblock (HTML)

Wörtlich aus Ausgabe 2 und 3. Oben steht die Quelle als Kopfzeile (`Herausgeber · Monat Jahr`).

```html
<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="background:#111111;border-bottom:6px solid #D7FF00;"><tr><td style="padding:28px 28px 24px;font-family:Helvetica,Arial,sans-serif;"><div style="font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#D7FF00;font-weight:700;">{{HERAUSGEBER}} · {{MONAT JAHR}}</div><div style="font-size:56px;line-height:1.05;font-weight:700;color:#D7FF00;margin:10px 0 8px;">{{ZAHL}}</div><div style="font-size:16px;line-height:1.5;color:#FFFFFF;">{{WAS SIE AUSSAGT}}</div><div style="font-size:14px;line-height:1.5;color:#BDBDB5;margin-top:10px;"><strong style="color:#FFFFFF;">Genau gelesen:</strong> {{LESART: wer hat gemessen, was zählt mit, was folgt für deinen Betrieb}}</div></td></tr></table>
```

Zeichen wie `>` im HTML als `&gt;` schreiben (Ausgabe 3: `&gt;8×`).

OFFEN (Vorschlag an Till, 18.10.2026): Der Block in Ausgabe 2 und 3 verlinkt die Originalquelle nicht.
Nach Regel 3 in `CLAUDE.md` sollte sie verlinkt sein – Vorschlag: ein Absatz direkt unter dem Block
„Quelle: [Herausgeber, Titel](URL)“. Bis Till entscheidet, den Absatz setzen.

## Ton

Wie im Blog (`kmk-schreibstil`), aber noch kürzer. Anrede nur „Hallo,“ – kein „Hallo zusammen“, keine Gefühlswörter, keine Werbung.
