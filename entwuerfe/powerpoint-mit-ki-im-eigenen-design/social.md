# Social-Paket: powerpoint-mit-ki-im-eigenen-design

Stand: 2026-11-08 (Social, Sonntags-Lauf). Nichts gepostet. Beitrag von Till am 06.11.2026 selbst in Ghost veröffentlicht.
Inhalt nur aus dem veröffentlichten Beitragstext (`redaktion/referenz/powerpoint-mit-ki-im-eigenen-design.html`).
Format: Praxistest, damit nach `kmk-social` der beste Typ für LinkedIn und für ein Karussell geeignet.

> INTERN – vor dem Posten entfernen: Der LinkedIn-Text hat Ich-Sätze. Sie stammen sinngemäß aus Tills veröffentlichtem
> Beitrag, neu sind sie nicht: „Ich habe in Claude dreimal dieselben sechs Folien bestellt …“ (Abschnitt „Wie lief der Test ab?“),
> „Mir war das nicht aufgefallen.“ (wörtlich, „Der Aha-Moment“), „Grenze meines Tests …“ (aus „Wo sind die Grenzen?“).
> Die Wertung „Mir gefällt C am besten“ steht bewusst nicht im Post. Till bitte bestätigen oder umformulieren.

## Termine (Vorschlag, Till entscheidet)

Im Vorrat liegen schon zwei LinkedIn-Pakete, beide „frühestens Do 12.11.“: `nicht-jedes-problem-braucht-ki` und
`eu-eurobarometer-ki-unternehmen`. Ein LinkedIn-Post pro Woche, donnerstags mittags. Vorschlag:

| Termin | Kanal | Paket |
|---|---|---|
| Di 10.11. vormittags | WhatsApp-Status | dieser Beitrag (falls am 10.11. ki-recherche-assistent-selbstversuch erscheint, hat der Vorrang; dieser Status dann Mi 11.11.) |
| Do 12.11. mittags | LinkedIn | **dieser Beitrag** (der frischeste, und ein Praxistest mit Vorher/Nachher) |
| Do 19.11. mittags | LinkedIn | nicht-jedes-problem-braucht-ki |
| Do 26.11. mittags | LinkedIn | eu-eurobarometer-ki-unternehmen |

Instagram nach Bedarf, sobald das Konto steht (Konto noch offen).

## LinkedIn

Petrol, Symbole in Kreisen, abgerundete Kästen: Präsentationen aus der KI erkennt man oft nach zwei Sekunden. Das liegt weniger am Werkzeug als an dem, was man ihm mitgibt.

Ich habe in Claude dreimal dieselben sechs Folien bestellt, mit identischem Text. Geändert hat sich nur das Material:

A – ohne Vorgaben: ordentlich, aber mit KI-Stempel.
B – mit Brandbook (PDF, 18 Seiten): sofort als Marke erkennbar. Nur das Logo fehlt, weil das Brandbook verbietet, es nachzubauen.
C – mit Brandbook und PowerPoint-Vorlage: Logo, Fußzeile und Seitenzahlen sind drin. Neue Folien bekommen die zehn Folienrahmen der Vorlage.

Dazu kam eine Stelle, mit der ich nicht gerechnet hatte: Brandbook und Vorlage widersprachen sich bei der Akzentfarbe. Mir war das nicht aufgefallen. Claude schon, und es hat dazugeschrieben, wem es gefolgt ist.

Für den Schreiner mit dem Küchenentwurf oder das Immobilienbüro mit der Eigentümerpräsentation heißt das: Vorlage und Logo mitgeben, Unterlagen vorher abgleichen, im Auftrag sagen, was im Zweifel gilt. Wer nichts davon hat, startet mit einem kurzen Design-Steckbrief.

Grenze meines Tests: ein Durchlauf je Variante, mit meinem eigenen, sehr genauen Brandbook.

#KI #Mittelstand #PowerPoint

(ca. 1.150 Zeichen)

Bild: Dokument-Post mit den Kacheln 1 bis 7 (siehe Instagram). Kürzere Variante: nur `kmk-praesentation-k3-social.png` (Ergebnis A/B/C) als Einzelbild.

## Erster Kommentar

👉 https://www.kleinmittelki.de/powerpoint-mit-ki-im-eigenen-design/

## WhatsApp-Status

Neu: Dreimal dieselbe Präsentation mit KI, nur eine sieht nach KI aus. Woran es liegt und wie du es im Betrieb nachmachst, mit Kopiervorlagen.
https://www.kleinmittelki.de/powerpoint-mit-ki-im-eigenen-design/

## Instagram (optional)

Kacheln 1080 × 1350 im Ordner, je eine pro Folie (mit `tools/grafik.py --social` gerendert, alle angesehen):

Folie 1: Dreimal dieselbe Präsentation mit KI. Nur eine sieht nach KI aus. → `kmk-praesentation-k1-social.png`
Folie 2: Gleicher Auftrag, jedes Mal mehr Material: nur der Auftrag, dann mit Brandbook, dann zusätzlich mit PowerPoint-Vorlage. → `kmk-praesentation-k2-social.png`
Folie 3: Ohne Vorgaben gibt es den KI-Look. Mit Brandbook sieht es nach dem Betrieb aus. Mit Vorlage wie aus einem Guss. → `kmk-praesentation-k3-social.png`
Folie 4: Brandbook und Vorlage widersprachen sich. Claude folgte der Vorlage und schrieb es dazu. → `kmk-praesentation-k4-social.png`
Folie 5: Gib der KI mit, was du schon hast: Vorlage und Logo, Brandbook oder einen kurzen Design-Steckbrief. → `kmk-praesentation-k5-social.png`
Folie 6: Vor dem Termin selbst nachsehen: Schriften, Logo-Datei, Bearbeitbarkeit. Ein Test, eigenes Material. → `kmk-praesentation-k6-social.png`
Letzte Folie: „Mehr auf kleinmittelki.de“ → `kmk-praesentation-k7-social.png`

Bildtext: Dreimal dieselben sechs Folien mit KI: ohne Vorgaben, mit Brandbook, mit Brandbook und Vorlage. Nur die erste sieht nach KI aus. Alle Ergebnisse und die Kopiervorlagen auf kleinmittelki.de.

Fußzeile der Kacheln: „Eigener Test · Stand: 06.11.2026 · Claude Opus 5.5, je Variante ein Durchlauf“.
Quellen der Kacheln: `k1.html` bis `k7.html`. Die Querformat-PNGs `kmk-praesentation-kN.png` entstehen beim Rendern mit; sie gehören nicht in den Beitrag.

Technik-Hinweis: Playwright konnte seinen Browser nicht laden (Proxy sperrt cdn.playwright.dev). Gerendert wurde mit dem unveränderten
`tools/grafik.py` über System-Chrome (`/usr/bin/google-chrome`).
