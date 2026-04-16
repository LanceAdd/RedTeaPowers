---
name: finishing-a-development-branch
description: Use when implementation has already been verified and you need to decide how to integrate, preserve, or discard the current branch or worktree. Present clear merge, PR, keep, or discard options after the chosen validation evidence is complete.
---

# Finishing a Development Branch

## Overview

Use this skill after the work has already passed the relevant completion gate.

Do not assume "all tests pass" is the only acceptable finish state. The required evidence depends on the chosen validation strategy and should already be confirmed through `verification-before-completion`.

Announce at start: "I'm using the finishing-a-development-branch skill to complete this work."

## Entry Gate

Before presenting branch options, confirm that completion evidence already exists for this session.

If that evidence is missing or unclear:

- stop
- use `redteapowers:verification-before-completion`
- return only after the completion claim is actually supported

Do not use this skill as a substitute for verification.

## Workflow

1. Confirm the branch or worktree to finish.
2. Identify the likely base branch and current repository state.
3. Present the four finish options below.
4. Execute the chosen option safely.
5. Clean up the branch or worktree only when that option truly calls for it.

## Present These Options

Present exactly these options:

```text
Implementation is verified. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is for now
4. Discard this work
```

Do not turn this into an open-ended "what next?" question.

## Option Rules

### Option 1: Merge locally

- switch to the base branch safely
- update it if the workflow calls for that
- merge the feature branch
- run the required post-merge verification if the merge itself changes the evidence surface
- delete the merged branch only when it is safe to do so
- remove the worktree if it is no longer needed

### Option 2: Push and create a PR

- push the feature branch to the remote
- create the PR with a concise summary and the real validation evidence
- keep the branch and worktree unless the user explicitly wants immediate cleanup after the PR is created

### Option 3: Keep the branch as-is

- report the branch name and worktree path
- leave the branch and worktree intact
- do not perform cleanup

### Option 4: Discard the work

Require explicit confirmation before destructive cleanup.

Use a confirmation shaped like:

```text
This will permanently delete:
- branch <name>
- worktree <path>
- unmerged local commits on this branch

Type 'discard' to confirm.
```

Only proceed after exact confirmation.

## Guardrails

- never claim the branch is ready if completion evidence is still missing
- never delete work without explicit confirmation
- never force-push without explicit user consent
- never assume PR creation means local cleanup is desired
- never hide what branch, base branch, or worktree you are operating on

## Integration

- `redteapowers:verification-before-completion` confirms the work is actually ready to close out
- `redteapowers:using-git-worktrees` may have created the worktree that now needs cleanup
- `redteapowers:executing-plans` and `redteapowers:subagent-driven-development` should hand off here only after verification
