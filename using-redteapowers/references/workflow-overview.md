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

## Default Convergence Rules

Use these rules by default unless a clear exception applies:

- Use a small convergence budget:
  ask only the questions that would change the route, and usually no more than 1-3 in one round
- Create at most one new active artifact before implementation starts
- If 3 or more same-kind low-risk items are visible, default to a batch checklist instead of separate loops
- Use a thin first slice only to open the topic, then convert the remaining same-kind work into a batch within the next 1-2 rounds if the direction is now clear
- Exceed these defaults only when requirements are unstable, architectural choices are expensive to reverse, or risk is unusually high

## Recommended Flow

1. Route the work with `shaping-work`
2. If the request is a bug or failure, use `systematic-debugging`
3. If the next blocker is missing facts, inventory, or comparison work across the current project, local references, or external sources, use `researching-and-collecting`
4. If design decisions still matter, use `brainstorming`
5. If documentation is needed, use `managing-project-docs`
6. If legacy project documents need conversion, use `migrating-project-docs`
7. If validation is not already obvious, choose it with `choosing-test-strategy`
8. If implementation still needs a stable execution artifact, use `writing-plans`
9. Use `test-driven-development` only when TDD is the chosen strategy
10. Use `verification-before-completion` before any success claim

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
- 3 or more same-kind low-risk items are already visible

### Formal plan

Use when:
- ordering matters
- another agent or session needs a stable artifact
- the work spans enough files or steps to justify planning

Before finalizing the plan, make sure the validation mode is already chosen or genuinely obvious.

### Spec plus plan

Use when:
- behavior is still under discussion
- several approaches need alignment
- mistakes would be expensive to unwind

## After Mainline Stabilizes

When the first slice has already opened the topic and the mainline is stable enough to inspect:

- switch from convergence mode to batch delivery mode
- keep one primary workstream for the topic
- reduce document and sync churn
- batch same-kind follow-up work into a small number of meaningful passes
- bring real flow or real experience verification forward before the very end
- extract reusable guidance, reference material, scripts, or validation rules only where they reduce future rework

See [002-opened-topic-stabilization.md](../../shaping-work/references/002-opened-topic-stabilization.md) for the detailed mode-switch rules.

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
- spending multiple rounds on clarification that no longer changes the route
- turning every visible same-kind task into its own tiny loop
- preserving fake momentum by slicing work smaller after uncertainty is already gone
- mixing document encodings across the same project

## Packaging Reference

Read [library-status-matrix.md](library-status-matrix.md) for the current keep, rewrite, and archive decisions across the top-level skill directories.
