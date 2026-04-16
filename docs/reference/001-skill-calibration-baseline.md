# Skill Calibration Baseline

Use this reference when reviewing and rewriting RedTeaPowers skills so the library evolves as one system instead of drifting skill by skill.

## Goal

Calibrate each skill against the current RedTeaPowers operating model:

- light process by default
- batch progress once the mainline is stable
- document creation only when it reduces real confusion
- validation chosen by risk, not by doctrine
- UTF-8 for all document reads and writes

The calibration pass is not a rewrite for rewrite's sake. Change a skill only when the current wording would misroute work, add ceremony, preserve outdated defaults, or make neighboring skills overlap.

## Review Dimensions

Check every skill against these dimensions:

| Dimension | What to confirm |
|-----------|-----------------|
| Trigger clarity | Frontmatter clearly says when to use the skill and when not to use it |
| Boundary fit | The skill has a distinct job and does not silently absorb neighboring skills |
| Process weight | The skill defaults to the lightest useful artifact and does not reintroduce mandatory ceremony |
| Batch behavior | The skill helps batch same-kind work once uncertainty drops instead of preserving tiny loops |
| Validation stance | The skill follows chosen validation strategy and does not smuggle in silent TDD or test-only assumptions |
| Document hygiene | The body is concise enough to load directly, with bulky detail moved into references only when needed |
| Tooling alignment | `agents/openai.yaml`, scripts, and references still match the live skill behavior |
| Completion honesty | The skill asks for fresh evidence before claiming success or handoff readiness |
| Encoding policy | Any document guidance explicitly preserves UTF-8 reads and writes |

## Pass Rules

- Calibrate in batches of neighboring skills, not isolated one-file micro-passes.
- Fix route-breaking inconsistencies first.
- Prefer one meaningful rewrite over several tiny wording-only edits.
- Extract references only when the body is actually getting heavy or repetitive.
- Do not create spec or plan docs for the calibration pass unless the pass itself becomes architecturally ambiguous.

## Recommended Review Order

1. Core routing chain: `using-redteapowers`, `shaping-work`, `researching-and-collecting`, `brainstorming`, `choosing-test-strategy`, `writing-plans`, `executing-plans`
2. Completion and quality gates: `systematic-debugging`, `verification-before-completion`, `finishing-a-development-branch`
3. Documentation layer: `managing-project-docs`, `migrating-project-docs`
4. Collaboration and execution helpers: `subagent-driven-development`, `using-git-worktrees`, `requesting-code-review`, `receiving-code-review`
5. Optional or specialized workflow: `test-driven-development`

## Typical Fix Shapes

Use these fix shapes during calibration:

- tighten frontmatter when triggers are vague or too broad
- remove outdated assumptions such as mandatory spec, mandatory plan, or mandatory tests-pass gates
- align neighboring skills on handoff order
- move lengthy examples into references when the body is doing too much
- rewrite old platform-specific or model-specific wording into RedTeaPowers-native guidance

## Exit Criteria

A skill is calibrated enough for the current pass when:

- its trigger boundary is clear
- its defaults match the modern workflow
- its handoffs are consistent with neighboring skills
- no major outdated assumption remains in the main body
- any touched metadata still matches the body
