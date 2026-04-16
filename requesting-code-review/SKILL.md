---
name: requesting-code-review
description: Use when a completed change, meaningful batch, risky refactor, or pre-merge branch needs focused review. Prepare the reviewer with scope, requirements, diff range, validation evidence, and open concerns so feedback targets real risks instead of generic commentary.
---

# Requesting Code Review

## Overview

Request review when fresh eyes will meaningfully reduce risk, not as empty ceremony.

Prefer review after a meaningful task boundary, batch, or branch milestone. Do not create extra review churn by asking for a separate review on every tiny edit when one bounded batch would be more useful.

## When To Request Review

Strong default moments:

- after a meaningful implementation batch
- before merging a risky or important branch
- after a complex bug fix
- when a refactor may have hidden regressions
- when you want an independent check against requirements or scope

Usually unnecessary:

- after a trivial isolated edit with obvious evidence
- before the change is coherent enough to review
- multiple times for the same write scope without new material risk

## Review Bundle

Before requesting review, prepare a small bundle containing:

- what changed
- what requirement, plan, or bug fix the change should satisfy
- what files or diff range the reviewer should inspect
- what validation evidence already exists
- any known risks, tradeoffs, or questions you want the reviewer to focus on

Keep the bundle concise. Give enough context to review the work, not your whole session history.

## Workflow

1. Choose the review point: batch, branch, risky fix, or pre-merge state.
2. Gather the review bundle.
3. Choose the reviewer path:
   - human review
   - agent or subagent review
   - both, when the work is important enough to justify it
4. Ask for review with bounded scope.
5. Route the resulting feedback through `redteapowers:receiving-code-review` before implementing comments blindly.

## For Agent-Or-Subagent Review

Use `code-reviewer.md` as the review prompt template when dispatching a reviewer agent.

Prefer including:

- `BASE_SHA` and `HEAD_SHA` when the review is diff-based
- the active plan or requirement excerpt
- the chosen validation evidence
- any specific areas where you want extra scrutiny

## Review Quality Rules

- ask for review on the real scope, not a fuzzy "look around"
- include verification evidence that already exists
- name unresolved questions instead of hiding them
- do not describe the work as complete if `verification-before-completion` has not happened yet
- keep documentation references and copied excerpts in UTF-8 text

## Output

Use a request shaped like:

```text
Review scope: settings cleanup batch
Requirements: Task 2 from docs/plan/004-settings-refresh.md
Diff range: 3d2c1ab..9f4e001
Validation so far: targeted regression test plus manual settings screen check
Focus areas: loading state regressions, mobile layout, copy consistency
```

## Integration

- `redteapowers:subagent-driven-development` and `redteapowers:executing-plans` can request review at meaningful checkpoints
- `redteapowers:receiving-code-review` handles incoming feedback
- `redteapowers:verification-before-completion` still decides whether the work is ready to be claimed as done
