---
name: using-redteapowers
description: Use when starting any conversation that may involve RedTeaPowers workflows. Route the request to the lightest useful skill for debugging, shaping, research, documentation, planning, or validation, and stop routing as soon as the next practical step is clear.
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, skip this skill.
</SUBAGENT-STOP>

## Overview

Use this skill as the entry router for RedTeaPowers.

Choose the lightest useful next skill, then stop routing and do the work. User instructions always win unless following them would create obvious risk.

If the request is already clear, low-risk, and ready to execute after a quick context check, do not keep routing.

## When To Use

Use this skill when:

- the request may need RedTeaPowers process help, but the right next skill is not obvious yet
- you need to choose between shaping, research, debugging, documentation, planning, or validation
- you want one quick routing pass before using the rest of the library

## Do Not Use When

Do not use this skill when:

- you are already inside a clearly chosen skill flow
- the next step is already obvious enough to execute directly
- the task is a subagent execution task rather than top-level routing

## Routing Order

Route in this order:

1. `systematic-debugging` for bugs, failures, and unexpected behavior
2. `shaping-work` for new work, mixed requests, batching decisions, or "do we need a plan/spec?" questions
3. `researching-and-collecting` when the next blocker is factual research, inventory, or comparison
4. `brainstorming` only when collaborative design is the real blocker
5. `managing-project-docs` when deciding what document to create or update
6. `migrating-project-docs` when legacy documentation needs conversion into the RedTeaPowers taxonomy
7. `choosing-test-strategy` when the validation mode is not already clear
8. `writing-plans` only when a formal execution artifact is actually needed
9. `test-driven-development` only when TDD was explicitly chosen or clearly requested

## Workflow

1. Check whether the task is already clear enough for direct execution.
2. If not, identify the first real blocker: bug, route choice, missing facts, design uncertainty, document placement, validation, or planning.
3. Route to the lightest skill that resolves that blocker.
4. Do not load heavier process just because it exists.
5. Stop routing once the next practical step is clear.

Default convergence budget:

- ask only the questions that change the route
- create at most one active new artifact before implementation unless risk clearly justifies more
- once more routing would not change the next step, execute instead

## Handoff

After routing:

- execute directly if the work is already clear enough
- use the selected skill and follow its workflow
- do not loop back here unless the work changed shape enough to need re-routing

## References

- Read [workflow-overview.md](references/workflow-overview.md) for the modernized routing, validation, and documentation model.
- Read [library-status-matrix.md](references/library-status-matrix.md) for the current keep, rewrite, and archive decisions across the library.
- Read [migrating-from-superpowers.md](references/migrating-from-superpowers.md) when converting older superpowers-based workflows, docs, or prompts into RedTeaPowers.
