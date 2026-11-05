# Quellen: ki-agent-beeinflusst-entscheidungen

Stand: 2026-11-05 (Scout, Lauf 7:47). Abgerufen am 05.11.2026. Hinweis aus ChatGPT (Eingang 2026-10-31, Punkt 1) – alle Angaben am Original geprüft.

## Originalquelle (selbst gelesen)
- Anthropic (Research), „How AI agents shape experts' judgment calls“, **27. Oktober 2026**.
  Autoren: Amaç Herdağdelen, Hailey Joren, Alex Tamkin.
  https://www.anthropic.com/research/agents-judgment-calls
- Herausgeber ist ein KI-Hersteller, untersucht wurde das eigene Produkt (Claude Code mit Claude Opus 4.8). Offen benennen.

## Nicht verwenden
- the-decoder.de (29.10.2026) – Zweitverwertung, nicht gelesen, nicht zitieren.

## Studiendesign (laut Original)
- 61 Analysten randomisiert; 11 verzichteten auf den KI-Agenten → **50 Analysten** in der Hauptauswertung.
- Teilnehmende: vorgeprüfte Fachleute mit Erfahrung in kausaler Inferenz (Beobachtungsdaten), die regelmäßig Python oder R nutzen.
- Aufgabe: Für eine **fiktive** landwirtschaftliche Genossenschaft („Greenfields“) prüfen, ob ein freiwilliges Beratungsprogramm
  die Produktivität um etwa 3–4 % steigert; danach empfehlen: ausweiten oder einstellen (einjährige Verlängerung ebenfalls möglich).
- Vier offene Analyseentscheidungen mit je zwei vertretbaren Optionen: Zielgröße, Vergleichsmethode, abgedeckte Betriebe, Gewichtung.
- Agent: Claude Code mit Claude Opus 4.8 (High Effort). Per Münzwurf bekam der Agent je Entscheidung eine **verdeckte Präferenz**,
  die er vertreten sollte. Die Analysten wussten das nicht.
- Median-Bearbeitungszeit: 65 Minuten.

## Zahlen (exakt, mit Bezug)
- **86 %**: Anteil der Analyseentscheidungen (alle vier zusammen), in denen die Analysten die Option wählten, zu der der Agent
  tendierte. Zufallsniveau etwa 50 %. **Bezug: Entscheidungen, nicht Personen, nicht die Abschlussempfehlung.**
  (Formulierung der ChatGPT-Mail „folgten in 86 % der untersuchten Entscheidungen“ ist so korrekt; „50 Fachanalysten“ stimmt für die Hauptauswertung.)
  - Einzelwerte: Zielgröße 92 %, Vergleichsmethode 82 %, abgedeckte Betriebe 81 %, Gewichtung 90 %.
- Abschlussempfehlung: Agent-Präferenz „ausweiten“ → 54 % empfahlen Ausweitung; Gegenpräferenz → 36 %. Effekt hier schwächer
  (laut Quelle 17 Prozentpunkte; Differenz der gerundeten Werte wäre 18 – im Beitrag die Angabe der Quelle nehmen oder nur 54 vs. 36 nennen).
- Analysten mit vorheriger eigener Wahl (38 Fälle): bei Widerspruch des Agenten wechselten 60 % ihre Wahl, bei Zustimmung 6 %.
  95-%-Konfidenzintervall 24 bis 82 Prozentpunkte (unpräzise, kleine Fallzahl).
- Aus den vier Präferenzen ließ sich die Abschlussempfehlung in 82 % der Fälle vorhersagen (Basiswert 61 %).
- 77 % übernahmen Argumente des Agenten in ihre Begründungen (teils wörtlich); nur 15 % nannten den Agenten als Quelle.
- 52 % hielten die Empfehlung eher für ihre eigene als die des Agenten. Selbstvertrauen 71 (Folgende) vs. 73 (Übrige) auf 0–100.
- Ohne KI: 6 von 11 (55 %) mit gravierenden Methodenfehlern; mit KI 3 von 50 (6 %). **Nicht randomisiert**, Gruppe ohne KI weniger
  erfahren → kein kausaler Schluss.

## Einschränkungen (laut Autoren und eigene)
- Agent-Präferenzen wurden **bewusst verstärkt**; reale Assistenten mit schwächeren Tendenzen könnten weniger Einfluss haben.
- Eine Aufgabe, ein Fachgebiet (Landwirtschaft), ein Modell, fiktiver Fall.
- Durchschnittswerte; Ausgangsmeinung und Präferenzstärke der Analysten nicht erhoben.
- Kleine Stichprobe (50, Teilgruppe 38).
- Teilnehmende sind Datenanalysten, keine Inhaber oder Geschäftsführer von KMU. Übertragung auf KMU-Entscheidungen
  (Preis, Investition, Personal) ist **unsere Ableitung**, nicht Ergebnis der Studie.
- Herstellerforschung über das eigene Produkt.

## Empfehlungen der Autoren (in eigenen Worten)
- Abhängigkeit vom Agenten messbar machen; Fachleute bemerken sie selbst kaum.
- Agenten so gestalten, dass sie für jede Option das stärkste Argument liefern, erst die Meinung des Menschen erfragen oder nur
  die wichtigsten Weichen hervorheben.
- Festlegen, welche Entscheidungen menschliches Urteil brauchen, und Zeit dafür einplanen.
- Ein menschlicher Prüfer ist nur dann eine unabhängige Kontrolle, wenn sein Urteil wirklich sein eigenes ist.
- Die Autoren plädieren nicht für weniger KI, sondern für bewusste Wahl, was man abgibt.

## Interne Verlinkung
- „KI irrt sich und klingt trotzdem sicher: So prüfst du KI-Ergebnisse im Betrieb“ (ki-ergebnisse-pruefen-leitfaden, veröffentlicht) –
  ergänzt ihn: dort geht es um falsche Fakten, hier um Einfluss auf die eigene Abwägung.
- „KI-Agenten: Was nach dem Chatbot kommt und was KMU davon haben“ (veröffentlicht).
