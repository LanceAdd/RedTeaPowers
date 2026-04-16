# Migrating From Superpowers

Use this guide when moving an older superpowers-based workflow, skill set, or documentation layout into RedTeaPowers.

## What Changes In RedTeaPowers

RedTeaPowers keeps the strongest parts of superpowers, but changes the defaults:

- heavy process is no longer the default
- spec and plan are no longer mandatory for every topic
- TDD is no longer the universal default
- documentation is split by purpose, not forced into only spec and plan
- all project documents should be read and written as UTF-8 text

## Fast Mapping

| Superpowers concept | RedTeaPowers equivalent |
|---------------------|-------------------------|
| `using-superpowers` | `using-redteapowers` |
| Default brainstorming before creative work | `shaping-work` first, then `brainstorming` only if real design uncertainty remains |
| Default spec/plan flow | Route to direct execution, session task tracking, plan, or spec plus plan based on task shape |
| Default TDD | `choosing-test-strategy` first, `test-driven-development` only if selected |
| `superpowers:` namespace | `redteapowers:` namespace |
| `.superpowers/` project state | `.redteapowers/` project state |
| `~/.config/superpowers/...` | `~/.config/redteapowers/...` |

## Workflow Migration

### Old default

Typical superpowers instinct:

1. invoke getting-started workflow
2. brainstorm
3. write spec
4. write plan
5. execute with strong TDD assumptions

### New default

Typical RedTeaPowers flow:

1. route with `using-redteapowers`
2. shape the work with `shaping-work`
3. if needed, use `brainstorming`
4. if needed, use `managing-project-docs`
5. if needed, use `writing-plans`
6. choose validation with `choosing-test-strategy`
7. execute

The big change is that each step is conditional, not mandatory.

## Documentation Migration

### Old assumption

Many older superpowers flows assume most durable work belongs in:
- `spec`
- `plan`

### New structure

RedTeaPowers uses:
- `guide`
- `discuss`
- `spec`
- `plan`
- `reference`
- `change`
- `archive`
- `scripts`

### Migration rule

When converting old docs:

- move stage-level development charters to `guide`
- move unresolved pre-execution requirement discussion to `discuss`
- keep only approved target behavior in `spec`
- keep executable sequencing in `plan`
- move lookup material to `reference`
- track per-round progress in `change`
- move inactive material to `archive`
- turn active queues into `plan` when they need a durable document, otherwise keep them in `TodoWrite` / `update_plan`

Add numbered filenames such as `001-topic.md`, `002-topic.md`, and preserve UTF-8 encoding when rewriting or splitting files.

## Testing Migration

### Old assumption

Older superpowers material often assumes:
- every implementation should use TDD
- tests-first is the default answer

### New rule

In RedTeaPowers:

1. choose the validation strategy first
2. use TDD only when it is the right fit

Use:
- `TDD` for clear local behavior
- `Regression test` for known bugs
- `Integration check` for cross-boundary behavior
- `Manual verification` for UX and visual work
- `Exploration first` when the interface is still moving

## Namespace And Path Migration

Update these patterns when migrating old content:

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/...` -> `.redteapowers/...`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

## Review Prompts And Agent Names

Older prompts may still say:
- `spec compliance`
- `superpowers:code-reviewer`
- fixed `spec -> plan -> execute` assumptions

When migrating prompts:

- change `spec compliance` to `scope compliance` where appropriate
- switch named agent examples to `redteapowers:...`
- allow session-tracked execution where a formal plan is unnecessary
- add UTF-8 checks when prompts review document work

## Migration Steps

- [ ] Replace `using-superpowers` with `using-redteapowers`
- [ ] Replace `superpowers:` namespace with `redteapowers:`
- [ ] Replace `.superpowers/` paths with `.redteapowers/`
- [ ] Replace `~/.config/superpowers/` paths with `~/.config/redteapowers/`
- [ ] Re-route old mandatory brainstorm/spec/plan flows through `shaping-work`
- [ ] Add `choosing-test-strategy` before any old default TDD step
- [ ] Reclassify documents into the new taxonomy
- [ ] Add numbered filenames where order matters
- [ ] Preserve UTF-8 encoding across migrated documents
- [ ] Archive historical or obsolete material instead of leaving it in active guidance

## Common Migration Mistakes

- Renaming the package but keeping old workflow defaults
- Renaming namespaces but leaving `.superpowers` paths behind
- Keeping old spec-first behavior even for tiny changes
- Keeping TDD as a silent default even after adding `choosing-test-strategy`
- Leaving historical notes mixed into active instructions
- Rewriting documents without preserving UTF-8
