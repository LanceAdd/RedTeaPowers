---
name: executing-plans
description: Use when you already have a written implementation plan or execution checklist and want to carry it out in a separate session. Works for formal plans and lighter batch checklists, as long as the execution artifact is clear enough to follow and verify.
---

# Executing Plans

## Overview

Load the execution artifact, review it critically, execute it, and report only what fresh evidence supports. The artifact may be a formal plan or a lighter checklist.
If the topic is already open and the mainline is stable, execute in batch delivery mode rather than recreating first-slice behavior during implementation.

Announce at start: "I'm using the executing-plans skill to implement this plan."

If subagents are available and the work has solid task boundaries, prefer `subagent-driven-development`.

## Step 1: Load And Review

1. Read the plan or checklist.
2. Confirm the artifact is still the right level of detail.
3. Raise concerns before starting if:
   - The artifact is missing critical context
   - Tasks are too vague to execute safely
   - The work should be merged, split, or re-routed
   - The topic is already stable enough for batch delivery, but the artifact still preserves fragmented follow-up work
4. If the artifact is still valid, create tracking and proceed.

## Step 2: Execute

For each task or batch:
1. Mark it in progress.
2. Execute the work as written.
3. Use the chosen validation strategy for that task.
4. Mark it complete only after fresh evidence exists.

Do not add ceremony while executing. If the artifact used batches, keep the batches intact unless a blocker forces a split.
Once the mainline is stable, prefer fewer stronger passes over many tiny completion updates.

## Step 3: Stabilize The Topic While Executing

When the plan or checklist is finishing follow-up work on an already opened topic:

- keep one primary workstream visible
- update reusable guidance or references if the batch reveals stable patterns
- remove or archive obsolete follow-up fragments that no longer deserve to stay active
- run a real experience or real flow check early enough to influence the remaining batch

Use `../shaping-work/references/002-opened-topic-stabilization.md` when deciding whether the topic has moved from opening work into steady delivery.

## Step 4: Complete Development

After all tasks or batches are complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- Use `redteapowers:finishing-a-development-branch`

## When To Stop

Stop and ask for help when:
- A blocker prevents execution
- The artifact no longer matches reality
- Validation keeps failing
- You discover the work needs a different route, document type, or testing strategy
 - The topic needs restabilization because architecture or boundary assumptions started moving again

Do not force progress through a bad plan.

## Remember

- Review the artifact critically first
- Follow the plan or checklist, not your urge to improvise scope
- Verify with the chosen evidence, not with assumptions
- Re-route when the artifact is wrong for the work
- Never start implementation on main/master without explicit user consent
- Once the mainline is stable, optimize for batch progress, lower sync cost, and early real-experience evidence

## Integration

- `redteapowers:using-git-worktrees` sets up the isolated workspace
- `redteapowers:writing-plans` creates formal plans when needed
- `redteapowers:managing-project-docs` helps when a checklist belongs in `todolist`
- `redteapowers:shaping-work` decides when a topic should switch from first-slice work into batch delivery mode
- `redteapowers:finishing-a-development-branch` completes the branch after execution
