# RedTeaPowers

RedTeaPowers is a curated skill library for structured software work with lighter process by default.

It started from the original `superpowers` skill set, then was selectively rebuilt into a more execution-oriented package:

- route before adding ceremony
- batch related small work instead of fragmenting it into tiny loops
- choose documentation by purpose instead of defaulting to `spec` and `plan`
- choose validation strategy intentionally instead of assuming TDD
- keep project documents in UTF-8

## Why RedTeaPowers

Many workflow systems become slow not because they lack structure, but because they over-apply structure.

RedTeaPowers is designed to keep the useful parts of process:

- work shaping
- explicit validation choices
- durable documentation when it actually helps
- repeatable execution workflows

while removing common sources of drag:

- mandatory brainstorm -> spec -> plan chains
- excessive convergence before implementation
- one-problem-one-loop fragmentation
- silent TDD defaults
- document sprawl without taxonomy

## Core Philosophy

RedTeaPowers follows a few default rules:

1. Start with the lightest workflow that preserves clarity and safety.
2. Shape the work before writing process artifacts.
3. If 3 or more same-kind low-risk items are visible, batch them by default.
4. Use a thin first slice only to open uncertainty, then move into batch progress quickly.
5. Choose the cheapest validation strategy that protects the real risk.
6. Read and write all project documents as UTF-8 text.

## What Is Included

This repository is the active packaged cut of the library. It intentionally keeps the current high-value skills and leaves out historical or experimental material.

### Workflow And Routing

- `using-redteapowers`
- `shaping-work`
- `brainstorming`
- `writing-plans`
- `executing-plans`

### Validation And Debugging

- `choosing-test-strategy`
- `test-driven-development`
- `systematic-debugging`
- `verification-before-completion`

### Documentation And Collaboration

- `managing-project-docs`
- `requesting-code-review`
- `receiving-code-review`
- `subagent-driven-development`

### Supporting Skills

- `using-git-worktrees`
- `finishing-a-development-branch`

## What Changed From The Original Superpowers

RedTeaPowers is not just a rename. It changes the operating defaults of the original library.

### 1. Workflow Is Routed, Not Forced

Original `superpowers` patterns often nudged work toward a heavier chain:

`brainstorm -> spec -> plan -> execute`

RedTeaPowers changes this to:

`route -> shape -> only add the next layer if it materially helps`

That means direct execution, batch checklist, lightweight plan, and spec-plus-plan are all valid routes depending on task shape.

### 2. Demand Convergence Is Now Guarded

RedTeaPowers adds explicit anti-over-convergence rules:

- use a small convergence budget by default
- ask only the questions that would change the route
- avoid creating more than one active artifact before implementation starts
- batch same-kind low-risk issues when they are already visible
- avoid staying in endless tiny-slice mode after the topic is understood

### 3. Spec And Plan Are No Longer Universal Defaults

In RedTeaPowers:

- `spec` is for approved behavior and boundaries
- `plan` is for executable sequencing
- `todolist` is the default home for active near-term work when a formal plan is unnecessary
- `guide`, `discuss`, `reference`, `change`, and `archive` are first-class document types

### 4. TDD Is A Strategy, Not A Doctrine

The original ecosystem often leaned toward implicit TDD-first behavior.

RedTeaPowers requires choosing a validation strategy first:

- TDD
- regression test
- integration check
- manual verification
- exploration first

TDD is still supported, but only when it is actually the right fit.

### 5. Documentation Taxonomy Was Expanded

Instead of centering nearly everything around `spec` and `plan`, RedTeaPowers formalizes a broader doc system:

- `guide`
- `discuss`
- `spec`
- `plan`
- `reference`
- `change`
- `archive`
- `todolist`
- `scripts`

This reduces document overload, keeps artifacts easier to navigate, and prevents long mixed-purpose files from becoming the default.

### 6. Naming, Namespace, And Paths Were Reworked

Examples of migration changes:

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/` -> `.redteapowers/`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

### 7. Historical Material Was Curated Instead Of Left Active

This package is intentionally selective. Not every original top-level skill was carried forward into the default active library.

The goal is to ship a cleaner working set rather than preserve every historical artifact as active guidance.

### 8. Some Skill Boundaries Were Renamed Or Reframed

Examples:

- `using-superpowers` was replaced by `using-redteapowers`
- agent-dispatch workflow ideas were kept, but the active packaged skill is framed as `subagent-driven-development`
- review prompts were updated to match the new scope-first model, including `spec`-centric wording being reduced where it no longer fit
- only the current packaged working set was kept active, while non-core or historical material stayed outside the default library

## Repository Layout

- `README.md` is the repository overview and positioning document.
- `PACKAGE.md` describes the packaged skill set at a high level.
- Each top-level directory is a skill.
- `agents/openai.yaml` provides UI-facing metadata where present.
- `references/` holds load-on-demand guidance.
- `scripts/` holds reusable helper scripts where needed.

## How To Use

### Use As A Git Repository

Clone this repository and work directly inside it as the source of truth:

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

### Use As A Codex Skill Library

Install or copy the skill folders into your Codex skills directory:

```text
~/.codex/skills
```

On this machine, that path is typically:

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` is useful as repository and package documentation, but it is not required for Codex runtime discovery.

## Recommended Entry Points

If you are starting fresh:

1. Use `using-redteapowers` for top-level routing.
2. Use `shaping-work` to choose between direct execution, checklist, plan, or spec-plus-plan.
3. Use `choosing-test-strategy` before locking in validation.
4. Use `managing-project-docs` when deciding what kind of artifact should exist.

## Migration Notes

If you are migrating an older `superpowers` setup, start here:

- `using-redteapowers/references/migrating-from-superpowers.md`
- `using-redteapowers/references/workflow-overview.md`
- `using-redteapowers/references/library-status-matrix.md`

## Encoding Policy

All project documents should be read and written as UTF-8 text.

This is a deliberate project rule, not a suggestion.
