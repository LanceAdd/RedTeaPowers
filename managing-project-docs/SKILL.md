---
name: managing-project-docs
description: Organize project documentation by purpose, numbering, and split strategy. Use when deciding whether to create or update guide, discuss, spec, plan, reference, change, archive, todolist, or scripts files, especially when documentation is becoming fragmented, overgrown, or hard to navigate.
---

# Managing Project Docs

## Overview

Create documentation only when it reduces confusion, preserves reusable decisions, or speeds up later work. Keep the system ordered enough to navigate without turning every small task into paperwork.

If the task is converting a legacy documentation set into this taxonomy, use `migrating-project-docs` instead of treating the whole migration as a simple doc placement decision.

## Workflow

1. Decide whether the work needs a document at all.
2. Choose the correct document type instead of defaulting to spec or plan.
3. Place the file in the standard directory for that type.
4. Apply ordered numbering with a short topic slug.
5. Split long content into an index plus parts when one file becomes hard to scan.
6. Keep links between active documents accurate as the work evolves.

## Core Rules

- Do not create a document whose only job is to satisfy ceremony.
- Prefer `todolist` or a lightweight checklist for near-term actionable work.
- Use `spec` only for approved target behavior and boundaries.
- Use `plan` only for executable implementation sequencing.
- Move reference material out of spec and plan when it starts crowding them.
- Archive inactive materials instead of leaving them mixed with active guidance.
- Read and write all project documents as UTF-8. When creating or editing docs, preserve UTF-8 encoding explicitly.

## Standard Types

| Type | Purpose |
|------|---------|
| `guide` | Big-picture orientation, strategy, or development outline |
| `discuss` | Unapproved ideas, requirement discussions, and provisional notes |
| `spec` | Approved behavior, boundaries, and decisions |
| `plan` | Actionable implementation steps |
| `reference` | Facts, schemas, API details, and lookup material |
| `change` | Per-round change log and decision trail |
| `archive` | Inactive but still valuable material |
| `todolist` | Current queue, prerequisites, and next actions |
| `scripts` | Reusable helper scripts for build, test, run, or maintenance work |

## Output

When documentation is needed, produce a short decision like:

```text
Create: docs/todolist/003-settings-cleanup.md
Why: four related tasks need a shared queue, but no formal spec or plan
Linked from: docs/change/012-april-ui-pass.md
```

## References

- Read [001-document-taxonomy.md](references/001-document-taxonomy.md) for boundaries between document types.
- Read [002-numbering-and-splitting.md](references/002-numbering-and-splitting.md) for filename, directory, and multi-file rules.
