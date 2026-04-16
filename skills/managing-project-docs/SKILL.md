---
name: managing-project-docs
description: Organize project documentation by purpose, numbering, and split strategy. Use when deciding whether to create or update guide, discuss, spec, plan, reference, change, archive, or scripts files, especially when documentation is becoming fragmented, overgrown, or hard to navigate.
---

# Managing Project Docs

## Overview

Create documentation only when it reduces confusion, preserves reusable decisions, or speeds up later work. Keep the system ordered enough to navigate without turning every small task into paperwork.

If the task is converting a legacy documentation set into this taxonomy, use `migrating-project-docs` instead of treating the whole migration as a simple doc placement decision.

When a project has no usable documentation structure yet, initialize the lightest useful docs tree first, then decide which concrete documents actually deserve to exist.

## Quick Chooser

Use this shortcut before doing anything heavier:

- Brand-new or nearly empty project docs:
  use the bootstrap initializer in `new:minimal` if you only need the directory skeleton, or `new:standard` if you want a navigable docs tree right away.
- Legacy repo with messy or mixed-purpose docs:
  start with `legacy:audit` to see suggested migration batches, then use `legacy:standard` only if the target RedTeaPowers tree still needs to be created.
- Existing repo with a usable docs tree:
  skip initialization and use this skill to decide the next real document type, numbering, or split.
- Single near-term task with no durable doc value:
  skip document creation and use session task tracking instead.

## Workflow

1. Decide whether the work needs a document at all.
2. If the project lacks a usable docs tree, choose the lightest matching bootstrap mode and profile first.
3. Choose the correct document type instead of defaulting to spec or plan.
4. Place the file in the standard directory for that type.
5. Apply ordered numbering with a short topic slug.
6. Split long content into an index plus parts when one file becomes hard to scan.
7. Keep links between active documents accurate as the work evolves.

## Core Rules

- Do not create a document whose only job is to satisfy ceremony.
- Prefer session task tracking in `TodoWrite` or `update_plan` for near-term actionable work that does not need a durable document.
- Use `spec` only for approved target behavior and boundaries.
- Use `plan` only for executable implementation sequencing.
- Move reference material out of spec and plan when it starts crowding them.
- Archive inactive materials instead of leaving them mixed with active guidance.
- Read and write all project documents as UTF-8. When creating or editing docs, preserve UTF-8 encoding explicitly.

## Standard Types

| Type | Purpose |
|------|---------|
| `guide` | Stage-level development charter or phased development outline |
| `discuss` | Pre-execution requirement discussion, open questions, and alternative proposals that are not entering implementation yet |
| `spec` | Approved behavior, boundaries, and decisions |
| `plan` | Actionable implementation steps |
| `reference` | Facts, schemas, API details, and lookup material |
| `change` | Per-round change log and decision trail |
| `archive` | Inactive but still valuable material |
| `scripts` | Reusable helper scripts for build, test, run, or maintenance work |

## Output

When documentation is needed, produce a short decision like:

```text
Create: docs/plan/003-settings-cleanup.md
Why: four related implementation steps need durable sequencing across sessions
Linked from: docs/change/012-april-ui-pass.md
```

## Typical Flows

Use these lightweight flows when the next move is not obvious:

- New project with little or no docs yet:
  run the bootstrap initializer in `new` mode, use `minimal` when you only want the directory skeleton, or `standard` when you want a navigable docs tree with guidance files, then decide whether the current work really needs `guide`, `spec`, `plan`, or only session task tracking.
- Legacy project with messy docs:
  run the bootstrap initializer in `legacy` mode with the `audit` profile first, review the suggested migration batches, then use `legacy:standard` only if the target RedTeaPowers tree still needs to be created before the real migration pass.
- Existing project with a working docs tree:
  skip bootstrapping and use this skill directly to place or split the next real document.

## References

- Read [001-document-taxonomy.md](references/001-document-taxonomy.md) for boundaries between document types.
- Read [002-numbering-and-splitting.md](references/002-numbering-and-splitting.md) for filename, directory, and multi-file rules.
- Read [003-bootstrap-initializer-cli.md](references/003-bootstrap-initializer-cli.md) for the recommended docs-tree bootstrap modes, profiles, and CLI behavior.
