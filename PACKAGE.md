# RedTeaPowers Package

This repository is the current clean product cut of the RedTeaPowers skill set.

The source skill directories now live under `skills/`.

It includes only the skills currently marked `Keep` in the source library status matrix from the source reference library.

## Included Skills

- `using-redteapowers`
- `shaping-work`
- `researching-and-collecting`
- `choosing-test-strategy`
- `managing-project-docs`
- `migrating-project-docs`
- `brainstorming`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `systematic-debugging`
- `verification-before-completion`
- `using-git-worktrees`
- `requesting-code-review`
- `receiving-code-review`
- `finishing-a-development-branch`
- `test-driven-development`

## Packaging Rules

- Treat this directory as UTF-8 text by default for all documentation reads and writes.
- Install the active RedTeaPowers package as one set by copying the included directories from `skills/` into the runtime Codex skills directory as flat installable skill folders.
- Do not assume a single skill directory will work correctly when copied in isolation; active skills may reference sibling skills from the same package.
- Do not make runtime skill behavior depend on repository-root docs or files that will not ship inside the selected skill directories.
- Keep archived or experimental skills out of this package unless they are explicitly promoted.
- Use `skills/using-redteapowers/references/library-status-matrix.md` in the source library when deciding future additions or removals.
