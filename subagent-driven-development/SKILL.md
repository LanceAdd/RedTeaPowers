---
name: subagent-driven-development
description: Use when executing an implementation plan or batch checklist in the current session and the work can be divided into clear tasks or batches for fresh subagents. Best when you want same-session execution with review checkpoints but do not want to manage every edit inline.
---

# Subagent-Driven Development

## Overview

Execute a plan or checklist by dispatching a fresh subagent per task or batch, then reviewing the result before moving on. Keep the context clean, keep the batches meaningful, and avoid re-fragmenting the work into tiny loops.

Core principle: fresh subagent per task or batch, then two-stage review: scope compliance first, code quality second.

## When To Use

Use this skill when:
- You already have a plan or checklist worth executing
- Tasks or batches can be handed off independently
- You want same-session progress with review gates

Do not use this skill when:
- The work is too coupled to split safely
- The artifact is so small that direct execution is simpler
- The artifact is so vague that subagents would mostly ask clarification questions

## Process

1. Read the plan or checklist once and extract every task or batch with the needed context.
2. Create tracking for the full set of tasks or batches.
3. For each item:
   - Dispatch an implementer subagent with the full task text and context
   - Resolve questions or blockers before implementation proceeds
   - Review for scope compliance
   - Review for code quality and request external review only when the batch risk or checkpoint justifies it
   - Mark the item complete only when both reviews pass
4. After all items complete, use `verification-before-completion`, then use `finishing-a-development-branch`.

## Task And Batch Handling

- A task may be a single component or a grouped cleanup batch.
- Do not split a healthy batch into smaller tasks just to preserve artificial granularity.
- Do split a task when the implementer is blocked by scope or context.
- Parallelize only across disjoint write scopes that can be reviewed independently.
- If the plan becomes obviously wrong, stop and re-route instead of grinding through it.

## Reviews

Review in this order:

1. Scope compliance: did the implementation match the requested task or batch, with nothing important missing and no unnecessary expansion?
2. Code quality: is the implementation clean, maintainable, and appropriately verified?
3. Request additional code review only when the checkpoint is important enough to benefit from fresh outside scrutiny.

Do not start the code quality review while scope issues are still open.
Do not create review churn by requesting a separate extra review for every tiny delegated item.

## Handling Implementer Status

Implementer subagents report one of four statuses:

- `DONE`: proceed to review
- `DONE_WITH_CONCERNS`: read the concerns, then decide whether to review or adjust first
- `NEEDS_CONTEXT`: provide missing context and re-dispatch
- `BLOCKED`: change something before retrying: context, task shape, model, or route

Never ignore a blocker and never force the same failed setup to repeat.

## Advantages

- Fresh context per task or batch
- Better same-session momentum than fully manual execution
- Review catches scope drift before it compounds
- Supports both formal plans and lighter grouped checklists
- Allows meaningful batching without forcing one huge inline execution context

## Red Flags

Never:
- Start implementation on the shared default branch without explicit user consent
- Dispatch multiple implementers in parallel against the same write scope
- Make the implementer read the plan file when you can provide the relevant excerpt
- Skip either review stage
- Force TDD if the chosen validation strategy says otherwise
- Move to the next task while review issues are still open

## Integration

- `redteapowers:using-git-worktrees` sets up isolated execution
- `redteapowers:writing-plans` creates plans when a plan is warranted
- `redteapowers:choosing-test-strategy` decides the validation mode before implementation
- `redteapowers:requesting-code-review` helps when a delegated batch needs focused outside review
- `redteapowers:verification-before-completion` confirms the real completion evidence after the delegated batches land
- `redteapowers:finishing-a-development-branch` completes the branch
- `redteapowers:executing-plans` is the inline alternative for the same artifact
