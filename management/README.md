# management/ – Aufgaben- und Ergebnissystem (Head of KMI)

Stand: 20.11.2026 · Pflege: Head of KMI (Grok Bot). Claude-Läufe dürfen lesen und ihre eigenen Zeilen in `aufgaben.md` fortschreiben.

## Zweck

Ein gemeinsamer Wissensstand für Wachstum, SEO, Newsletter, Distribution und Betrieb von KLEIN. MITTEL. KI.
Hier steht, **was geplant, vorbereitet, umgesetzt und geprüft ist**, mit Beleg. Die Redaktionsarbeit selbst (Themen, Texte,
Freigaben) bleibt in `redaktion/` und `docs/lauf.md`. Dieser Ordner verdoppelt sie nicht, er steuert und misst sie.

| Datei | Inhalt |
|---|---|
| `aufgaben.md` | Alle Aufgaben mit ID, Bereich, Verantwortlichem, Status, Datum, Beleg |
| `kennzahlen.md` | Baseline und wöchentliche Fortschreibung; nur gemessene Werte mit Quelle |
| `experimente.md` | Wachstumsexperimente: Hypothese, Maßnahme, Messgröße, Zeitraum, Ergebnis |

## Rollen

- **Till** – gibt frei und entscheidet: Themenwahl, Vorschau-Link (Veröffentlichung), echte Entscheidungen. Sonst nichts.
- **Head of KMI** (Grok Bot) – Steuerung, Wachstum, SEO-/Wachstumsanalyse, Kontrolle der Ergebnisse, Kommunikation mit Till
  (Themenvorschläge, Vorschau-Link, wöchentlicher Bericht). Arbeitet lesend am Blog, schreibt nur unter `management/`.
- **Claude-Redaktion** (geplante Aufgabe „KMK Redaktion“, Agenten Chefredakteur, Scout, Autor, Prüfer, Ideen, Social, Analyst) –
  Recherche, Text, Design, Ghost-Upload über `tools/ghost.py`. Hält die Regeln aus `CLAUDE.md` ein.

## Freigabegrenzen (nur mit Tills ausdrücklicher Zustimmung)

1. Veröffentlichung und jede Änderung an bereits veröffentlichten Inhalten (auch Titel, Meta, Links, Slugs, Tags, Seiteneinstellungen).
2. Versand von Mails, Nachrichten, Newsletter und Social-Posts.
3. Kosten: kostenpflichtige Dienste, Abos, Werbung.
4. Rechtliches und Sicherheit (Impressum, Datenschutz, Schlüssel, Zugriffsrechte).
5. Löschen wichtiger Daten und wesentliche Änderungen von Zugriffsrechten. Im Repo gilt ohnehin: nie löschen, nur markieren.

Alles andere Interne und Reversible (Analyse, Entwürfe, Planung, Dokumentation unter `management/`) braucht keine Rückfrage.

## Kommunikationsregel

Till bekommt von Head of KMI nur:
1. **Themenvorschläge** (er wählt),
2. den **Vorschau-Link** eines fertigen Beitrags (er gibt frei),
3. **echte Entscheidungen**, vollständig vorbereitet (Ja/Nein),
4. den **wöchentlichen Managementbericht**.

Berichte nennen nur ausgeführte und geprüfte Arbeit und trennen klar: **geplant · vorbereitet · umgesetzt · geprüft**.

## Status-Definition

| Status | Bedeutung |
|---|---|
| geplant | beschlossen oder vorgeschlagen, noch nichts getan |
| vorbereitet | Entwurf, Konfiguration oder Antrag liegt bereit, Wirkung/Freigabe fehlt |
| umgesetzt | ausgeführt, Wirkung noch nicht kontrolliert |
| geprüft | Wirkung mit Beleg kontrolliert (Bericht, Messwert, Link) |

## Freigabe-Mechanik (Kurzfassung, Details: `docs/lauf.md`, `CLAUDE.md`)

- Themenwahl: Till antwortet per Mail („1 und 3“). Der nächste Lauf liest sie in Gmail (Absender Till, Label „Gesendet“, ID nicht in
  `redaktion/mail.json` → `verarbeitet`), setzt den Board-Status `freigegeben` und trägt Ja/Nein mit wörtlichem Zitat in
  `redaktion/entscheidungen.md` ein.
- Veröffentlichung: „A ja“ per Mail → `tools/mailfreigabe.py` schreibt eine Zeile in `redaktion/freigaben.jsonl`
  (gebunden an Beitrags-ID und `updated_at` bzw. Newsletter-Hash). `tools/ghost.py abarbeiten` plant dann zum nächsten freien Termin
  aus `redaktion/fahrplan.md` ein. Ohne passende Freigabe verweigert `ghost.py` (SPERRE).
- **Offen (Entscheidung nötig, siehe aufgaben.md OPS-010):** Antwortet Till nur im Chat bei Head of KMI, sieht der Lauf das nicht.
  Head of KMI trägt deshalb **nie selbst** etwas in `freigaben.jsonl` ein. Bis der Weg geklärt ist: Freigaben per Mail-Antwort oder
  direkt in einer Claude-Sitzung geben.
