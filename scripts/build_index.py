#!/usr/bin/env python3
"""Build a machine-readable index from README.md.

The README is the single source of truth. This script parses its curated
sections into data/resources.json and fills the entry-count marker in the
README, so the human-readable list and the machine index never drift.

Usage:
    python scripts/build_index.py            # regenerate data/resources.json and update the count
    python scripts/build_index.py --check    # exit non-zero if anything would change (used in CI)

Curated entries are bullets of the form:
    - **[Title](url)** — description

Entries under "Related awesome lists" are pointers to other lists, not curated
resources, so they are excluded from the index and the count.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
INDEX = ROOT / "data" / "resources.json"

ENTRY_RE = re.compile(r"^- \*\*\[(?P<title>.+?)\]\((?P<url>[^)]+)\)\*\*\s+[—-]+\s+(?P<desc>.+)$")
H2_RE = re.compile(r"^## (?P<title>.+?)\s*$")
COUNT_RE = re.compile(r"(<!--entry-count-->)(.*?)(<!--/entry-count-->)", re.DOTALL)

# Sections after this heading are pointers to other lists, not curated resources.
STOP_SECTION = "Related awesome lists"


def parse(readme_text: str) -> list[dict]:
    tier = None
    section = None
    records: list[dict] = []

    for line in readme_text.splitlines():
        if line.startswith("**Core "):
            tier = "core"
            continue
        if line.startswith("**Adjacent & background."):
            tier = "adjacent"
            continue

        h2 = H2_RE.match(line)
        if h2:
            section = h2.group("title")
            if section == STOP_SECTION:
                break  # everything below is related lists / footer
            continue

        m = ENTRY_RE.match(line)
        if m and section is not None:
            records.append(
                {
                    "title": m.group("title"),
                    "url": m.group("url"),
                    "section": section,
                    "tier": tier or "other",
                    "description": m.group("desc").strip(),
                }
            )

    return records


def render_index(records: list[dict]) -> str:
    payload = {"count": len(records), "resources": records}
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def update_count(readme_text: str, count: int) -> str:
    if not COUNT_RE.search(readme_text):
        raise SystemExit("entry-count marker not found in README.md")
    return COUNT_RE.sub(rf"\g<1>{count}\g<3>", readme_text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if outputs would change")
    args = parser.parse_args()

    readme_text = README.read_text(encoding="utf-8")
    records = parse(readme_text)
    index_text = render_index(records)
    new_readme = update_count(readme_text, len(records))

    if args.check:
        stale = []
        if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != index_text:
            stale.append("data/resources.json")
        if new_readme != readme_text:
            stale.append("README.md entry count")
        if stale:
            print("Out of date: " + ", ".join(stale))
            print("Run: python scripts/build_index.py")
            return 1
        print(f"Index up to date ({len(records)} entries).")
        return 0

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(index_text, encoding="utf-8")
    if new_readme != readme_text:
        README.write_text(new_readme, encoding="utf-8")
    print(f"Wrote {INDEX.relative_to(ROOT)} and set entry count to {len(records)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
