# Contributing

Thank you for helping keep **Awesome Reinforcement Learning for Agents** accurate and useful. This document explains what belongs in the list and how to propose changes.

## Code of conduct

All participants must follow the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Unprofessional or harassing behavior is not acceptable.

## What to add

Entries should be **directly relevant** to reinforcement learning as applied to **agents**: LLM agents, tool and API use, multi-agent systems, embodied agents where policy learning or reward feedback is central, or infrastructure that primarily supports those settings.

Prefer:

- Peer-reviewed papers, strong preprints, or widely used open-source projects with clear documentation.
- **Stable URLs**: arXiv abstract pages (`https://arxiv.org/abs/...`), ACL Anthology, official project pages, or canonical GitHub repositories.
- **Neutral, factual one-line descriptions** (what the resource is), not marketing superlatives.

Avoid:

- Paywalled-only links without a freely readable summary or preprint.
- Duplicate listings of the same work (link the canonical paper *or* repo once; you may mention the other in the same bullet).
- Purely generic deep RL resources with no clear connection to agents (those belong in general RL lists; see [README.md](README.md#related-awesome-lists)).
- Affiliate links, referral trackers, or shortened URLs that hide the destination.

## Pull request format

1. **Placement**: Add the item under the most specific existing section in [README.md](README.md). If nothing fits, open an issue to discuss a new section before large reorganizations.

   README taxonomy (pick one primary section per item):

   - Foundations: RL, agents and interaction loops
   - Agent environments and task worlds
   - Rollouts, trajectories and credit assignment
   - Tool-use and API-agent RL
   - Verifiable rewards and reward engineering
   - RL for reasoning agents
   - RLHF, RLAIF and preference optimisation for agent backbones
   - Multi-agent reinforcement learning
   - Embodied and physical agents
   - Training systems and infrastructure
   - Evaluation, safety and governance
2. **Markdown style**: Use a single bullet in this form:

   ```markdown
   - **[Title or project name](https://example.com/path)** — One concise sentence describing the contribution and why it matters for RL-for-agents readers.
   ```

3. **Alphabetical or thematic order**: Within a section, keep a sensible order (often chronological for tightly related benchmarks, or alphabetical by title—match the surrounding list).
4. **Link hygiene**: Confirm links resolve (no 404). For arXiv, prefer `/abs/` over PDF-only links so readers see metadata.

## Dead or moved links

If you find a broken link, PRs that **update** the URL or **remove** an irrecoverable entry are welcome. Briefly note in the PR description what you verified (e.g., new arXiv ID, repository rename).

## Maintainer discretion

Maintainers may decline additions that are off-scope, redundant, or insufficiently documented, or may edit wording for consistency.

---

## Repository metadata checklist (after you create the GitHub repo)

Copy these into the GitHub repository **About** settings when you publish:

| Field | Suggested value |
|-------|-----------------|
| **Description** | Curated papers, benchmarks, and tools for reinforcement learning in LLM, tool-use, multi-agent, and embodied agents. |
| **Website** | (optional) Link to a project page if you add one later. |
| **Topics** | `reinforcement-learning`, `llm-agents`, `tool-use`, `multi-agent-systems`, `rlhf`, `benchmarks`, `awesome-list`, `machine-learning`, `large-language-models` |

**Features:** Enable **Issues** if you want community suggestions; disable **Wiki** unless you plan to maintain it.

### Optional: Awesome list compliance

If you intend to submit this list to [sindresorhus/awesome](https://github.com/sindresorhus/awesome), read their [pull request requirements](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) first. The README includes the [Awesome](https://awesome.re) badge; remove or retain it according to whether you meet their criteria at submission time.
