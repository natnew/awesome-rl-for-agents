# AGENTS.md

Shared operating protocol for *Awesome Reinforcement Learning for Agents*. Claude Code reads `CLAUDE.md` first; other agents start here. Follow repository-local guidance over generic awesome-list conventions.

## Purpose and boundaries

`README.md` is the canonical product: a selective, durable map of reinforcement learning for agents. Prioritise technical usefulness, credible sources, clear placement, and neutral descriptions over volume.

- Review resources, PRs, issues, links, duplicates, and placement; draft entries and maintainer comments as requested.
- Modify files only when asked. A review or suggestion alone does not authorise edits.
- Keep changes focused: one resource or tightly related group per PR. Preserve the maintainer's style; avoid unrelated edits and broad formatting sweeps.
- Never hand-edit `data/resources.json` or the `<!--entry-count-->N<!--/entry-count-->` marker. Both are generated from the README.

## Load only relevant context

Start with the request and working-tree status; preserve existing user changes. Read the relevant issue, PR title/body/diff, or target file, then use this routing:

| Need | Read or search |
| --- | --- |
| Scope, placement, style | `README.md` intro, Contents, target section, and neighbouring entries |
| Submission requirements | `CONTRIBUTING.md` |
| Issue expectations | Matching template in `.github/ISSUE_TEMPLATE/`: `add-resource.yml`, `broken-link.yml`, or `new-section.yml` |
| PR expectations | `.github/PULL_REQUEST_TEMPLATE.md` |
| Operating context | `CLAUDE.md` |
| Duplicates | Search `README.md` and `data/resources.json`; use the JSON only for duplicate detection |
| Unresolved maintainer precedent | Relevant recent issues and merged PRs, where available |

Read each needed source once; expand context only when evidence or uncertainty requires it. Instruction-only edits do not require resource research or duplicate checks.

## Entry review checklist

Before adding or recommending acceptance, check all five:

1. **Scope and value.** Directly relevant to RL for agents: environments and benchmarks with reward or verification signals; rollouts, trajectories, credit assignment, datasets, rewards, tool/API use, training infrastructure, multi-agent or embodied policy learning. Foundations, reasoning, preference optimisation, and safety belong where they inform agent policies within existing Adjacent sections. Reject generic deep RL without an agent connection, speculative additions, thin wrappers, and low-signal resources.
2. **Source and link.** Inspect the source enough to substantiate the description. Use a credible, canonical, durable HTTPS URL that resolves: arXiv `/abs/`, ACL Anthology, official project/docs/dataset page, or main repository rather than a fork. Prefer metadata pages over PDF-only links; avoid paywalled-only sources without a readable summary, broken links, shortened URLs, tracking, and referrals. Report verification limits rather than claiming success.
3. **Distinctness.** Search README and the generated index by title, URL, arXiv ID, repo slug, aliases, and renamed repositories; check relevant issues/PRs for prior suggestions. Check nearby sections and stronger existing equivalents. List a paper and its repository once, cross-referencing the other in the same bullet. For duplicates, recommend closing, editing, or cross-referencing.
4. **Placement.** Choose the most specific existing section from the README Contents and match local ordering (often chronological or alphabetical). Core covers the interaction loop; Adjacent covers foundations and neighbouring fields. On-ramp is a reading path: prefer placing resources in Core or Adjacent. If two sections fit, recommend the more discoverable one and explain uncertainty briefly.
5. **Wording and format.** Use one factual sentence naming the RL signal or interaction loop; match surrounding wording and canonical names. No marketing, rankings, pricing, time-sensitive claims such as "latest", or unsupported performance, adoption, or maturity claims. Avoid title case in descriptions.

Entry format:

```markdown
- **[Title or project name](https://example.com/path)** — One concise sentence naming the RL signal or interaction loop.
```

Use an em dash. Example description: "Benchmark of multi-step tool-use tasks with environment-returned reward, for evaluating agent policies."

## Task workflows

- **Add-resource issue:** Apply the checklist, choose placement, and draft a bullet only if it qualifies. Recommend a decision; apply the entry only when editing is requested.
- **PR review:** Read the title, body, and diff; confirm focused scope, apply the checklist to changed entries, and verify generated-file parity when entries changed. Prefer a small maintainer fix over asking a contributor for trivial revisions.
- **Broken link:** Verify the failure, then seek a canonical replacement (repository rename, new arXiv ID, official mirror). Prefer official sources; remove only if no credible replacement exists and removal is authorised. A flaky but valid host may warrant a targeted `.lycheeignore` exception rather than removal. Record what was verified.
- **Authorised edit:** Make the smallest relevant change, validate as below, and review the final diff for unintended edits.

### Decisions

| Decision | Use when |
| --- | --- |
| Accept as-is | All checklist items pass. |
| Edit as maintainer | Suitable resource needs minor wording, formatting, URL, placement, or index fixes. |
| Request changes | Material scope, source, duplicate, or rationale uncertainty cannot be resolved by the maintainer. |
| Close | Off-scope, promotional, thin wrapper, duplicate, or broken with no durable replacement. |
| Park | Plausible but needs evidence, discussion, or a taxonomy decision. |

These are recommendations during review. Posting comments or changing issue/PR state requires a request to do so.

## Validation

After **any entry change**, including a URL or description edit, run from the repository root:

```sh
python scripts/build_index.py
python scripts/build_index.py --check
```

The generator updates `data/resources.json` and the README count; include both outputs when changed. It stops at "Related awesome lists", whose pointers are not counted. CI's Index workflow runs `--check`.

For instruction-only changes, review the diff and run `git diff --check`; do not regenerate the index unnecessarily. This repository has no application build/lint/test suite. Verify changed resource links when applicable and report checks that could not run.

## Protected changes

Preserve headings, anchors, Contents links, summary blocks, and the existing taxonomy. Adding an entry under an existing heading is normal curation.

Unless already explicitly authorised by the request, ask before:

- Creating sections, changing taxonomy, reordering large parts of the README, removing multiple entries, or making judgement-heavy scope changes.
- Editing badges, intro/framing/disclaimer, Contents or major headings, the "Related awesome lists" structure, contributor-facing assets, licence text, or unrelated repository metadata.
- Changing contribution rules or touching private, local, scratch, or draft files.

Keep unrelated files out of scope. Generated index/count updates required by an authorised entry edit are part of that edit; use the generator, never manual changes.

## Completion and maintainer comments

Report what was reviewed, the decision and brief reason, files changed, validation (including index regeneration when applicable), and any uncertainty or follow-up. Include a suggested entry or maintainer comment only when useful.

Comments should thank the contributor, state the decision, and explain it briefly. Example: "Thank you — this is in scope. I would accept it with a small maintainer edit to tighten the description."
