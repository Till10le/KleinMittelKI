# Prüfung: modellwahl-kanonen-auf-spatzen

- Datum: 10.11.2026 (Redaktions-Lauf Di 12:47, Prüfrunde 1)
- Prüfer: Prüfer-Agent, unabhängig
- Ergebnis: **NICHT BESTANDEN**

Grund: Eine Kernaussage zu den Abo-Limits ist mit der verlinkten Quelle nicht mehr belegbar (Seite 404), und die heute
erreichbare Anthropic-Seite sagt etwas anderes. Betroffen sind Text, Grafik g2 und Quellenliste. Dazu kommt eine
Pauschalaussage zur Abo-Rechnung, die der Hersteller widerlegt, und der Text ist etwas zu lang. Alles andere ist in Ordnung.

## Mängel (müssen behoben werden)

### M1 – Opus „verbraucht das Wochenlimit schneller als Sonnet“: Quelle weg, Aussage nicht belegt (Punkt 1, 3, 11)
- Fundstellen: beitrag.md Abschnitt „Was der Sprit kostet“, Absatz **Limits** (Satz „Für Team- und Enterprise-Plätze schreibt
  Anthropic ausdrücklich, dass Opus das Wochenlimit schneller verbraucht als Sonnet, und empfiehlt Sonnet für den Alltag.“);
  Grafik `kmk-modellwahl-g2.png` (Abo-Kasten, dritter Punkt „Opus verbraucht das Wochenlimit schneller als Sonnet“);
  Quellenliste, Eintrag „About Team and Enterprise plan usage“.
- Befund: https://support.claude.com/en/articles/9267304-about-team-and-enterprise-plan-usage liefert am 10.11.2026 **HTTP 404**,
  auch ohne Slug. quellen.md hatte schon gewarnt, dass die Seite nur alte Modellnamen (Opus 4.5/Sonnet 4.5) nannte.
  Die aktuellen Help-Center-Seiten sagen etwas anderes:
  - „Usage limit best practices“ (https://support.claude.com/en/articles/9797557-usage-limit-best-practices) nennt die
    **Modellwahl** als Faktor, sagt aber nicht, welches Modell das Limit wie schnell verbraucht. Opus und Sonnet kommen dort
    nicht vor, eine Empfehlung für den Alltag auch nicht.
  - „Claude Fable models on your plan“ (https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan):
    Fable-Modelle „draw from your plan's regular weekly usage limits and use them faster than other Claude models“. Das gilt
    für Max, Ultra und **Premium-Plätze** in Team und sitzbasiertem Enterprise, dort höchstens 50 % des Wochenlimits für Fable.
    Auf **Standard-Team-Plätzen** und bei Pro läuft Fable nur über Nutzungsguthaben (usage credits) und zählt nicht gegen das Limit.
- Korrektur, Text, z. B.: „**Limits:** Laut [Anthropic](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
  hängt die Nutzungsgrenze unter anderem von der Länge der Nachrichten, der Größe der Dateien und von der Modellwahl ab. Beim
  stärksten Modell schreibt Anthropic es [ausdrücklich](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan):
  Fable verbraucht das Wochenlimit schneller als die anderen Claude-Modelle. Auf Standard-Plätzen im Team-Abo läuft Fable
  nur über zusätzlich bezahltes Guthaben. Wer morgens für jede Kleinigkeit das größte Modell nimmt, steht nachmittags bei der
  wichtigen Auswertung womöglich an der Grenze.“
- Korrektur, Grafik g2 (Grafik-Agent, neu rendern mit `--social`): dritten Punkt ersetzen, z. B. „Das stärkste Modell
  verbraucht das Wochenlimit schneller“. Die Fußzeile bleibt: „Quelle: Anthropic Help Center, Anthropic-Preisliste“.
- Korrektur, Quellen: Eintrag 9267304 streichen. Dafür „Claude Fable models on your plan“ aufnehmen und den Link auf
  9797557 auf die volle URL „…/9797557-usage-limit-best-practices“ ändern. quellen.md Abschnitt 4 nachziehen.

### M2 – „Die Rechnung am Monatsende ändert sich nicht, egal welches Modell“ stimmt so nicht mehr (Punkt 1)
- Fundstellen: beitrag.md Absatz 1 in „Was der Sprit kostet“; Box „Das Wichtigste in 30 Sekunden“, Punkt 2 („Im Abo zahlst
  du pro Platz … Echtes Geld kostet sie erst bei eigenen Anwendungen“); g2 Abo-Kasten, Punkt 1 („Rechnung bleibt gleich“);
  Schlussabschnitt Satz 1.
- Befund: Laut derselben Fable-Seite geht Fable auf Standard-Team-Plätzen und bei Pro nur über Nutzungsguthaben, also mit
  echtem Geld. Die Aussage stimmt für die üblichen Modelle, aber nicht pauschal. Das stützt die These des Beitrags sogar.
- Korrektur: einschränken, z. B. „Solange niemand Zusatzguthaben nutzt, ändert sich die Rechnung am Monatsende nicht.
  Ausnahme: Das stärkste Claude-Modell läuft auf Standard-Plätzen nur über solches Guthaben.“ In der Box reicht
  „… meist nicht über die Rechnung“. In g2 z. B. „Preis pro Platz, Rechnung meist gleich“.

### M3 – Länge über dem Rahmen (Punkt 6, 14)
- Befund: Ohne INTERN-Absatz und Platzhalter hat der Text rund 2.050 Wörter bis „Quellen“ und rund 2.190 mit Quellenliste.
  Die Vorgabe für einen Langtext ist 1.900–2.000. Zum Vergleich die Referenzbeiträge, gleich gezählt mit Quellen:
  Agenten 1.977, Modelle 1.919. Damit liegt der Text etwa 10 % darüber.
- Korrektur: um rund 150 Wörter kürzen. Kandidaten: im Abschnitt „Billig ist nicht immer günstig“ den Satz zu den zwei
  Entwickler-Wegen streichen (für Abo-Nutzer ohne Nutzen); FrugalGPT auf einen Satz kürzen; im Absatz **Strom** den Satz mit
  den Denk-Tokens (543,5/37,7) streichen; die Doppelung „Wie viel ein Router spart …“ streichen, weil sie schon in der
  Bildunterschrift von g4 steht.

## Hinweise (kein Mangel, zur Entscheidung)

- H1: „Sonnet für die meisten Anwendungen“ steht so in der Preisliste („Sonnet for most production workloads“). Die Seiten
  „Models overview“ und „Choosing the right model“ sagen dagegen „start with Claude Opus 5.5 for most workloads“. Das ist
  belegt, aber selektiv. Vorschlag: „Sonnet für Alltagsarbeit wie Texte und Datenanalyse“ (Auswahlmatrix), dann ist es eindeutig.
- H2: Unter der H2 „Zum Ausprobieren: drei Aufgaben, zwei Stufen“ steht eine Box mit eigener Überschrift „Zum Ausprobieren:
  die eigene Faustregel …“. Das wirkt doppelt. Im Agenten-Referenzbeitrag steht die Box ohne eigene H2. Vorschlag: Box-Kopf
  auf „Die eigene Faustregel in einer halben Stunde“ kürzen oder die H2 weglassen.
- H3: Bei den Versuchen zu Antwortlänge und Tabelle hat Anthropic ältere Modelle gemessen (laut Seite „earlier model“ bzw.
  Sonnet 5). Der Text nennt kein Modell und ist damit korrekt. Optional „mit einem älteren Modell“ ergänzen.

## Checkliste

| Nr. | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen gegen Originalquelle | **Mangel M1, M2.** Selbst geprüft und ok: Preise Haiku/Sonnet/Opus/Fable, Faktoren 20/40/80, eigene Rechnung 0,35/7/14/28 $, Tests (85/91 %, 1/20, 4,3-fach, 7 %), Antwortlänge 0,49/0,57/1,40 $, Tabelle 7/25 bei 5,01 $ und 25/25 bei 0,40 $, Prompt Caching, „directional, not guarantees“, Denkaufwand als Hebel, zwei Startwege, Stapel 50 %, Haiku „classification, extraction, routing“. **Nicht selbst prüfbar** (Host in dieser Umgebung gesperrt): lmsys.org (RouteLLM), arxiv.org (FrugalGPT), frontiersin.org (Dauner/Socher), help.openai.com (Auto, Admin-Umleitung, Modellwahl im Eingabefeld ab April 2026). Diese Angaben stimmen mit quellen.md überein; vor der Freigabe einmal im offenen Netz gegenlesen. |
| 2 | Grundgesamtheit und Einschränkungen | ok (Herstellermessung, offene Modelle, Forschung 2023/2024, API statt Chat, Annahme 2.000/300) |
| 3 | Originalveröffentlichung verlinkt | Mangel M1 (toter Link 9267304). Sonst Originale verlinkt |
| 4 | Keine erfundene Ich-Form, INTERN vollständig | ok, keine Ich-Form im Text, Vorschläge im INTERN-Absatz aufgezählt |
| 5 | Platzhalter | ok, zwei `[TILL: …]` bewusst offen und im INTERN-Absatz genannt |
| 6 | Überschriften, Länge, Teaser | Mangel M3 (Länge). Teaser 152 Zeichen, ungleich Titel, ok. Struktur nach Langtext ok |
| 7 | Rubrik, Kategorie, Tags | ok (Wissen / Leitfäden, `#wissen`) |
| 8 | „Für KMU“-Zeile | entfällt (kein Aktuell-Beitrag) |
| 9 | Ton und Verbote | ok, kein Hype, kein CTA, kein Handel, kein Arbeitgeber-Bezug |
| 10 | KMU-Bezug | ok (10–150 Leute, Ingenieurbüro mit 40 Leuten, Hausverwaltung, Lizenzverwaltung/Büroleitung) |
| 11 | Grafiken | Mangel M1/M2 in g2. g1, g3, g4: Baukasten, Titel als Aussage, Fußzeile mit Stand und Quelle, Alt-Texte und Bildunterschriften ok, Werte stimmen |
| 12 | Vorschaubild | ok, drei Zeilen, Logo, Lime-Kante |
| 12a | Titelbild | ok, ohne Titel, ein Merksatz, keine Zahl, `titelbild:` im Frontmatter |
| 13 | Ghost-Vorschau | ausgelassen (noch kein Entwurf in Ghost) |
| 14 | Vergleich mit Referenz | Mangel M3 (Länge); siehe auch H2. Aufbau, Box, 4 PNG, Schlussfolge („Was das für den Mittelstand bedeutet“ · „Ein Gedanke zum Mitnehmen“ · „Quellen“) wie in den Referenzen |

## Direkt korrigiert in beitrag.md

1. „**Geld:** Echte Euro geht es erst …“ → „**Geld:** Um echte Euro geht es erst …“ (Grammatik).
2. Preisliste: bei Haiku 5.5 „(bei Anfragen bis 100.000 Tokens)“ ergänzt. Laut Preisliste kostet Haiku darüber 0,50/2,50 $.
3. Stapelverarbeitung: „Antwort innerhalb von 24 Stunden“ → „Antwort meist innerhalb einer Stunde, spätestens nach
   24 Stunden, dafür 50 Prozent Rabatt“ (Batch-Doku: „most batches completing within 1 hour … after 24 hours“).
