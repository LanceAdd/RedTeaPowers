---
name: shaping-work
description: Route new development requests by size, uncertainty, and coupling before choosing direct execution, a batch checklist, a plan, or a spec plus plan. Use when a request could be over-scoped into excessive documentation, fragmented into tiny loops, or mixed with several related small fixes.
---

# Shaping Work

## Overview

Route work before committing to a heavy process. Choose the lightest workflow that keeps the work understandable, testable, and worth revisiting.

Do not confuse "smallest closed loop" with "best long-term pace." Use a thin first slice to open the topic when needed, then switch quickly to efficient batch progress.
Once the mainline is stable enough, shift from architecture convergence into batch delivery mode instead of continuing topic-by-topic micro-loops.

Treat over-convergence as a delivery risk. The goal is not to eliminate uncertainty at all costs. The goal is to remove only the uncertainty that would materially change the route or implementation.

## Workflow

1. Read the request and current project context.
2. Group related small issues into one workstream before deciding the workflow.
3. Score the work on ambiguity, coupling, scale, and urgency.
4. Apply the default convergence budget below.
5. Choose one route from the table below.
6. If a thin first slice is needed, set an explicit follow-up checkpoint for batching or escalation.
7. State the route briefly, then proceed without adding heavier ceremony.
8. If the topic is already open, run the stabilization checkpoint below before creating more slices or documents.

## Default Convergence Budget

Use these defaults unless a clear exception applies:

- Ask at most 1-3 high-value clarification questions in one round.
- Create at most one new active artifact for a topic before implementation starts.
- If additional questions or documents would not change the route, stop converging and execute.
- Break this budget only when requirements are unstable, architectural choices are expensive to reverse, or the work carries unusual safety, security, or coordination risk.

## Routing Table

| Route | Use when | Avoid when |
|-------|----------|------------|
| Direct execution | One bounded change, clear expected result, low coordination risk | Multiple related fixes are already piling up |
| Batch checklist | Several similar small tasks can be handled together in one pass, especially when 3 or more same-kind low-risk items share area, files, or validation | Architecture or requirements are still unclear |
| Lightweight plan | Work spans multiple steps or files, but the outcome is already understood | A two-line todo list would be enough |
| Spec plus plan | Requirements are unstable, decisions are expensive, or multiple valid approaches need alignment | The work is already understood well enough to implement |

## First-Slice Rule

Use a thin first slice only to open uncertainty, not as a permanent execution style.

- After the first slice, re-evaluate immediately.
- If the slice confirms the direction, batch the remaining same-kind work within the next 1-2 rounds.
- Do not create a second or third tiny slice unless new uncertainty appeared that actually changes the route.
- If the work keeps resisting batching after several slices, escalate deliberately to a plan or spec instead of staying in endless micro-loops.

## Opened-Topic Stabilization Checkpoint

Run this checkpoint once a first slice or initial implementation has already opened the topic.

Treat the mainline as stable enough to switch modes when most of these are true:

- the core path now works or is close enough to inspect meaningfully
- system boundaries are frozen enough that the route is no longer changing
- the next visible work is mostly same-kind cleanup, follow-through, or consistency work
- new questions are no longer architectural and mainly affect execution details

When the mainline is stable:

- switch from convergence mode to batch delivery mode
- keep one primary workstream for the topic instead of scattering follow-up docs
- batch same-area follow-up work into a small number of meaningful passes
- reduce document churn to the minimum needed for execution and future reuse
- pull real experience verification forward instead of waiting until the very end

See [002-opened-topic-stabilization.md](references/002-opened-topic-stabilization.md) for the detailed mode switch, systemization outputs, and completion signals.

## Guardrails

- Batch same-kind small issues instead of creating one micro-loop per issue.
- Default to a batch checklist when 3 or more same-kind low-risk items are visible.
- Do not force a separate spec or plan for every subtopic.
- Do not stay in endless "minimal next slice" mode after the topic is already understood.
- Re-route when the work grows or shrinks. A lightweight plan can replace a spec-heavy flow, and direct execution can expand into a batch checklist.
- Prefer one visible workstream per topic over scattered document fragments.
- Once the topic is open and stable, optimize for batch progress and systemization rather than more edge freezing.
- Do not delay real user-flow or real experience checks until the last possible moment if the mainline is already usable.

## Output

Produce a short routing decision before implementation:

```text
Route: batch checklist
Why: This request contains four related UI cleanup items with low ambiguity and shared files.
Artifacts: update todolist + implement in one pass
```

## References

- Read [001-work-sizing-and-routing.md](references/001-work-sizing-and-routing.md) for the sizing signals, route examples, and escalation rules.
- Read [002-opened-topic-stabilization.md](references/002-opened-topic-stabilization.md) for switching from first-slice work into batch delivery and stable system building.
