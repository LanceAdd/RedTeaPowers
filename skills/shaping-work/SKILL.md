---
name: shaping-work
description: Route new development requests by size, uncertainty, and coupling before choosing direct execution, session task tracking, a plan, or a spec plus plan. Use when a request could be over-scoped into excessive documentation, fragmented into tiny loops, or mixed with several related small fixes.
---

# Shaping Work

## Overview

Use this skill to choose the lightest workflow that will keep the work understandable and safe without adding avoidable ceremony.

The core job is to decide between direct execution, session task tracking, a lightweight plan, or a spec plus plan.

Use a thin first slice only to open uncertainty. Once the topic is stable enough, switch quickly to batch delivery instead of staying in micro-loops.

## When To Use

Use this skill when:

- the right level of process is still unclear
- the request may be getting over-scoped into too much documentation
- several related small fixes should probably be grouped into one workstream
- you need to decide whether the work should be executed directly, tracked in `TodoWrite` / `update_plan`, planned, or specified
- you need to open a new module or subsystem and choose whether it needs `discuss`, `guide`, `spec`, or `plan`

## Do Not Use When

Do not use this skill when:

- the next step is already obvious enough to execute directly
- the main blocker is factual research rather than route choice
- the work is clearly a bug investigation that belongs in `systematic-debugging`

## Workflow

1. Read the request and current project context.
2. Group related small issues into one workstream before deciding the route.
3. Judge the work on ambiguity, coupling, scale, and urgency.
4. Apply the default convergence budget below.
5. Choose one route from the routing table.
6. If a first slice is needed, set an explicit checkpoint for batching or escalation.
7. If the topic is already open, run the stabilization check before creating more slices or documents.
8. State the route briefly, then proceed.

Default convergence budget:

- ask at most 1-3 high-value clarification questions in one round
- create at most one new active artifact before implementation unless risk clearly justifies more
- if more questions or documents would not change the route, stop converging and execute

## Routing Table

| Route | Use when | Avoid when |
|-------|----------|------------|
| Direct execution | One bounded change, clear expected result, low coordination risk | Multiple related fixes are already visible |
| Direct execution with session task tracking | Several similar small tasks can be handled together in one pass, especially when 3 or more same-kind low-risk items share area, files, or validation | Architecture or requirements are still unclear |
| Lightweight plan | Work spans multiple steps or files, but the outcome is already understood | Direct execution with session task tracking would be enough |
| Spec plus plan | Requirements are unstable, decisions are expensive, or multiple valid approaches need alignment | The work is already understood well enough to implement |

## First-Slice Rule

Use a thin first slice only to open uncertainty, not as a permanent execution style.

- re-evaluate immediately after the first slice
- if the slice confirms the direction, batch the remaining same-kind work within the next 1-2 rounds
- do not keep slicing unless new uncertainty appeared that actually changes the route
- if the topic keeps resisting batching, escalate deliberately to a plan or spec

## Opened-Topic Stabilization

Treat the mainline as stable enough to switch into batch delivery when most of these are true:

- the core path now works or is close enough to inspect meaningfully
- system boundaries are stable enough that the route is no longer changing
- the next visible work is mostly same-kind cleanup, follow-through, or consistency work
- new questions are mainly execution details rather than architectural decisions

When the topic is stable:

- switch from convergence mode to batch delivery mode
- keep one primary workstream instead of scattering follow-up documents
- batch same-area follow-up work into a small number of meaningful passes
- reduce document churn to the minimum needed for execution and reuse
- pull real experience verification forward if the mainline is already usable

## Output

Produce a short routing decision before implementation:

```text
Route: direct execution with session task tracking
Why: This request contains four related UI cleanup items with low ambiguity and shared files.
Artifacts: update `TodoWrite` / `update_plan` + implement in one pass
```

## Handoff

After shaping:

- execute directly if the route is direct execution
- use `managing-project-docs` when the route needs a durable document or an artifact placement decision
- use `writing-plans` when the route needs a formal plan
- use `brainstorming` or `researching-and-collecting` only if shaping reveals a different real blocker

## References

- Read [001-work-sizing-and-routing.md](references/001-work-sizing-and-routing.md) for the sizing signals, route examples, and escalation rules.
- Read [002-opened-topic-stabilization.md](references/002-opened-topic-stabilization.md) for switching from first-slice work into batch delivery and stable system building.
- Read [references/003-new-module-development-flow.md](references/003-new-module-development-flow.md) when the work is a new module or subsystem rather than a small bounded change.
