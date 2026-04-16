# New Module Plan Template

Use this template when a new module already has an approved `spec` and enough design clarity to enter implementation planning.

## Inputs

Before writing the plan, make sure these inputs exist and are stable enough:

- the module `spec`
- any separate design record in `reference`, if one was needed
- the chosen validation strategy, or a deliberate reason why it is obvious

## Placement

Default location:

```text
docs/plan/NNN-module-name.md
```

## Plan Goal

Convert the approved module boundary and design into a small number of executable, verifiable batches.

Do not restate the whole spec. Use the plan to sequence implementation.

## Suggested Structure

```markdown
# [Module Name] Implementation Plan

**Goal:** [what implementation completion should achieve]
**Scope:** [what this plan covers]
**Inputs:** [spec path] + [design record path if any]
**Validation:** [chosen strategy]
**Execution mode:** [direct | inline | subagent-driven]

## Task 1: Establish module skeleton and mainline path

**Why:** [why this comes first]

**Areas:**
- [area/file group]
- [area/file group]

**Do:**
- [action]
- [action]

**Verify:**
- [verification]

**Exit:**
- [observable completion checkpoint]

## Task 2: Implement core rules and state handling

...

## Task 3: Add integrations and adapters

...

## Task 4: Close error handling, edge cases, and observability

...

## Task 5: Batch cleanup and durable follow-through

...
```

## Decomposition Rules

Prefer batches shaped by outcome:

- skeleton and mainline path
- core rules and state transitions
- external integrations
- edge conditions and failure handling
- durable cleanup or documentation updates

Do not decompose by:

- one file per task
- one function per task
- arbitrary tiny steps that do not leave the module in a meaningfully better state

## Batch Quality Check

A task is shaped well when:

- it has a clear purpose
- its boundaries are understandable
- its validation is explicit
- its exit condition leaves the module more complete, not just more busy

## Anti-Patterns

Avoid:

- discovering module design for the first time inside the plan
- leaving integration work unnamed
- mixing future optional extensions into the first implementation batches
- writing "wire everything up" as a vague catch-all task
