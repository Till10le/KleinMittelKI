# Prüfung: olg-hamm-chatbot-haftung

Datum: 19.10.2026 · Prüfer (unabhängig)
Ergebnis: **NICHT BESTANDEN** (ein Format-Mangel, sonst sauber; nach Korrektur bestanden)

Originale selbst gelesen (WebFetch, 19.10.2026):
- Volltext NRWE https://nrwe.justiz.nrw.de/olgs/hamm/j2026/4_UKl_3_25_Urteil_20260512.html
- Pressemitteilung https://www.justiz.nrw/presse/2026-05-12

## Checkliste

1. Fakten: ok (nach Korrektur). Az. 4 UKl 3/25, 12.05.2026, VZ NRW gegen Aesthetify GmbH, zwei Ärzte/Geschäftsführer,
   Terminbuchung und Fragen, § 5 UWG, kein „Dritter“ (PM), korrekte Daten entlasten nicht (PM), „voraussehen können
   und müssen“/„halluzinieren“ (Rn. 93 f.), Prompt-Anweisung und Keyword-Filter nach der Abmahnung als Beleg für
   Steuerungsgewalt (Rn. 12, 70, 95), Erfahrungssätze zurückgewiesen (Rn. 104), strenge Anforderungen im Gesundheitswesen (Rn. 93).
   Rechtskraft: Tenor „Die Revision wird zugelassen.“; NRWE-Kopfdaten „Rechtskraft: rechtskräftig“; PM schweigt dazu.
   Der Satz im Beitrag gibt genau das wieder und ist mit Stand datiert: ok.
2. Einschränkungen: ok (Gesundheitswesen, keine Aussage zu anderen Branchen, Stand Rechtskraft).
3. Originalveröffentlichung verlinkt: ok (NRWE-Volltext, PM des Gerichts). Keine Zweitquelle verlinkt.
4. Ich-Aussagen: ok. „Meine Einordnung“, Gedanke zum Mitnehmen, Testempfehlung und Handwerks-Beispiel im INTERN-Absatz als Vorschlag markiert.
5. Platzhalter: ok (keine).
6. Format: H2 exakt; Wörter 20 / 100 / 109 / 83 / 16 = 328 (Rahmen 260–330); Teaser 116 Zeichen, ungleich Titel; fuer_kmu 104 Zeichen: ok.
   **Mangel 1** siehe unten (zwei Bookmark-Karten).
7. Rubrik Aktuell / Entwicklungen + #empfehlung: ok (Urteil, kein Studie). Kein Duplikat im Blog-Index.
8. „Für KMU“-Zeile: ok.
9. Ton/Verbote: ok. Keine Floskeln, kein CTA, kein Handels-/Arbeitgeberbezug; Hinweis „ersetzt keine Rechtsberatung“ vorhanden.
10. KMU-Bezug: ok (Handwerksbetrieb 20–150 Leute, Geschäftsführung/Marketing, Testprozess vor Go-live).
11. Grafiken: keine – für Nachricht ohne starke Kennzahl zulässig: ok.
12. Vorschaubild angesehen: Kategorie ENTWICKLUNGEN mit Lime-Balken, Titel drei Zeilen lesbar, Logo, kleinmittelki.de, Lime-Kante: ok.
13. Ghost-Vorschau: in diesem Lauf nicht möglich (kein Ghost-Zugriff), nach Ghost-Lauf prüfen – kein Mangel.
14. Vergleich mit Referenz (werbung-chatgpt-sponsored-agents u. a. Nachrichten): Aufbau, Tags, Länge gleich; Abweichung siehe Mangel 1.
- tools/lexical.py läuft fehlerfrei (vor und nach Korrektur).

## Direkt korrigiert (Formulierung gegen Original)

- „Der Chatbot sei kein „Dritter“, sondern sein technisches Mittel.“ → „… sondern nur ein technisches Mittel des
  Betreibers.“ (Volltext: „(lediglich) ein technisches Mittel“; „sein“ war mehrdeutig).
- „Es ging um Gesundheit und um Werbung, dort gelten strenge Maßstäbe.“ → „Es ging um das Gesundheitswesen, dort gelten
  laut Gericht besonders strenge Maßstäbe.“ (Rn. 93 nennt nur Gesundheitsschutz/-wesen, nicht Werbung.)

## Mängel

1. **Zwei Bookmark-Karten unter „Zum Originalartikel“** (Ende beitrag.md). Format Nachricht verlangt eine Karte; alle
   neun veröffentlichten Nachrichten in `redaktion/referenz/` haben genau eine.
   Vorschlag: nur die NRWE-Karte behalten; die Pressemitteilung im Text verlinken, z. B. in „Was ist passiert?“:
   „Das Oberlandesgericht Hamm gab der Klage am 12. Mai 2026 statt ([Pressemitteilung](https://www.justiz.nrw/presse/2026-05-12), Az. 4 UKl 3/25).“

## Hinweise (kein Mangel)

- INTERN-Absatz bittet um Gegenlesen der Zitate „technisches Mittel“/„Steuerungsgewalt“: erledigt, beide wörtlich im
  Volltext (Rn. 70). Im Beitrag steht nur „technisches Mittel“ sinngemäß, „Steuerungsgewalt“ nicht als Zitat. Der Satz
  im INTERN-Absatz kann beim nächsten Bearbeiten entfallen.
- Rechtskraft vor Veröffentlichung erneut in den NRWE-Kopfdaten prüfen (wie im INTERN-Absatz vermerkt).

---

## Runde 2 – 19.10.2026

Ergebnis: **BESTANDEN**

- Mangel 1 behoben: nur noch die NRWE-Bookmark-Karte; Pressemitteilung im Text verlinkt (Originalquelle, Link korrekt).
  INTERN-Satz zu den Zitaten gestrichen.
- Durch die Überarbeitung neu entstanden und von mir direkt behoben:
  - Die Leerzeile zwischen INTERN-Absatz und Einstieg fehlte. Der Einstieg „Ein Kunde fragt …“ war damit Teil des
    INTERN-Absatzes, und `tools/ghost.py` (Zeile 319) entfernt Absätze, die mit „INTERN“ beginnen – der Einstieg wäre
    beim Veröffentlichen verschwunden. Leerzeile eingefügt.
  - „Was ist passiert?“ lag durch den Link bei 102 Wörtern (Rahmen 60–100). Gekürzt ohne Inhaltsverlust:
    „Verbraucherzentrale Nordrhein-Westfalen“ → „Verbraucherzentrale NRW“, „Oberlandesgericht Hamm“ → „OLG Hamm“,
    „ein Unternehmen für ästhetische Behandlungen“ → „einen Anbieter ästhetischer Behandlungen“,
    „die sich der Betreiber zurechnen lassen muss“ → „die dem Betreiber zuzurechnen ist“.
- Stand jetzt: Einstieg 20 · Was ist passiert? 99 · Meine Einordnung 109 · Mittelstand 83 · Gedanke 16 = 327 Wörter
  (260–330). Teaser 116, fuer_kmu 104 Zeichen. H2 exakt, eine Bookmark-Karte wie in den Referenz-Nachrichten.
- Fakten unverändert und weiter durch Volltext/PM gedeckt; keine neuen Ich-Sätze, keine Platzhalter, keine Verbotswörter.
- `tools/lexical.py` läuft fehlerfrei.
- Offen und kein Mangel: Ghost-Vorschau nach dem Ghost-Lauf prüfen; Rechtskraft vor Veröffentlichung in NRWE erneut
  ansehen; „Meine Einordnung“ und Gedanke bleiben INTERN-Vorschlag bis Tills Freigabe.
