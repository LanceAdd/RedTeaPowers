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
- `scripts/`

## Quick Mapping Table

| Legacy signal | Usually migrate to | Notes |
|---------------|--------------------|-------|
| architecture overview, orientation, topic map | `reference` | Keep explanatory material in lookup docs, not `guide` |
| unapproved ideas, decision debate, open questions | `discuss` | Use only while requirements are still under discussion and not entering execution |
| approved behavior, scope, success criteria | `spec` | Keep only the stable target behavior |
| ordered implementation sequence | `plan` | Use only when sequencing still matters |
| active tasks, blockers, next steps, cleanup queue | `plan` or session task tracking | Use `plan` only when the queue needs a durable cross-session artifact |
| schema notes, API facts, terminology, lookup details | `reference` | Move facts out of spec/plan when crowded |
| what changed this round and why | `change` | Use for migration logs or active project updates |
| retired notes, finished stage docs, superseded plans | `archive` | Keep searchable, not active |
| runnable helper content | `scripts` | Move executable material out of docs |

## Filename Signals

These are weak signals, not rules:

- `spec.md`, `requirements.md`, `behavior.md`
  Often become `spec`, but can also become `guide`, `discuss`, or `reference`

- `plan.md`, `roadmap.md`, `implementation.md`
  Often become `plan`, but very short active work may not deserve a document after migration

- `notes.md`, `research.md`, `scratch.md`
  Often become `reference`, `discuss`, or `archive`

- `todo.md`, `tasks.md`, `next-steps.md`
  Often become `plan` or collapse into session task tracking

- `changelog.md`, `updates.md`, `round-notes.md`
  Often become `change` or `archive`

## Content Signals

### guide

Signals:

- defines a stage or phase development charter
- gives bounded development direction for the next execution phase
- records stage-specific principles or constraints
- exists to steer execution for that stage, not to explain the area generally

### discuss

Signals:

- contains requirement discussion before execution
- contains alternatives and tradeoffs
- contains unresolved questions
- not yet entering implementation

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

## Mixed Documents

A legacy document should usually be split when it combines:

- overview + detailed reference
- approved behavior + open questions
- implementation plan + transient task queue
- active guidance + historical notes

Common split patterns:

- `guide` + `reference`
- `spec` + `reference`
- active type + `archive`

## Migration Biases

When uncertain:

- prefer `discuss` over `spec` only while the requirement is still pre-execution
- once execution is chosen, prefer `spec` over leaving active decisions in `discuss`
- prefer session task tracking over a written plan for very short near-term queues
- prefer `plan` when the queue needs durable sequencing across sessions
- prefer `archive` over leaving stale material active
- prefer `reference` for stable facts

These biases reduce false authority and reduce document clutter.
