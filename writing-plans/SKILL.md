---
name: writing-plans
description: Use when work actually needs an implementation plan or execution checklist across multiple steps, files, or contributors. Default to a lightweight todolist for related small work, and do not use when direct execution is enough or a formal plan would only restate obvious next actions.
---

# Writing Plans

## Overview

Write a plan only when planning will reduce confusion, coordination cost, or execution risk. If a lightweight checklist is enough, do not inflate it into a formal plan.
Default to the smallest artifact that keeps execution moving.
Once a topic is already open and the mainline is stable, use the plan to organize batch delivery and systemization, not to preserve first-slice behavior.

Before using this skill, route the work with `shaping-work`. If validation strategy is not decided yet, use `choosing-test-strategy` before finalizing the plan.

## First Decision: Plan Or Checklist

Start by assuming a checklist or direct execution is enough. Escalate to a formal plan only when the work would be meaningfully harder to execute without one.
If a first slice already proved the direction, plan the next meaningful batch instead of writing a plan around another tiny slice.

Use a formal plan when:
- The work spans multiple files, steps, or milestones
- Ordering matters
- Another agent or future session needs a stable execution artifact
- The task has enough surface area that a todolist would become vague

Use a checklist or todolist instead when:
- The work is a batch of related small changes
- The next actions are obvious
- Fine-grained planning would cost more than it saves
- The remaining same-kind work should simply be finished in one coordinated pass

If a checklist is enough, hand off to `managing-project-docs` and store it under `docs/todolist/`.

## Plan Style

Write plans for execution, not ceremony.

- Group related work into meaningful tasks or batches.
- Collapse same-kind low-risk fixes into one batch when they touch the same area.
- Do not force every task into 2-5 minute micro-steps.
- Include exact file paths, dependencies, and validation expectations.
- Include only as much detail as the executor actually needs.
- Prefer a few strong tasks with clear checkpoints over a wall of tiny steps.
- Do not write a formal plan whose only purpose is to serialize obvious same-kind follow-up work.

## When The Topic Is Already Open

If a first slice already validated the route, the plan should shift into stabilization mode:

- define one primary workstream for the topic
- batch same-area follow-up work into a small number of passes
- name any systemization outputs that should come out of the batch
- pull real experience verification forward enough to influence the remaining work

Use `../shaping-work/references/002-opened-topic-stabilization.md` as the reference for this mode switch.

## Document Location

Store plans under `docs/plan/NNN-topic.md` unless the project already uses a stronger convention.

Use `managing-project-docs` for numbering and split rules.
Write and update plan documents in UTF-8 encoding.

## Plan Header

Every formal plan should start with:

```markdown
# [Feature Name] Implementation Plan

**Goal:** [What this work will accomplish]
**Scope:** [What is in and out]
**Validation:** [Chosen strategy from choosing-test-strategy]
**Execution mode:** [Direct, inline, or subagent-driven]

---
```

## Task Structure

Prefer tasks shaped like this:

````markdown
## Task 1: Settings panel cleanup batch

**Why:** Consolidate four related UI fixes while the same files are open.

**Files:**
- Modify: `src/settings/Panel.tsx`
- Modify: `src/settings/Panel.css`
- Verify: `manual UI check in settings screen`

**Do:**
- Align spacing tokens across the three cards
- Fix button disabled and loading states
- Update helper copy to match the new behavior
- Remove the obsolete warning row

**Checkpoint:**
- All four fixes are visible in one pass
- No card regressed at desktop or mobile widths
````

Use smaller steps inside a task only when sequencing is easy to get wrong.

## Required Sections

Every formal plan must make these things explicit:

- What files or areas will change
- What each task or batch is responsible for
- What the validation strategy is
- What the completion checkpoint is
- What the executor should not expand or overbuild
- That any written plan or checklist artifact is stored as UTF-8 text

If the topic is already open, also make explicit:

- which batch turns the topic from first-slice work into steady delivery
- whether a `guide`, `reference`, script, checklist, or reusable pattern should be created or updated
- when real experience verification must happen before final completion

## No Placeholder Planning

These are plan failures:
- "TBD", "TODO", or "fill in later"
- "Add appropriate validation" without naming the chosen validation strategy
- "Write tests" without saying what kind of test or check is expected
- "Similar to Task N" when the task can stand alone
- Creating separate tasks only to preserve fake granularity

## Self-Review

After writing the plan:

1. Check that the plan is actually necessary and not better as a checklist.
2. Check coverage against the requirements or spec.
3. Check that task granularity supports momentum instead of slowing it down.
4. Check that the validation section matches the chosen testing strategy.
5. Check that the plan is not preserving micro-slice behavior after the topic is already open.
6. Check that the plan reduces coordination and document churn instead of increasing it.
7. Split oversized plans only when readability truly suffers.

## Handoff

After saving the plan:

- Use `subagent-driven-development` for same-session execution when the task boundaries are solid
- Use `executing-plans` for inline execution
- Skip both and execute directly if the work shrank enough that the plan is no longer needed
