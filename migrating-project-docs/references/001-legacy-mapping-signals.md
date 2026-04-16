# Legacy Mapping Signals

Use this reference to map legacy documentation into the RedTeaPowers document system.

## Core Principle

Map by actual purpose, not by legacy filename.

A file called `spec.md` is not automatically a `spec`.

## Target Directories

Prefer these targets:

- `docs/guide/`
- `docs/discuss/`
- `docs/spec/`
- `docs/plan/`
- `docs/reference/`
- `docs/change/`
- `docs/archive/`
- `docs/todolist/`
- `scripts/`

## Quick Mapping Table

| Legacy signal | Usually migrate to | Notes |
|---------------|--------------------|-------|
| architecture overview, orientation, topic map | `guide` | Keep big-picture material together |
| unapproved ideas, decision debate, open questions | `discuss` | Use when the behavior is not yet locked |
| approved behavior, scope, success criteria | `spec` | Keep only the stable target behavior |
| ordered implementation sequence | `plan` | Use only when sequencing still matters |
| active tasks, blockers, next steps, cleanup queue | `todolist` | Better than forcing a full plan |
| schema notes, API facts, terminology, lookup details | `reference` | Move facts out of spec/plan when crowded |
| what changed this round and why | `change` | Use for migration logs or active project updates |
| retired notes, finished stage docs, superseded plans | `archive` | Keep searchable, not active |
| runnable helper content | `scripts` | Move executable material out of docs |

## Filename Signals

These are weak signals, not rules:

- `spec.md`, `requirements.md`, `behavior.md`
  Often become `spec`, but can also become `guide`, `discuss`, or `reference`

- `plan.md`, `roadmap.md`, `implementation.md`
  Often become `plan`, but short active work may really be `todolist`

- `notes.md`, `research.md`, `scratch.md`
  Often become `reference`, `discuss`, or `archive`

- `todo.md`, `tasks.md`, `next-steps.md`
  Often become `todolist`

- `changelog.md`, `updates.md`, `round-notes.md`
  Often become `change` or `archive`

## Content Signals

### guide

Signals:

- explains the area
- orients readers
- gives strategy or development direction
- useful even without immediate implementation

### discuss

Signals:

- contains alternatives and tradeoffs
- contains unresolved questions
- not yet approved as project truth

### spec

Signals:

- states what should happen
- records approved boundaries
- defines success conditions

Anti-signals:

- mostly implementation steps
- mostly raw research
- mostly active task queue

### plan

Signals:

- ordered execution matters
- dependencies matter
- another person or future session needs stable sequencing

Anti-signals:

- only a short near-term queue
- mostly same-kind cleanup items

### reference

Signals:

- readers will revisit this for facts
- stable lookup material
- data models, API details, configuration facts, glossaries

### change

Signals:

- explains what changed in a pass
- records why the project docs or implementation changed
- useful as a short decision trail

### archive

Signals:

- no longer active
- still historically useful
- likely to confuse readers if left in active folders

### todolist

Signals:

- near-term tasks
- blockers and prerequisites
- several same-kind small fixes
- active queue that should move soon

## Mixed Documents

A legacy document should usually be split when it combines:

- overview + detailed reference
- approved behavior + open questions
- implementation plan + active checklist
- active guidance + historical notes

Common split patterns:

- `guide` + `reference`
- `spec` + `reference`
- `plan` + `todolist`
- active type + `archive`

## Migration Biases

When uncertain:

- prefer `discuss` over `spec`
- prefer `todolist` over `plan` for near-term actionable queues
- prefer `archive` over leaving stale material active
- prefer `reference` for stable facts

These biases reduce false authority and reduce document clutter.
