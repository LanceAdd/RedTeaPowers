# Skill Calibration Matrix

Use this matrix to track the current calibration state of the active RedTeaPowers skills.

## Status Labels

- `Aligned`: no immediate rewrite pressure; review only if a neighboring change demands it
- `Touch now`: high-impact inconsistency or drift that should be corrected in the current calibration wave
- `Rewrite next`: still valuable, but the body or defaults need a deliberate cleanup pass soon

## Matrix

| Skill | Current role | Main calibration focus | Status |
|-------|--------------|------------------------|--------|
| `using-redteapowers` | entry router | keep routing order consistent with validation-first and light-process rules | `Aligned` |
| `shaping-work` | route selector | preserve anti-fragmentation defaults and opened-topic stabilization rules | `Aligned` |
| `researching-and-collecting` | factual discovery and synthesis | gather evidence and normalize findings before design or execution | `Aligned` |
| `brainstorming` | design before implementation | keep collaborative design conditional instead of default ceremony | `Aligned` |
| `choosing-test-strategy` | validation router | remain the source of truth for non-dogmatic validation choice | `Aligned` |
| `writing-plans` | formal execution artifact writer | protect checklist-vs-plan boundary and keep validation explicit | `Aligned` |
| `executing-plans` | inline execution from plan or checklist | keep completion verification and branch-closeout handoffs consistent | `Aligned` |
| `systematic-debugging` | evidence-first debugging workflow | keep the body lean while preserving the evidence-first core and specialized references | `Aligned` |
| `verification-before-completion` | final evidence gate | keep completion claims strategy-neutral and consistently referenced from closing flows | `Aligned` |
| `finishing-a-development-branch` | branch integration and cleanup | keep branch closeout dependent on verified evidence instead of test-only assumptions | `Aligned` |
| `managing-project-docs` | document taxonomy controller | keep doc creation deliberate and apply the same standards to this repo's own docs | `Aligned` |
| `migrating-project-docs` | legacy-doc conversion workflow | keep migration batch-oriented and watch for further body growth | `Aligned` |
| `subagent-driven-development` | delegated same-session execution | keep delegated batching strong without creating review churn | `Aligned` |
| `using-git-worktrees` | isolated workspace setup | keep isolation conditional, safe, and repository-aware | `Aligned` |
| `requesting-code-review` | outgoing review request workflow | keep review requests batch-aware, scoped, and evidence-backed | `Aligned` |
| `receiving-code-review` | incoming feedback handling | keep feedback handling technical, deliberate, and non-performative | `Aligned` |
| `test-driven-development` | optional TDD execution mode | keep it specialized and prevent it from leaking back into default routing | `Aligned` |

## Current State

The active package is now calibrated to the current RedTeaPowers operating model.

Future calibration should be usage-driven:

- revise a skill only when real use reveals routing drift, unnecessary ceremony, or reference bloat
- keep `agents/openai.yaml` aligned whenever a skill body changes materially
- rerun a focused calibration pass before adding new top-level skills or major workflow branches
