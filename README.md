# RedTeaPowers

[中文说明 / Chinese Version](README.zh-CN.md)

```text
        )   )  (
       (   (   ) )
        )   ) ( (
      ╭───────────╮
      │ RedTea >  │__
      │ Powers    │  )
      ╰───────────╯__/
```

RedTeaPowers is a curated skill library for structured software work that keeps useful discipline while stripping out process drag.

It was rebuilt from the original `superpowers` ecosystem for teams who still want structure, but do not want to pay for it with slow momentum, endless micro-loops, or document sprawl.

## Why RedTeaPowers

Many process-heavy development systems fail in the same predictable ways:

- too much convergence before implementation
- too many mandatory `spec` and `plan` artifacts
- too many one-problem-one-loop passes
- silent TDD pressure where other validation would fit better
- weak document taxonomy that pushes everything into the same buckets

RedTeaPowers keeps the useful parts:

- work shaping before blind execution
- explicit validation choices
- durable documentation when it is genuinely valuable
- repeatable execution and completion workflows

and changes the defaults that usually slow teams down.

## What It Optimizes For

RedTeaPowers is designed for:

- lighter process by default
- faster batch delivery after the mainline stabilizes
- evidence before claims
- documentation with clear purpose
- UTF-8 consistency across project documents

## Core Defaults

1. Start with the lightest workflow that preserves clarity and safety.
2. Shape the work before producing process artifacts.
3. When 3 or more same-kind low-risk items are visible, batch them by default.
4. Use a thin first slice only to open uncertainty, then move into meaningful batch progress.
5. Choose validation by real risk, not by habit.
6. Read and write all project documents as UTF-8 text.

## Workflow At A Glance

```text
route -> research if facts are missing -> design only if needed -> plan only if needed -> execute -> verify -> finish
```

Recommended entry points:

1. `using-redteapowers` for top-level routing
2. `shaping-work` to choose direct execution, session task tracking, plan, or spec-plus-plan
3. `researching-and-collecting` when the next blocker is missing facts, inventory, or comparison work
4. `choosing-test-strategy` before locking in validation
5. `managing-project-docs` when deciding what artifact should exist

## Skill Map

| Area | Skills |
|------|--------|
| Routing and shaping | `using-redteapowers`, `shaping-work`, `researching-and-collecting`, `brainstorming` |
| Planning and execution | `writing-plans`, `executing-plans`, `subagent-driven-development` |
| Validation and debugging | `choosing-test-strategy`, `test-driven-development`, `systematic-debugging`, `verification-before-completion` |
| Documentation and migration | `managing-project-docs`, `migrating-project-docs` |
| Review and branch flow | `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch` |

## What Changed From Superpowers

RedTeaPowers is not just a rename. It changes the operating behavior of the original library.

| Old tendency | RedTeaPowers default |
|--------------|----------------------|
| `brainstorm -> spec -> plan -> execute` by habit | route first, then add only the next layer that materially helps |
| heavy requirement convergence up front | small convergence budget with explicit stop rules |
| `spec` and `plan` as default document outcomes | broader doc taxonomy with `guide`, `discuss`, `reference`, `change`, `archive`, and `scripts`, plus session task tracking in `TodoWrite` / `update_plan` |
| silent TDD-first behavior | choose validation first, use TDD only when it actually fits |
| one tiny loop per visible issue | batch same-kind low-risk follow-up work |
| thin first slice forever | open the topic, then stabilize into efficient delivery |

## Document Taxonomy Note

Two document types are easy to misuse unless their boundaries stay explicit:

- `discuss` is for pre-execution requirement discussion, open questions, and alternatives while the work is not entering implementation yet
- once the team decides to execute, the approved behavior and boundaries should move into `spec` instead of staying in `discuss`
- `guide` is for a stage-level development charter or phased development outline
- `guide` is not the default home for general explanatory material, architecture overview, or "how this area works" notes; those usually belong in `reference`

See [docs/reference/003-document-taxonomy-clarifications.md](docs/reference/003-document-taxonomy-clarifications.md) for the sharper boundary rules.

## Included In The Current Package

The active package currently includes:

- `using-redteapowers`
- `shaping-work`
- `researching-and-collecting`
- `choosing-test-strategy`
- `managing-project-docs`
- `migrating-project-docs`
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

See [PACKAGE.md](PACKAGE.md) for the packaged skill set and [using-redteapowers/references/library-status-matrix.md](using-redteapowers/references/library-status-matrix.md) for keep, rewrite, and archive decisions.

## Quick Start

Clone the repository:

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

Install the skill folders into your Codex skills directory:

```text
~/.codex/skills
```

On this machine that path is typically:

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` is useful package documentation, but it is not required for runtime skill discovery.

## Repository Layout

- `README.md` is the English overview
- `README.zh-CN.md` is the Chinese overview
- `PACKAGE.md` describes the packaged active skill set
- each top-level directory is a skill
- `agents/openai.yaml` holds UI-facing metadata where present
- `references/` holds load-on-demand guidance
- `scripts/` holds reusable helper scripts where needed
- `assets/` holds reusable presentation assets

## Migration Notes

If you are moving from an older `superpowers` setup, start here:

- [using-redteapowers/references/migrating-from-superpowers.md](using-redteapowers/references/migrating-from-superpowers.md)
- [using-redteapowers/references/workflow-overview.md](using-redteapowers/references/workflow-overview.md)
- [using-redteapowers/references/library-status-matrix.md](using-redteapowers/references/library-status-matrix.md)

## Project Rule

All project documents should be read and written as UTF-8 text.
