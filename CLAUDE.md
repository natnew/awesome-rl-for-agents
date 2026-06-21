# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A public, maintained **awesome list**: *Awesome Reinforcement Learning for Agents*. `README.md` is the
single source of truth — a curated technical index, not an application codebase and not a marketing page.
`data/resources.json` is a machine-readable mirror generated from the README. Most work here is curation,
maintenance, and contribution review, not software development.

## Default operating mode

- Inspect `README.md` (and `data/resources.json` for duplicates) before making any curation decision.
- Make the smallest safe change that satisfies the task; avoid broad rewrites unless explicitly requested.
- Preserve the existing taxonomy — sections, headings, and ordering — unless explicitly asked to change it.
- Prefer a maintainer edit for trivial fixes over creating contributor friction.
- After editing README entries, regenerate the index (`python scripts/build_index.py`) in the same change.

## Scope: what belongs

Entries must be **directly relevant to reinforcement learning applied to agents**:

- LLM agents, tool/API use, multi-agent systems, embodied agents where policy learning or reward feedback is central.
- Infrastructure that primarily supports those settings (trainers, rollout services, environments, verifiers).
- Canonical sources: arXiv `/abs/` pages, ACL Anthology, official project pages, canonical GitHub repositories,
  datasets, durable docs.

## Scope: what does not belong

- Generic deep-RL resources with no clear agent connection (point to general RL lists instead).
- Thin wrapper pages, landing pages, or low-signal tools when a primary source exists.
- Affiliate links, referral trackers, shortened URLs, or PDF-only links without a readable summary.
- Duplicate listings of the same work (link the canonical paper *or* repo once; mention the other in the same bullet).
- Promotional, sales-led, or unsupported-claim entries.

## Awesome-list quality standards

- Prefer relevance, durability, technical substance, source quality, and clear categorisation.
- Prefer official sources, papers, repositories, datasets, and durable project pages over thin wrappers.
- Remove or neutralise promotional, time-sensitive ("new", "latest"), ranking ("best", "#1"), pricing,
  and unsupported claims.
- Preserve the existing taxonomy unless a structural improvement is clearly justified (discuss via a
  taxonomy issue before large reorganisations).

## README formatting rules

- Each entry is a single bullet:
  ```markdown
  - **[Title or project name](https://example.com/path)** — One concise sentence on what it is and why it matters for RL-for-agents readers.
  ```
- Use the em dash (`—`) between link and description; the build script also accepts a hyphen.
- Keep a sensible within-section order (chronological for tightly related benchmarks, otherwise alphabetical —
  match the surrounding list).
- The entry-count marker `<!--entry-count-->N<!--/entry-count-->` in the intro is filled by the build script;
  never hand-edit the number.
- Contents links must resolve to a heading anchor (lowercased, punctuation stripped, spaces → hyphens).

## Protected public-facing areas

Edit these only when the maintainer explicitly asks, or when the requested task directly requires it:

- Badges and the badge row.
- The entry-count marker (it is generated — see Maintenance).
- The Contents structure and major taxonomy headings.
- The "Related awesome lists" structure.
- Contributor-facing banners or images (`assets/`).
- Broad project positioning text (the intro, the "How this list is organised" framing, the disclaimer).

Adding an entry under an existing heading is normal curation, not a structural change.

## Link quality rules

- Confirm links resolve (no 404). For arXiv, prefer `/abs/` over PDF-only links.
- Use the canonical destination — no shortened, referral, or affiliate links.
- A flaky-but-valid host can be added to `.lycheeignore` rather than removed.

## Neutral description style

- One factual sentence: what the resource *is*, naming the RL signal or interaction loop it concerns
  (environment, reward, trajectory, tool-use, multi-agent, embodied policy).
- No superlatives, endorsements, or marketing language. Match the wording conventions of the surrounding list.

## Examples

Acceptable — canonical source, clear RL-for-agents connection, neutral one-liner, fits a Core section:

```markdown
- **[ExampleBench](https://arxiv.org/abs/2401.00000)** — Benchmark of multi-step tool-use tasks with environment-returned reward, for evaluating agent policies.
```

Weak — promotional wording, marketing/non-canonical link, unclear RL connection. Request a canonical source and a
neutral description, or close if the connection cannot be established:

```markdown
- **[BestAgentKit 🚀](https://bestagentkit.example.com/pricing)** — The #1 all-in-one platform to ship powerful AI agents fast.
```

## Section placement

Core (the RL-for-agents loop): Environments & Benchmarks · Rollouts, trajectories and credit assignment ·
Datasets & trajectory corpora · Verifiable Rewards & Reward Design · Tool-use and API-agent RL ·
Training systems and infrastructure.

Adjacent & background: Foundations: RL, agents and interaction loops · RL for reasoning agents ·
RLHF, RLAIF and preference optimisation for agent backbones · Multi-agent reinforcement learning ·
Embodied and physical agents · Evaluation, safety and control.

On-ramp: Surveys & reading paths (a reading path; prefer placing the resource itself in a Core/Adjacent section).

- Place each item under the **most specific** existing section.
- Core covers the loop directly; Adjacent covers foundations and neighbouring fields that inform agent policies.
- If nothing fits, open a taxonomy issue before adding a new section.

## Duplicate checking

Before adding or accepting an entry, check it is not already listed:

- Search the README and `data/resources.json` for the title, the URL, and the arXiv ID / repo slug.
- A paper and its repo are the same work — list once, cross-reference in the bullet if useful.

## Maintenance commands

- Regenerate the index and entry count: `python scripts/build_index.py`
- CI parity check (fails if README and index drift): `python scripts/build_index.py --check`

`scripts/build_index.py` parses curated bullets, stops at "Related awesome lists" (those are pointers, not
counted), writes `data/resources.json`, and fills the entry-count marker.

**Generated files.** `data/resources.json` and the entry-count marker are generated, not authored.

- Do not edit `data/resources.json` by hand.
- Update it only by running `python scripts/build_index.py`.
- Commit it alongside `README.md`, and only when entry changes require regeneration.

## CI workflows

- **Index** (`.github/workflows/index.yml`) — runs `build_index.py --check`; keeps README and JSON in sync.
- **Links** (`.github/workflows/links.yml`) — lychee link check on `**/*.md`; weekly cron plus on change.
- **Labels** (`.github/workflows/labels.yml`) — syncs `.github/labels.yml` (skip-delete).

A README content change that touches entries will fail Index until the index is regenerated.

## PR triage workflow

1. Confirm scope (RL-for-agents) and that the bullet names the RL signal / interaction loop.
2. Check the link is canonical and resolves; check it is not a duplicate.
3. Check placement is the most specific section, and ordering matches the surrounding list.
4. Check the description is neutral and one line.
5. If entries changed, ensure `data/resources.json` and the count were regenerated.

## Issue-to-entry workflow

- **Add a resource** issue → verify scope, link, section, non-duplication → add the bullet → regenerate index.
- **Broken/moved link** issue → update the URL (or remove an irrecoverable entry) → note what was verified → regenerate.
- **New section** (taxonomy) issue → agree the section and candidate entries before any large reorganisation.

## Disposition: accept / edit / request / close / park

- **Accept as-is** when scope, link, placement, and wording all pass.
- **Edit as maintainer** for small safe fixes — wording, casing, em dash, ordering, section move, regenerating
  the index. Prefer this over bouncing a PR back for trivial changes.
- **Request changes** only when needed: off-scope risk, non-canonical link, duplicate uncertainty, or a missing
  rationale that the maintainer cannot resolve.
- **Close** when the entry weakens the list (off-scope, promotional, thin wrapper, unfixable duplicate) — with a
  brief reason.
- **Park** (label, leave open) when the idea is plausible but needs discussion, e.g. a proposed new section.

## Contributor communication

- Warm, concise, respectful, low-friction. Thank contributors; explain decisions briefly.
- When requesting changes, be specific and minimal — say exactly what would make the entry mergeable.

## Documentation conventions

- Keep public-facing text calm, technically precise, and neutral.
- Keep `README.md`, `CONTRIBUTING.md`, and `.github/**` concise and actionable.
- Do not make claims the repository cannot substantiate.

## Git

- Work on a feature branch and open a PR rather than pushing to `main`.
- Run `git status` before committing; do not stage `__pycache__/`, local scratch, or unrelated files.
- Keep documentation/curation commits focused; do not bundle unrelated changes.
