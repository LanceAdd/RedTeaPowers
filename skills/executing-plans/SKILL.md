---
name: executing-plans
description: Use when you already have a written implementation plan and want to carry it out in a separate session. Works for formal plans and lighter batch-oriented plans, as long as the execution artifact is clear enough to follow and verify.
---

# Executing Plans

## Overview

Use this skill to load an existing written plan, review it critically, execute it, and report only what fresh evidence supports.

The artifact may be a formal plan or a lighter batch-oriented plan. If the topic is already open and stable, execute in batch delivery mode rather than recreating first-slice behavior.

If subagents are available and the work has solid task boundaries, prefer `subagent-driven-development`.

## When To Use

Use this skill when:

- you already have a written plan
- the artifact is clear enough to follow and verify
- the task should now move from planning into implementation

## Do Not Use When

Do not use this skill when:

- there is no usable execution artifact yet
- the plan no longer matches reality and needs re-routing first
- the task is better handled directly inside a subagent workflow from the start

## Workflow

1. Read the plan.
2. Confirm it is still the right level of detail.
3. Raise concerns before starting if tasks are vague, wrongly split, or no longer match the topic.
4. Execute each task or batch as written.
5. Validate each task with fresh evidence before marking it complete.
6. Keep batches intact unless a blocker forces a split.
7. Once all work is done, hand off to completion verification and branch closeout.

## Execution Rules

- do not add ceremony while executing
- do not improvise scope just because the artifact exists
- if the artifact is wrong for the work, stop and re-route instead of forcing progress
- once the mainline is stable, prefer fewer stronger passes over many tiny completion updates
- do not start implementation on the shared default branch without explicit user consent

## Opened Topic Rule

When execution is finishing follow-up work on an already opened topic:

- keep one primary workstream visible
- update reusable guidance or references if the batch reveals stable patterns
- remove or archive obsolete follow-up fragments that no longer deserve to stay active
- run a real experience or real flow check early enough to influence the remaining batch

Use `../shaping-work/references/002-opened-topic-stabilization.md` when the topic may have shifted from opening work into steady delivery.

## Stop Signals

Stop and ask for help when:

- a blocker prevents execution
- the artifact no longer matches reality
- validation keeps failing
- the work needs a different route, document type, or testing strategy
- the topic needs restabilization because architecture or boundary assumptions started moving again

## Handoff

After execution:

- use `verification-before-completion` to confirm the completion evidence
- use `finishing-a-development-branch` after completion evidence is confirmed
- use `shaping-work`, `writing-plans`, or `managing-project-docs` again only if execution exposed a route or artifact problem

## References

- Use `../shaping-work/references/002-opened-topic-stabilization.md` when deciding whether execution should shift into steady batch delivery.
