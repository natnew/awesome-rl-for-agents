# AGENTS.md

Operating protocol for AI coding agents working in this repository.

Claude Code should read `CLAUDE.md` first, then use this file as the shared repository contract. Other agents should start here. Follow repository-local guidance over generic awesome-list assumptions.

## Repository North Star

This is a public, maintained awesome list: *Awesome Reinforcement Learning for Agents*. The `README.md` is the product: a durable, high-signal, navigable map of reinforcement learning applied to agents — environments, rollouts, credit assignment, reward design, tool-use learning, multi-agent RL, embodied agents, and the post-training methods that power agentic behaviour.

`data/resources.json` is a machine-readable mirror generated from the README by `scripts/build_index.py`. It is not authored by hand.

The list is curated, not accumulated. Each entry should help a reader understand the RL-for-agents loop, find a credible primary source, or compare related work. Selectivity, durability, clear placement, and neutral description quality matter more than volume.

## Agent Role

Agents may help with:

* README maintenance when explicitly asked
* New entry review
* Pull request review
* Issue triage
* Broken-link checks
* Duplicate detection
* Section placement
* Description tightening
* Maintainer comment drafts
* Regenerating the index after an entry change (`python scripts/build_index.py`)
* Small, safe cleanup edits when explicitly requested

Agents must not:

* Add speculative, off-scope, or low-signal entries
* Inflate claims or preserve promotional wording
* Reorganise the taxonomy without explicit instruction
* Run broad formatting sweeps
* Edit unrelated files
* Hand-edit `data/resources.json` or the entry-count marker
* Rewrite the maintainer's style unnecessarily
* Turn one contribution into a broad structural change
* Touch protected areas unless explicitly instructed

## Read Order

Before reviewing or editing, read in this order:

1. `README.md` — scope, taxonomy, formatting, protected areas, and existing examples
2. `CONTRIBUTING.md` — submission requirements and entry format
3. `.github/ISSUE_TEMPLATE/` — `add-resource.yml`, `broken-link.yml`, `new-section.yml` for contributor expectations
4. `.github/PULL_REQUEST_TEMPLATE.md` — the merge checklist applied to every PR
5. `CLAUDE.md` — repository operating mode and maintenance commands
6. `data/resources.json` — for duplicate detection only (generated; never edit directly)
7. Recent issues and merged PRs, where available, for maintainer precedent

Do not assume the generic awesome-list pattern overrides this repository's existing structure.

## Repository Facts

* `README.md` contains the intro, the entry-count marker, a Contents map, the curated sections, and a "Related awesome lists" pointer block.
* The taxonomy is grouped: **On-ramp** (Surveys & reading paths), **Core — the RL-for-agents loop**, and **Adjacent & background**. See Section Placement Rules.
* Each entry is a single bullet. Some sections carry explanatory text or a small summary block (for example "reward signal types") before the bullets — preserve it.
* The entry-count marker `<!--entry-count-->N<!--/entry-count-->` in the intro is filled by `scripts/build_index.py`. Never hand-edit the number.
* `scripts/build_index.py` parses curated bullets, stops at "Related awesome lists" (those are pointers, not counted), writes `data/resources.json`, and fills the count. Run it after any entry change.
* CI parity check: `python scripts/build_index.py --check` — the **Index** workflow fails if README and JSON drift.
* `CONTRIBUTING.md` asks for focused PRs — one resource (or one tightly related group) per PR.
* New entries go under the **most specific** existing section, in the surrounding section's order (often chronological for tightly related benchmarks, otherwise alphabetical by title).
* New sections or taxonomy changes are handled separately, via a `new-section` issue, before any large reorganisation.
* For a work that exists as both a paper and a repository, list it once and cross-reference the other in the same bullet.

## Scope Rules

Entries must be directly relevant to reinforcement learning applied to agents.

Belongs:

* LLM agents, tool/API use, multi-agent systems, and embodied agents where policy learning or reward feedback is central
* Environments, benchmarks, and task worlds that produce reward or verification signals
* Rollout, trajectory, and credit-assignment methods
* Datasets and trajectory corpora
* Verifiable rewards and reward-design resources
* Tool-use and API-agent RL
* Training systems and infrastructure (trainers, rollout services, verifiers) that primarily support these settings
* Foundations and adjacent fields that train or inform agent policies (classical MARL, robotics, preference optimisation for backbones)
* Canonical sources: arXiv `/abs/` pages, ACL Anthology, official project pages, canonical GitHub repositories, datasets, and durable docs

Does not belong:

* Generic deep-RL resources with no clear agent connection (point to general RL lists instead)
* Thin wrapper pages, landing pages, or low-signal tools when a primary source exists
* Broken or inaccessible links
* Duplicate or near-duplicate resources, including a paper and its repo listed twice
* Affiliate links, referral trackers, shortened URLs, or PDF-only links without a readable summary
* Promotional, sales-led, or unsupported-claim entries
* Ranking, pricing, or time-sensitive claims such as "new", "latest", "best", "#1", "fastest", or "most advanced"

## Quality Bar

An entry qualifies when all are true:

* It is directly relevant to reinforcement learning for agents, and the bullet names the RL signal or interaction loop it concerns (environment, reward, trajectory, tool-use, multi-agent, embodied policy).
* The source is canonical, credible, and useful to a technical reader.
* The link is canonical, durable, and resolves (no 404; arXiv `/abs/` over PDF-only).
* The resource adds something distinct from existing entries.
* It fits an existing section without forcing a taxonomy change.
* The description is one neutral, factual sentence in the surrounding section's wording conventions.
* No duplicate or stronger existing equivalent is already present.

## README Formatting Rules

Infer format from the surrounding section before editing.

* Preserve the heading structure, anchors, and Contents links (anchors are lowercased, punctuation stripped, spaces → hyphens).
* Preserve badges, the badge row, intro framing, the entry-count marker, summary blocks, and the "Related awesome lists" structure.
* Each entry is a single bullet in this form:

  ```markdown
  - **[Title or project name](https://example.com/path)** — One concise sentence on what it is and why it matters for RL-for-agents readers.
  ```

* Use the em dash (`—`) between link and description; the build script also accepts a hyphen.
* Use HTTPS and canonical names.
* Keep the description to one factual sentence; match the surrounding wording conventions.
* Do not use marketing superlatives or title case for descriptions.
* Do not perform broad formatting changes unless explicitly asked.
* After any entry change, regenerate the index in the same change: `python scripts/build_index.py`.

## Link Quality Rules

Verify that:

* The link resolves (no 404).
* The link points to the canonical source — arXiv `/abs/`, ACL Anthology, an official project page, or the canonical GitHub repository.
* Repository links point to the main project, not an arbitrary fork.
* Paper links prefer the abstract/metadata page over a PDF-only link.
* Dataset links prefer the official dataset page or a maintained repository.
* URLs carry no avoidable tracking, referral, or affiliate parameters, and are not shortened.
* A flaky-but-valid host can be added to `.lycheeignore` rather than removed.

## Description Style

One factual sentence: what the resource *is*, naming the RL signal or interaction loop it concerns.

Descriptions should be:

* Neutral
* Factual
* Specific
* Short
* Free of hype and unsupported claims
* Useful to a reader scanning the list quickly

Prefer:

* "Benchmark of multi-step tool-use tasks with environment-returned reward, for evaluating agent policies."
* "Framework for training LLM agents across diverse interactive environments with trajectory data."
* "Offline control as conditional trajectory modelling, with sequence-level credit assignment."

Avoid:

* "Powerful", "revolutionary", "cutting-edge", "state-of-the-art"
* "Best", "latest", "new", "#1", "industry-leading", "fastest"
* Unsupported claims about performance, adoption, or maturity

## Section Placement Rules

The taxonomy (preserve exactly unless explicitly asked to change it):

**On-ramp**

* Surveys & reading paths — a reading path through the list; prefer placing the resource itself in a Core or Adjacent section.

**Core — the RL-for-agents loop**

* Environments & Benchmarks
* Rollouts, trajectories and credit assignment
* Datasets & trajectory corpora
* Verifiable Rewards & Reward Design
* Tool-use and API-agent RL
* Training systems and infrastructure

**Adjacent & background**

* Foundations: RL, agents and interaction loops
* RL for reasoning agents
* RLHF, RLAIF and preference optimisation for agent backbones
* Multi-agent reinforcement learning
* Embodied and physical agents
* Evaluation, safety and control

To place an item:

1. Place each item under the **most specific** existing section.
2. Core covers the loop directly; Adjacent covers foundations and neighbouring fields that inform agent policies.
3. Compare the candidate with neighbouring entries and match the section's order.
4. If two sections fit, choose the one where readers would most naturally look first.
5. Do not create a section for a single item.
6. Do not move many existing entries unless explicitly asked.
7. If placement is uncertain, state the trade-off and recommend one option.
8. If nothing fits, open a `new-section` (taxonomy) issue before adding a section.

## Duplicate Checking Rules

Before adding or approving, search the README and `data/resources.json` for:

* The same URL
* The same project under a different URL
* The same paper title, or its arXiv ID / repo slug
* A paper and its repository (the same work — list once, cross-reference in the bullet)
* A renamed repository
* An existing entry in a nearby section
* An existing issue or PR suggesting the same resource
* A stronger canonical source already listed

If a duplicate exists, recommend closing, editing, or cross-referencing rather than adding another entry.

## Decision Matrix

| Decision           | Use when                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Accept as-is       | In scope, canonical link, correct placement, matching format, neutral one-line description, no duplicate. |
| Edit as maintainer | Strong resource needing small fixes: wording, casing, em dash, canonical URL, placement, or regenerating the index. Prefer this over bouncing a trivial PR. |
| Request changes    | Off-scope risk, non-canonical link, duplicate uncertainty, or a missing rationale the maintainer cannot resolve. |
| Close              | Off-scope, promotional, thin wrapper, duplicate, or broken with no durable replacement.                   |
| Park               | Plausible but needs discussion — for example a proposed new section. Label and leave open.                |

## Issue-to-Entry Workflow

For **add-resource** issues:

1. Check scope (RL-for-agents) and that the bullet names the RL signal / interaction loop.
2. Check the source is canonical and the link resolves.
3. Check for duplicates across README and `data/resources.json`.
4. Identify the most specific section.
5. Draft a neutral one-line entry only if the resource qualifies.
6. Add the bullet, then regenerate the index (`python scripts/build_index.py`).
7. Recommend accept, maintainer edit, request changes, close, or park, with a concise comment.

For **broken-link** issues:

1. Verify the reported link.
2. Search for a canonical replacement (new arXiv ID, repository rename, official mirror).
3. Prefer official replacements over mirrors.
4. Update the URL and note what was verified; remove the entry only when no credible replacement exists.
5. Regenerate the index if the entry set changed.

For **new-section** (taxonomy) issues:

* Agree the section and candidate entries before any large reorganisation.

## Pull Request Review Workflow

1. Read the PR title, description, and diff.
2. Confirm it changes only relevant files and is focused (one resource or one tightly related group).
3. Check each added or changed link is canonical and resolves.
4. Check scope and that the bullet names the RL signal / interaction loop.
5. Check duplicates.
6. Check the section is the most specific one, and ordering matches the surrounding list.
7. Check local formatting (single bullet, em dash, neutral one line).
8. Confirm `data/resources.json` and the entry count were regenerated if entries changed.
9. Decide: accept, maintainer edit, request changes, close, or park.
10. Draft a concise maintainer comment.

Minimise contributor friction. If the resource is clearly suitable and the issue is minor, recommend a maintainer edit rather than asking the contributor to revise.

## Stop and Ask

Stop and ask the maintainer before:

* Creating a new section or changing the taxonomy
* Reordering large parts of the README
* Changing the Contents structure or major headings
* Editing the badge row, the intro, or the "How this list is organised" framing
* Editing the "Related awesome lists" structure
* Changing contribution rules
* Removing multiple entries
* Making judgement-heavy scope changes
* Editing files unrelated to the stated task

## Protected Areas

Edit these only when the maintainer explicitly asks, or when the task directly requires it:

* Badges and the badge row
* The entry-count marker (it is generated — regenerate, do not hand-edit)
* `data/resources.json` (generated — update only by running the build script)
* The Contents structure and major taxonomy headings
* The "Related awesome lists" structure
* The intro, the "How this list is organised" framing, and any disclaimer
* Contributor-facing banners or images (`assets/`)
* Licence text and unrelated repository metadata
* Private, local, scratch, or draft files

Adding an entry under an existing heading is normal curation, not a structural change.

## Maintainer Comment Style

Comments should be warm, concise, respectful, and decision-oriented. Thank contributors and explain decisions briefly.

Prefer:

* "Thank you for the suggestion. This is in scope and the link is canonical; I would place it under Tool-use and API-agent RL with a shorter neutral description."
* "Thank you — useful resource. I would accept this with a small maintainer edit to drop the ranking claim."
* "Thank you for raising this. I would close it as a duplicate; the work already appears under Environments & Benchmarks."
* "Thank you — I would park this until we agree a section for it in a taxonomy issue."

Avoid:

* Long explanations
* Harsh or defensive wording
* Asking contributors for trivial edits the maintainer can safely make

## Final Response Pattern

When finishing a task, summarise:

* What was reviewed
* Decision or recommended decision
* What changed, if anything (including whether the index was regenerated)
* Any risks or uncertainties
* Suggested maintainer comment, if relevant
* Follow-up needed, if any

Do not modify `README.md`, `data/resources.json`, or other files unless explicitly asked.
