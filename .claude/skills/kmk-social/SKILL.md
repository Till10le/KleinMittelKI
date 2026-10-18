---
name: kmk-social
description: Regeln und Vorlagen für LinkedIn, Instagram und WhatsApp-Status von KLEIN. MITTEL. KI. – sachlich, ohne Influencer-Ton, Link im ersten Kommentar, Karussell im CI. Laden, bevor ein Social-Post entsteht.
---

# Social Media

Jeder Inhalt wird viermal genutzt: Blog → Newsletter → LinkedIn → WhatsApp. Nicht zufällig posten, aber auch nicht alles an einem Tag.
Gepostet wird erst nach Tills Freigabe. Kommentieren macht Till selbst.

## Rhythmus

| Wann | Was | Kanal |
|---|---|---|
| Dienstag vormittags | Hinweis auf neue Ausgabe/Beitrag | WhatsApp-Status (Till postet selbst) |
| Donnerstag mittags | Ein Post pro Woche | LinkedIn |
| nach Bedarf | Karussell zu Praxistest oder Wissensbeitrag | Instagram (Konto noch offen) |

## LinkedIn

- Einmal pro Woche. Erster Satz = Nutzen oder überraschende Beobachtung für den Leser, nicht „Ich habe …“.
- 600–1.200 Zeichen, kurze Absätze, keine Hashtag-Wolken (höchstens 3 sachliche).
- Link nie im Post, sondern im ersten Kommentar. Höchstens ein Emoji (👉 vor dem Link im Kommentar).
- Am besten: Praxistests mit Vorher/Nachher, eine Zahl genau gelesen, ein konkreter Test zum Nachmachen.
- Nie: Gefühlswörter, „schaut mal, wie einfach“, Köder-Fragen, zweite Ankündigung des Blogs, Handel, Politik.

Ausgabe in `entwuerfe/<slug>/social.md`:

```
## LinkedIn
<Text>

## Erster Kommentar
👉 <URL des Beitrags>

## WhatsApp-Status
<höchstens 2 Sätze + URL>

## Instagram (optional)
Folie 1: <Titel, höchstens 8 Wörter>
Folie 2–6: <je ein Gedanke, höchstens 25 Wörter>
Letzte Folie: „Mehr auf kleinmittelki.de“
Bildtext: <höchstens 3 Sätze>
```

## Instagram-Karussell im CI

- Format 1080 × 1350 (4:5). OFFEN: Ein eigener Renderer dafür wird gebaut, sobald das Instagram-Konto steht.
  Bis dahin nur die Folientexte vorbereiten.
- Weißer Grund, Ink-Schrift, ein Lime-Element pro Folie, Kategorie-Label oben, „kleinmittelki.de“ unten.
- Keine Fotos von Personen außer Till, keine Stockbilder.

## WhatsApp

Erreicht das regionale Netzwerk (Ortenau) besser als LinkedIn. Text kurz und persönlich-sachlich, z. B.
„Neu: Was der AI Act für KI-Bilder in Betrieben wirklich heißt. Fünf Fälle, klare Antworten.“
