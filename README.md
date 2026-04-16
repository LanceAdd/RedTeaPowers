# RedTeaPowers

[中文说明 / Chinese Version](README.zh-CN.md)

```text
    ____           __  ______              ____                            
   / __ \___  ____/ / /_  __/__  ____ _   / __ \____ _      _____  __________
  / /_/ / _ \/ __  /   / / / _ \/ __ `/  / /_/ / __ \ | /| / / _ \/ ___/ ___/
 / _, _/  __/ /_/ /   / / /  __/ /_/ /  / ____/ /_/ / |/ |/ /  __/ /  (__  ) 
/_/ |_|\___/\__,_/   /_/  \___/\__,_/  /_/    \____/|__/|__/\___/_/  /____/  
```

> Structured software work, with less ceremony and better momentum.

## 🍵 What This Is

RedTeaPowers is a curated skill library for teams that still want engineering discipline, but do not want to pay for it with slow momentum, endless micro-loops, or document sprawl.

It keeps the useful parts of process:

- work shaping before blind execution
- explicit validation choices
- durable documentation with clear purpose
- disciplined execution, review, and completion

It strips out the parts that usually become drag:

- mandatory `spec` and `plan` for every task
- one-problem-one-loop behavior
- silent TDD-by-default assumptions
- vague documentation buckets that absorb everything

## ✨ Design Direction

RedTeaPowers is opinionated in a few important ways:

- **Light by default**: start with the smallest safe workflow
- **Sharp boundaries**: `discuss`, `guide`, `spec`, `plan`, `reference`, `change`, `archive` each do a different job
- **Evidence first**: success claims require fresh verification
- **Batch after clarity**: once the mainline is open, same-kind follow-up work should move in stronger passes
- **Runtime realism**: skills should work after distribution, not only inside the source repo

## 🧭 Operating Model

```text
route -> research if facts are missing -> design only if needed -> plan only if needed -> execute -> verify -> finish
```

Recommended entry points:

1. `using-redteapowers` for top-level workflow routing
2. `shaping-work` to choose direct execution, session task tracking, plan, or `spec + plan`
3. `researching-and-collecting` when the next blocker is missing facts, inventory, or comparison work
4. `choosing-test-strategy` before locking in validation
5. `managing-project-docs` when deciding what artifact should exist

## 🧩 Skill Constellation

| Area | Skills |
|------|--------|
| Routing and shaping | `using-redteapowers`, `shaping-work`, `researching-and-collecting`, `brainstorming` |
| Planning and execution | `writing-plans`, `executing-plans`, `subagent-driven-development` |
| Validation and debugging | `choosing-test-strategy`, `test-driven-development`, `systematic-debugging`, `verification-before-completion` |
| Documentation and migration | `managing-project-docs`, `migrating-project-docs` |
| Review and branch flow | `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch` |

## 🔄 From Superpowers To RedTeaPowers

This repo is not a rename. It is a reset of the operating defaults.

| Old tendency | RedTeaPowers default |
|--------------|----------------------|
| `brainstorm -> spec -> plan -> execute` by habit | route first, then add only the next layer that materially helps |
| heavy convergence up front | small convergence budget with explicit stop rules |
| `spec` and `plan` as default document outcomes | broader taxonomy with `guide`, `discuss`, `reference`, `change`, `archive`, and `scripts`, plus session task tracking in `TodoWrite` / `update_plan` |
| silent TDD-first behavior | choose validation first, use TDD only when it actually fits |
| one tiny loop per visible issue | batch same-kind low-risk follow-up work |
| first-slice behavior kept too long | open the topic, then stabilize into efficient delivery |

## 📚 Document Taxonomy

The repo now treats documentation as a deliberate system, not as generic notes.

Key boundaries:

- `discuss` is for pre-execution requirement discussion
- `guide` is for stage-level development charter or phased development outline
- `spec` is for approved behavior and boundaries
- `plan` is for execution sequencing
- `reference` is for lookup material and durable technical explanation
- `change` is written after execution and review close

See:

- [Document Taxonomy Clarifications](docs/reference/003-document-taxonomy-clarifications.md)

## 🧱 New Module Work

New modules need a sharper opening move than ordinary feature polish.

Use:

- [New Module Development Flow](skills/shaping-work/references/003-new-module-development-flow.md)
- [New Module Spec Template](skills/brainstorming/references/001-new-module-spec-template.md)
- [Module Design Record Template](skills/brainstorming/references/002-module-design-record-template.md)
- [New Module Plan Template](skills/writing-plans/references/001-new-module-plan-template.md)

This reflects the current project rule:

1. keep requirements in `discuss` until execution is approved
2. move approved behavior into `spec`
3. place durable design explanation in `reference` when it would overcrowd the spec
4. write `plan` only after the module shape is stable enough to execute

## 📦 Current Active Package

The current active package includes:

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

See:

- [Package Overview](PACKAGE.md)
- [Library Status Matrix](skills/using-redteapowers/references/library-status-matrix.md)

## 🗂️ Repository Layout

The repo now separates source-library structure from runtime installation shape.

```text
RedTeaPowers/
├─ skills/    # source skill directories
├─ docs/      # repo-level calibration and reference notes
├─ assets/    # shared presentation assets
├─ README.md
├─ README.zh-CN.md
└─ PACKAGE.md
```

Inside `skills/`, each subdirectory is one installable skill:

```text
skills/<skill-name>/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
└─ scripts/
```

## 🚀 Installation

Clone the repository:

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

Copy the skill directories you want from `skills/` into your Codex skills directory:

```text
~/.codex/skills
```

On this machine that path is typically:

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` is useful package documentation, but runtime discovery depends on the individual skill folders.

## 🔧 Packaging Rule

This matters for how the repo is maintained now:

- source skills live under `skills/`
- distributed skills are copied as flat sibling directories into the runtime skills folder
- runtime skill behavior must not depend on repository-root files that will not ship with the selected skill directories

In practice:

- keep runtime references inside the skill itself
- or use sibling-skill relative references that still exist after flat distribution

## 🔁 Migration References

If you are moving from an older `superpowers` setup, start here:

- [Migrating From Superpowers](skills/using-redteapowers/references/migrating-from-superpowers.md)
- [Workflow Overview](skills/using-redteapowers/references/workflow-overview.md)
- [Library Status Matrix](skills/using-redteapowers/references/library-status-matrix.md)

## 📝 Project Rule

All project documents should be read and written as UTF-8 text.
