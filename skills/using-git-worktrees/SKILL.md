---
name: using-git-worktrees
description: Use when implementation should happen in an isolated branch workspace instead of the current checkout, especially for risky changes, parallel workstreams, delegated execution, or when the current workspace is dirty. Create a safe git worktree with directory, ignore, setup, and baseline checks that match the repository.
---

# Using Git Worktrees

## Overview

Use a git worktree when isolation will reduce risk or coordination cost.

Do not create a worktree just because one could exist. If the current workspace is already clean, isolated enough, and the user does not need branch separation, skip this skill.

## When To Use

Good reasons to use a worktree:

- risky or multi-step implementation on a separate branch
- delegated execution where another agent should not touch the current checkout
- parallel workstreams with disjoint scopes
- a dirty current workspace that should not be disturbed
- pre-merge or pre-review isolation that benefits from a clean branch workspace

Usually unnecessary:

- tiny isolated edits in an already clean branch
- work that will remain in the current checkout by user preference

## Workspace Selection

Choose the worktree location in this order:

1. Use an existing repo convention if one is already present, such as `.worktrees/` or `worktrees/`.
2. Use an explicit repository preference if project docs or local instructions define one.
3. Otherwise ask the user for a local-vs-global preference before creating a new convention.

Prefer stable conventions over inventing a new path every time.

## Safety Rules

For a project-local worktree directory:

- verify the directory is ignored before creating the worktree
- if it is not ignored, add the appropriate ignore rule before continuing
- avoid polluting the repository with nested checkout noise

For a global worktree directory:

- keep the path predictable
- include the project name in the path so multiple repos do not collide

## Setup Workflow

1. Confirm the target branch name and intended worktree path.
2. Create the worktree on a dedicated branch.
3. Run the lightest useful project setup for that repository.
4. Run the best available baseline verification so the worktree starts from known evidence.
5. Report the path, branch, and baseline result before implementation starts.

## Setup And Baseline Guidance

Project setup may include dependency install, environment bootstrap, or other repo-specific preparation.

Baseline verification should match the project and the upcoming risk. Examples:

- targeted tests
- a build or typecheck
- a smoke command
- a minimal manual or scripted check when no reliable automation exists

If baseline verification fails:

- report the failure clearly
- distinguish pre-existing failures from new setup problems when possible
- ask whether to proceed, investigate, or choose a different route

## Output

Use a report shaped like:

```text
Worktree ready: .worktrees/settings-refresh
Branch: feature/settings-refresh
Setup: pnpm install
Baseline: pnpm test --filter settings (pass)
Ready for implementation in isolated workspace
```

## Guardrails

- do not assume a directory convention when the repo is ambiguous
- do not create a project-local worktree directory that is not ignored
- do not skip baseline evidence when the whole point of the worktree is clean isolation
- do not describe isolation as complete until branch, path, and baseline status are known

## Integration

- `redteapowers:shaping-work` decides whether isolated implementation is worth the overhead
- `redteapowers:executing-plans` and `redteapowers:subagent-driven-development` may use worktrees when branch isolation helps execution
- `redteapowers:finishing-a-development-branch` handles cleanup or integration after the isolated work is complete
