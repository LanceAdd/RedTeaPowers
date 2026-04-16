---
name: shaping-work
description: Route new development requests by size, uncertainty, and coupling before choosing direct execution, a batch checklist, a plan, or a spec plus plan. Use when a request could be over-scoped into excessive documentation, fragmented into tiny loops, or mixed with several related small fixes.
---

# Shaping Work

## Overview

Route work before committing to a heavy process. Choose the lightest workflow that keeps the work understandable, testable, and worth revisiting.

Do not confuse "smallest closed loop" with "best long-term pace." Use a thin first slice to open the topic when needed, then switch quickly to efficient batch progress.

## Workflow

1. Read the request and current project context.
2. Group related small issues into one workstream before deciding the workflow.
3. Score the work on ambiguity, coupling, scale, and urgency.
4. Choose one route from the table below.
5. State the route briefly, then proceed without adding heavier ceremony.

## Routing Table

| Route | Use when | Avoid when |
|-------|----------|------------|
| Direct execution | One bounded change, clear expected result, low coordination risk | Multiple related fixes are already piling up |
| Batch checklist | Several similar small tasks can be handled together in one pass | Architecture or requirements are still unclear |
| Lightweight plan | Work spans multiple steps or files, but the outcome is already understood | A two-line todo list would be enough |
| Spec plus plan | Requirements are unstable, decisions are expensive, or multiple valid approaches need alignment | The work is already understood well enough to implement |

## Guardrails

- Batch same-kind small issues instead of creating one micro-loop per issue.
- Do not force a separate spec or plan for every subtopic.
- Do not stay in endless "minimal next slice" mode after the topic is already understood.
- Re-route when the work grows or shrinks. A lightweight plan can replace a spec-heavy flow, and direct execution can expand into a batch checklist.
- Prefer one visible workstream per topic over scattered document fragments.

## Output

Produce a short routing decision before implementation:

```text
Route: batch checklist
Why: This request contains four related UI cleanup items with low ambiguity and shared files.
Artifacts: update todolist + implement in one pass
```

## References

- Read [001-work-sizing-and-routing.md](references/001-work-sizing-and-routing.md) for the sizing signals, route examples, and escalation rules.
