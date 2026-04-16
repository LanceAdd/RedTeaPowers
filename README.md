# RedTeaPowers

RedTeaPowers is a curated skill package for structured software work with lighter process by default.

It is designed around a few core ideas:

- shape the work before forcing process
- choose documentation deliberately instead of defaulting to spec and plan
- choose a validation strategy before implementation instead of defaulting to TDD
- keep all project documents in UTF-8

## Included Skills

- `using-redteapowers`
- `shaping-work`
- `choosing-test-strategy`
- `managing-project-docs`
- `brainstorming`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `systematic-debugging`
- `verification-before-completion`
- `using-git-worktrees`
- `requesting-code-review`
- `receiving-code-review`
- `finishing-a-development-branch`
- `test-driven-development`

## Package Notes

- This package is the clean active cut of the library.
- Historical or experimental material is intentionally left out of the default package.
- Documentation should be read and written as UTF-8 text.

## Key Entry Points

- Start with `using-redteapowers` for workflow routing.
- Use `shaping-work` to decide between direct execution, checklist, plan, or spec plus plan.
- Use `choosing-test-strategy` before locking in testing or verification.
- Use `managing-project-docs` to choose the right document type and numbering scheme.

## Repository Layout

- `PACKAGE.md` describes the packaged skill set.
- Each top-level directory is a skill.
- `agents/openai.yaml` provides UI-facing metadata where present.
- `references/` holds load-on-demand guidance.
- `scripts/` holds helper scripts when a skill needs them.
