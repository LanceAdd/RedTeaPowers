# Skill Calibration Backlog

**Goal:** bring the current RedTeaPowers skill set back into one consistent operating model without reintroducing spec-heavy or micro-slice-heavy process.

**Current focus:** final metadata, cross-reference, and package-consistency sweep.

**Prerequisites before each batch:**
- read the touched skill bodies, not only their frontmatter
- compare neighboring handoffs before rewriting
- preserve UTF-8 for every documentation edit
- update `agents/openai.yaml` when the user-facing behavior changes materially

## Batch 1: Core route and closeout consistency

- [x] establish calibration baseline and matrix
- [x] align onboarding flow with validation-first planning rules
- [x] reinsert `verification-before-completion` into execution handoffs
- [x] rewrite `finishing-a-development-branch` away from test-only assumptions

## Batch 2: Debugging and review helpers

- [x] slim `systematic-debugging` without weakening its evidence-first core
- [x] rewrite `requesting-code-review` into a current RedTeaPowers review-request skill
- [x] rewrite `receiving-code-review` to remove legacy model-specific baggage

## Batch 3: Workspace and support skill cleanup

- [x] modernize `using-git-worktrees`
- [x] recheck `subagent-driven-development` after review-skill rewrites
- [x] verify metadata alignment for touched support skills

## Batch 4: Final consistency sweep

- [x] scan all `agents/openai.yaml` files for stale prompts
- [x] recheck cross-references after all rewrites
- [x] run package validation on every touched skill
- [x] decide whether any long bodies still deserve reference extraction

**Current decision:** no additional reference extraction is immediately required for the active package. Revisit only if future usage shows a specific skill body growing heavy again.
