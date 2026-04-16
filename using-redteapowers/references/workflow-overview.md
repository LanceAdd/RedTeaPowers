# Workflow Overview

Use this guide to understand the RedTeaPowers workflow before choosing a specific skill.

## The New Default

Do not assume every request needs:
- a formal design pass
- a formal spec
- a formal implementation plan
- strict TDD
- tiny one-change-only loops

Start by shaping the work, then add only the process that reduces real risk.

## Recommended Flow

1. Route the work with `shaping-work`
2. If the request is a bug or failure, use `systematic-debugging`
3. If design decisions still matter, use `brainstorming`
4. If documentation is needed, use `managing-project-docs`
5. If implementation needs a stable execution artifact, use `writing-plans`
6. Before implementation, choose validation with `choosing-test-strategy`
7. Use `test-driven-development` only when TDD is the chosen strategy
8. Use `verification-before-completion` before any success claim

## Work Shapes

### Direct execution

Use when:
- the request is bounded
- expected behavior is already clear
- documentation would mostly restate obvious work

### Batch checklist

Use when:
- several same-kind small issues belong together
- splitting them would waste setup time
- one active queue is enough

### Formal plan

Use when:
- ordering matters
- another agent or session needs a stable artifact
- the work spans enough files or steps to justify planning

### Spec plus plan

Use when:
- behavior is still under discussion
- several approaches need alignment
- mistakes would be expensive to unwind

## Validation Shapes

Choose the lightest strategy that guards the real risk:

- `TDD` for clear local behavior
- `Regression test` for known bugs
- `Integration check` for cross-boundary behavior
- `Manual verification` for UX and visual work
- `Exploration first` when the interface is still moving

## Documentation Shapes

Use the document type that matches the job:

- `guide` for orientation and development outline
- `discuss` for provisional decisions and unapproved ideas
- `spec` for approved behavior
- `plan` for executable implementation sequencing
- `reference` for lookup material
- `change` for per-round change records
- `archive` for inactive but useful history
- `todolist` for active next actions

All project documents should be read and written as UTF-8 text.

## Anti-Patterns

Avoid:
- writing a spec just because a topic exists
- writing a plan when a checklist would do
- forcing TDD onto visual or exploratory work
- preserving fake momentum by slicing work smaller after uncertainty is already gone
- mixing document encodings across the same project

## Packaging Reference

Read [library-status-matrix.md](library-status-matrix.md) for the current keep, rewrite, and archive decisions across the top-level skill directories.
