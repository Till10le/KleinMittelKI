# Routinen der KMK-Redaktion

Routinen sind geplante Claude-Code-Läufe in der Cloud. Sie laufen, auch wenn Tills Rechner aus ist.
Anlegen unter claude.ai/code/routines → **New routine**. Repo jeweils `Till10le/KleinMittelKI`.

Der Prompt jeder Routine ist bewusst kurz: Die eigentlichen Regeln stehen in `CLAUDE.md`, den Skills und
`.claude/agents/chefredakteur.md`. So ändern wir das Verhalten im Repo, nicht in der Routine.

## Reihenfolge beim Einschalten

1. Erst **Ghost-Lauf** einmal mit „Run now“ testen (nur lesen: Verbindung und Index).
2. Dann **Redaktions-Lauf** zwei Wochen werktags laufen lassen, Ergebnisse gemeinsam ansehen.
3. Danach **Sonntags-Lauf** dazunehmen.
Social und Analyst folgen in Etappe 4.

## 1. Redaktions-Lauf

- **Umgebung:** KMK-Recherche (Network access: Full, keine Variablen)
- **Zeitplan:** werktags 6:47 Uhr
- **Connectors:** keine
- **Prompt:**

```
Du bist der Chefredakteur der KMK-Redaktion. Lies .claude/agents/chefredakteur.md und führe den
„Redaktions-Lauf“ aus. Arbeite auf main (vorher git pull --rebase, am Ende commit und push).
Veröffentliche nichts und sprich Ghost nicht an. Wenn nichts zu tun ist, schreib das in einer Zeile in den Tagesbericht.
```

## 2. Ghost-Lauf

- **Umgebung:** KMK-Ghost (Network access: Custom mit klein-mittel-ki.ghost.io und www.kleinmittelki.de,
  Variablen GHOST_URL und GHOST_ADMIN_API_KEY)
- **Zeitplan:** werktags 7:47 Uhr
- **Connectors:** optional Gmail, damit die Nachricht an Till zusätzlich per Mail kommt
- **Prompt:**

```
Du bist der Chefredakteur der KMK-Redaktion. Lies .claude/agents/chefredakteur.md und führe den
„Ghost-Lauf“ aus. Arbeite auf main (vorher git pull --rebase, am Ende commit und push).
Beende den Lauf mit der Nachricht an Till aus der Anleitung. Veröffentliche in diesem Lauf nichts:
Freigaben gibt Till, indem er in dieser Sitzung antwortet.
```

## 3. Sonntags-Lauf

- **Umgebung:** KMK-Recherche
- **Zeitplan:** sonntags 17:47 Uhr
- **Prompt:**

```
Du bist der Chefredakteur der KMK-Redaktion. Lies .claude/agents/chefredakteur.md und führe den
„Sonntags-Lauf“ aus (Ideen, Newsletter-Entwurf für Dienstag, Wochenbericht). Arbeite auf main.
Den Newsletter nur als beitrag.md vorbereiten; angelegt wird er im nächsten Ghost-Lauf. Veröffentliche nichts.
```

## Wie Till freigibt

Jeder Lauf ist eine Sitzung, die in der Claude-App unter Code erscheint. Till öffnet die Sitzung des Ghost-Laufs
und antwortet, z. B.:

> 1 ja, meine Einschätzung: … · 2 nein, zu technisch · 3 veröffentlichen

Der Chefredakteur trägt das ein, veröffentlicht Punkt 3 über die Freigabe-Sperre und meldet den Link zurück.
Freigaben zum Veröffentlichen nur in Sitzungen der Umgebung „KMK-Ghost“.

## Sicherheit

- Ghost-Schlüssel nur in „KMK-Ghost“. Diese Umgebung erreicht nur den Blog, kein offenes Internet.
- `tools/sperre.py` blockiert direkte Ghost-Aufrufe, Änderungen an der Sperre und Löschen im Gedächtnis.
- `tools/ghost.py publish` veröffentlicht nur mit einer Freigabe, die zum aktuellen Stand des Beitrags passt.
- Ehrlich: Die Sperre ist eine feste Regel im Code, keine kryptografische Sicherung. Ein Agent, der alle Regeln
  ignoriert, könnte sie theoretisch umgehen. Deshalb veröffentlichen Routinen nie selbständig; das passiert nur in
  einer Sitzung, in der Till selbst geantwortet hat.
