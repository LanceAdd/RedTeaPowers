# Opened Topic Stabilization

Use this reference once a first slice, pilot implementation, or initial closed loop has already opened the topic.

## Goal

Switch from early convergence into efficient batch delivery without losing the structural gains from the first slice.

The goal is not to keep proving the same direction over and over. The goal is to turn a validated opening into a stable, reusable, lower-friction workstream.

## Mainline Stable Signals

Treat the mainline as stable enough when most of these are true:

- the core path now works or is testable in a real way
- boundary and architecture decisions are no longer shifting every round
- new work is mostly same-kind follow-through, cleanup, consistency, coverage, or UX polish
- the next questions do not materially change the route
- the first slice already taught the team the core pattern

## Mode Switch

Before stabilization:

- minimize irreversible decisions
- open the topic carefully
- freeze boundaries only as needed

After stabilization:

- batch related work
- reduce document and sync churn
- unify follow-up work under one primary workstream
- validate real experience earlier
- extract reusable patterns before the topic spreads

## Batch Delivery Rules

When the topic is open:

- prefer one primary checklist, plan, or workstream per topic
- batch same-area issues instead of creating new mini-topics
- collapse same-kind polish, cleanup, and consistency work into fewer passes
- keep execution artifacts aligned with actual delivery batches

If 3 or more same-kind low-risk follow-ups are visible, they should usually become one batch.

## Systemization Outputs

Check whether the topic now needs one or more of these stable outputs:

- `guide` for how the area works
- `reference` for reusable facts, contracts, or schemas
- reusable checklist for future passes
- script for repeated maintenance or migration work
- validation rule or test strategy note for future similar changes
- canonical implementation pattern in code or docs

Do not create all of them automatically. Create only the ones that reduce future rework.

## Real Experience Verification

Once the mainline is stable enough to inspect:

- run real flow checks earlier
- inspect actual user-facing behavior before the last cleanup round
- use that evidence to steer the next batch

Do not wait until every small follow-up is done before checking whether the topic feels correct in practice.

## Stabilization Completion Signals

Treat the topic as stabilized when most of these are true:

- same-kind follow-up work is being handled in batches
- there is one clear primary workstream for the topic
- reusable guidance or reference material exists where it actually helps
- real experience checks have been performed early enough to shape the remaining work
- the team would know where to place the next related change without rediscovering structure

## Anti-Patterns

Avoid:

- opening a topic successfully, then continuing forever in thin slices
- creating one follow-up document per small subissue
- keeping old convergence-heavy rituals after the route is already clear
- delaying real UX or flow verification until the very last round
- treating batch delivery as lower quality when it is actually the correct post-stabilization mode
