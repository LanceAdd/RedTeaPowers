---
name: writing-plans
description: Use when work actually needs a written implementation plan across multiple steps, files, or contributors. Default to session task tracking for related small work, and do not use when direct execution is enough or a formal plan would only restate obvious next actions.
---

# Writing Plans

## Overview

Write a plan only when planning will materially reduce confusion, coordination cost, or execution risk.

Default to the smallest artifact that keeps execution moving:

- direct execution when the next step is already clear
- session task tracking in `TodoWrite` / `update_plan` when the work is a visible batch of related small tasks
- formal plan only when the work would be meaningfully harder to execute without one

Before using this skill, route the work with `shaping-work`. If the validation strategy is not decided yet, use `choosing-test-strategy` before finalizing the plan.

## When To Use

Use this skill when:

- the work spans multiple files, steps, or milestones
- ordering matters
- another agent or future session needs a stable execution artifact
- simple session task tracking would be too vague to guide the work safely

## Do Not Use When

Do not use this skill when:

- direct execution is already clear enough
- direct execution with session task tracking is enough
- the plan would only restate obvious same-kind follow-up work

If session task tracking is enough, keep the tasks in `TodoWrite` / `update_plan` and execute directly instead of writing a document.

## Plan Or Session Tracking

Start by assuming direct execution or session task tracking is enough. Escalate to a formal plan only when execution would otherwise become unclear.

Use session task tracking when:

- the work is a batch of related small changes
- the next actions are already obvious
- fine-grained planning would cost more than it saves
- the remaining same-kind work should be finished in one coordinated pass

Use a formal plan when:

- the work spans multiple steps, files, or contributors
- sequencing or dependencies are easy to get wrong
- the task boundary needs a durable artifact for handoff or later reuse
- the topic is large enough that session task tracking would hide real risk

## Workflow

1. Confirm that a formal plan is actually needed.
2. Define the goal, scope, chosen validation strategy, and execution mode.
3. Group the work into meaningful tasks or batches.
4. Include the files or areas involved, key dependencies, and completion checkpoints.
5. Keep the plan as short as possible while still executable.
6. If the topic is already open, plan the next meaningful batch instead of preserving first-slice behavior.
7. Save the plan, then hand off to execution.

## Plan Structure

Every formal plan should make these things explicit:

- goal and scope
- validation strategy
- execution mode
- files or areas expected to change
- what each task or batch is responsible for
- completion checkpoints
- what not to expand or overbuild
- UTF-8 for any written plan artifact

Keep tasks execution-shaped:

- group related work into meaningful batches
- collapse same-kind low-risk fixes into one task when they share area or validation
- prefer a few strong tasks over a wall of tiny steps
- include only as much detail as the executor actually needs

Use smaller sub-steps only when sequencing is easy to get wrong.

## Opened Topic Rule

If a first slice already proved the direction, the plan should shift into stabilization mode:

- define one primary workstream for the topic
- batch same-area follow-up work into a small number of passes
- name any reusable outputs that should come out of the batch
- pull real experience verification forward enough to affect the remaining work

Use `../shaping-work/references/002-opened-topic-stabilization.md` for the detailed mode-switch rules.

## Guardrails

- Do not write placeholder planning such as `TBD`, `TODO`, or unnamed validation.
- Do not create separate tasks only to preserve fake granularity.
- Do not write a formal plan when session task tracking would do the job.
- Split oversized plans only when readability truly suffers.

## Handoff

After saving the plan:

- use `subagent-driven-development` for same-session execution when task boundaries are solid
- use `executing-plans` for inline execution
- skip both and execute directly if the work shrank enough that the plan is no longer needed

## References

- Use [references/001-new-module-plan-template.md](references/001-new-module-plan-template.md) when planning implementation for a newly designed module or subsystem.
- Use `../shaping-work/references/002-opened-topic-stabilization.md` when planning work that has already moved past the first slice.
- Use [plan-document-reviewer-prompt.md](plan-document-reviewer-prompt.md) when the plan needs a focused review pass.
