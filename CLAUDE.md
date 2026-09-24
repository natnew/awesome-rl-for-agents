# CLAUDE.md

Claude-specific operating layer for *Awesome Reinforcement Learning for Agents*. `AGENTS.md` is the shared protocol and the authority on review checklist, decisions, task workflows, and protected changes — read it before any review or edit. This file adds only what Claude needs on top.

## What this repository is

A curated awesome list, not an application. `README.md` is the product; everything else supports it.

| Path | Role |
| --- | --- |
| `README.md` | Canonical list: intro, entry-count marker, Contents, curated sections, "Related awesome lists". |
| `data/resources.json` | Generated mirror of README entries. Never hand-edit. |
| `scripts/build_index.py` | Only tooling: parses README → JSON and fills the count marker. |
| `AGENTS.md` | Checklist, decisions, workflows, validation, protected changes. |
| `CONTRIBUTING.md` | Contributor-facing scope, taxonomy list, entry format. |
| `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md` | Public contribution forms. |
| `.github/workflows/` | `index.yml` (`--check` on README/JSON changes), `links.yml` (lychee on all `*.md`, weekly), `claude.yml` (`@claude` mentions), `labels.yml`. |
| `.lycheeignore` | Hosts exempt from CI link checks. |

There is no build, lint, or test suite. Do not invent one or add dependencies.

## Commands

```sh
python scripts/build_index.py          # after any entry add/remove/edit (URL, title, description)
python scripts/build_index.py --check  # must print "Index up to date (N entries)."
git diff --check                        # always, before finishing
```

Commit regenerated `data/resources.json` and the README count together with the entry change. For instruction-only or non-entry edits, skip regeneration. Lychee is not installed locally; verify changed links with WebFetch and report any you could not verify.

## Parser invariants (easy to break silently)

`build_index.py` reads README line by line. Keep these true or entries vanish from, or leak into, the index:

- An entry is a top-level bullet exactly `- **[Title](url)** — description` (em dash; hyphen tolerated). Indented bullets or other shapes are not indexed.
- URLs must not contain `)` — the regex stops at the first one. Percent-encode it (`%29`).
- Section = nearest `## ` heading. `###` subheadings (e.g. "Reward signal types") do not start a new section; their bullets are unlinked on purpose so they stay uncounted.
- Tier comes from the paragraph lines beginning `**Core ` and `**Adjacent & background.` — do not reword their openings.
- Parsing stops at `## Related awesome lists`; entries below it are pointers, not curated resources.

## Scope and style in one breath

In scope: RL applied to agents — environments with reward/verification signals, rollouts and credit assignment, trajectory data, reward design, tool/API-use RL, training infrastructure; plus Adjacent foundations that inform agent policies. Each description is one neutral sentence naming the RL signal or interaction loop, no hype, rankings, or time-sensitive claims. Place in the most specific existing section, matching local order. Full rules: `AGENTS.md` § Entry review checklist.

## How to work here

- **Edit only when asked.** Reviews, triage, and suggestions are read-only unless the request authorises changes; posting comments or changing issue/PR state also needs an explicit request.
- **`@claude` in GitHub** (`claude.yml`): the triggering issue/PR comment is the request. Read the full issue or PR diff first; keep replies short and use the output format below.
- **Duplicates:** grep `README.md` for title, URL, arXiv ID, and repo slug before anything else; `data/resources.json` mirrors the same data.
- **Smallest change:** one resource (or tightly related group) per change; prefer a maintainer fix over asking a contributor for trivial revisions.
- **Stop and ask** before new sections, taxonomy or Contents changes, large reorders, multi-entry removals, intro/badge/framing edits, or contribution-rule changes (`AGENTS.md` § Protected changes).
- **Parallel work:** worth it only for batch link verification or reviewing several independent submissions; single-entry tasks are faster inline.

## Review output format

For PR or issue review, respond with:

- **Decision**: accept, maintainer edit, request changes, close, or park
- **Reason**: 1–3 bullets
- **Suggested README entry**, if useful
- **Suggested maintainer comment** (thank, decide, explain briefly)
- **Files changed**, and whether the index was regenerated
- **Remaining uncertainty**, including links not verified
