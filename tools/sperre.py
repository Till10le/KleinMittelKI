#!/usr/bin/env python3
"""PreToolUse-Hook der KMK-Redaktion: blockiert Wege an der Freigabe-Sperre vorbei.

Blockiert (Exit-Code 2):
- direkte Aufrufe der Ghost Admin API außerhalb von tools/ghost.py (curl, eigener Code)
- Änderungen an redaktion/freigaben.jsonl, tools/ghost.py, tools/sperre.py, .claude/settings.json
  (Freigaben entstehen nur über `python3 tools/ghost.py freigabe`)
- Löschen von Dateien im Gedächtnis (redaktion/) oder von Entwürfen
"""
import json
import re
import sys

GESCHUETZT = ("redaktion/freigaben.jsonl", "tools/ghost.py", "tools/sperre.py", "tools/mailfreigabe.py",
              ".claude/settings.json")


def block(grund: str) -> None:
    print(f"SPERRE der KMK-Redaktion: {grund} Wenn das nötig ist, frag Till.", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = str(inp.get("file_path", ""))
        if any(path.endswith(g) for g in GESCHUETZT):
            block(f"{path} ist geschützt.")
        return
    if tool == "Bash":
        cmd = str(inp.get("command", ""))
        if "ghost/api/admin" in cmd or re.search(r"curl[^|;]*ghost\.io", cmd):
            block("Ghost nur über tools/ghost.py ansprechen.")
        if re.search(r"(>|tee|sed -i|truncate|rm )[^|;]*(freigaben\.jsonl|tools/ghost\.py|tools/sperre\.py|"
                     r"tools/mailfreigabe\.py|settings\.json)", cmd):
            block("Geschützte Datei darf nicht per Shell verändert werden.")
        if re.search(r"\brm\b[^|;]*(redaktion/|entwuerfe/)", cmd) or re.search(r"git\s+rm\b", cmd):
            block("Im Gedächtnis und in Entwürfen wird nichts gelöscht.")
        if re.search(r"\bgit\s+push\b[^|;]*(--force|-f\b)", cmd):
            block("Kein Force-Push.")


if __name__ == "__main__":
    main()
