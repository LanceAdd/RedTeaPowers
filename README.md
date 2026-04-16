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

RedTeaPowers is a curated skill library for structured software work with lighter process by default.

## Overview

RedTeaPowers started from the original `superpowers` ecosystem, then was selectively rebuilt into a cleaner, more execution-oriented package.

It keeps the parts of process that actually help:

- work shaping
- explicit validation choices
- durable documentation when it is truly useful
- repeatable execution workflows

and pushes back on the parts that often slow teams down:

- mandatory brainstorm -> spec -> plan chains
- excessive convergence before implementation
- one-problem-one-loop fragmentation
- silent TDD defaults
- document sprawl without taxonomy

## Why Build This Instead Of Continuing With Superpowers

RedTeaPowers exists because simply continuing to use the original `superpowers` defaults would keep reintroducing the same delivery problems.

In practice, the old flow was strong in structure but too easy to over-apply. Teams could end up spending too much time converging before coding, too much time writing process artifacts, and too little time turning one opened topic into fast, meaningful progress.

RedTeaPowers was built to keep the useful discipline while changing the default operating behavior.

## Pain Points It Solves

- Over-convergence before implementation. Small and medium tasks could get trapped in too much clarification, too many tiny slices, or too much speculative structure before real delivery started.
- Forced `spec` and `plan` writing. Process artifacts were too easy to produce by habit even when a checklist or direct execution was enough.
- Weak document taxonomy. Important information was too likely to collapse into only `spec` and `plan`, which made document systems harder to navigate and easier to fragment.
- Silent TDD pressure. TDD could become the assumed answer even when the work was visual, exploratory, integration-heavy, or otherwise a poor fit.
- One-problem-one-loop execution. Same-kind low-risk issues were too easy to split into many tiny passes instead of being handled as one efficient batch.
- Poor transition from first slice to real momentum. A thin opening slice is useful, but without a rule to batch soon after, teams can stay stuck in endless micro-progress.
- Encoding inconsistency in docs. Without an explicit rule, project documents can drift into mixed encodings and become harder to process reliably.

In short, RedTeaPowers is for teams who still want structure, but want that structure to accelerate delivery instead of slowing it down.

## Core Defaults

RedTeaPowers follows these defaults:

1. Start with the lightest workflow that preserves clarity and safety.
2. Shape the work before writing process artifacts.
3. If 3 or more same-kind low-risk items are visible, batch them by default.
4. Use a thin first slice only to open uncertainty, then move into batch progress quickly.
5. Choose the cheapest validation strategy that protects the real risk.
6. Read and write all project documents as UTF-8 text.

## Included Skills

Workflow and routing:

- `using-redteapowers`
- `shaping-work`
- `brainstorming`
- `writing-plans`
- `executing-plans`

Validation and debugging:

- `choosing-test-strategy`
- `test-driven-development`
- `systematic-debugging`
- `verification-before-completion`

Documentation and collaboration:

- `managing-project-docs`
- `migrating-project-docs`
- `requesting-code-review`
- `receiving-code-review`
- `subagent-driven-development`

Supporting skills:

- `using-git-worktrees`
- `finishing-a-development-branch`

## What Changed From The Original Superpowers

RedTeaPowers is not just a rename. It changes the operating defaults of the original library.

### 1. Workflow Is Routed, Not Forced

Old instinct:

```text
brainstorm -> spec -> plan -> execute
```

RedTeaPowers default:

```text
route -> shape -> add only the next layer that materially helps
```

That means direct execution, batch checklist, lightweight plan, and spec-plus-plan are all valid routes depending on task shape.

### 2. Demand Convergence Is Explicitly Guarded

RedTeaPowers adds anti-over-convergence rules:

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

### 6. Naming, Namespace, And Paths Were Reworked

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/` -> `.redteapowers/`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

### 7. Historical Material Was Curated Instead Of Left Active

This package is intentionally selective. Not every original top-level skill was carried forward into the default active library.

### 8. Some Skill Boundaries Were Renamed Or Reframed

- `using-superpowers` was replaced by `using-redteapowers`
- agent-dispatch workflow ideas were kept, but the active packaged skill is framed as `subagent-driven-development`
- review prompts were updated to fit the newer scope-first model instead of rigid spec-centric assumptions
- only the current packaged working set stays active by default

## Repository Layout

- `README.md` is the English repository overview
- `README.zh-CN.md` is the Chinese repository overview
- `PACKAGE.md` describes the packaged skill set
- each top-level directory is a skill
- `agents/openai.yaml` provides UI-facing metadata where present
- `references/` holds load-on-demand guidance
- `scripts/` holds reusable helper scripts where needed
- `assets/` holds reusable presentation assets such as the character icon

## How To Use

Use as a git repository:

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

Use as a Codex skill library by installing or copying the skill folders into:

```text
~/.codex/skills
```

On this machine, that path is typically:

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` is useful as repository and package documentation, but it is not required for Codex runtime discovery.

## Recommended Entry Points

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

This is a project rule, not a suggestion.
