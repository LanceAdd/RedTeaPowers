---
name: migrating-project-docs
description: Use when converting an existing project's legacy documents into the RedTeaPowers documentation system, especially when old notes, specs, plans, todos, research dumps, or superpowers-era files need reclassification, splitting, renumbering, link repair, archiving, and UTF-8 normalization.
---

# Migrating Project Docs

## Overview

Convert legacy project documentation into the RedTeaPowers document system without blindly rewriting everything from scratch.

Use this skill when a project already has documentation, but the current set is messy, overgrown, spec-and-plan heavy, mixed-purpose, weakly linked, poorly ordered, or still shaped by older superpowers defaults.

If the user only needs to choose a new document type for current work, use `managing-project-docs` instead. Use this skill when the task is a migration pass across existing material.

## Migration Goals

During migration:

- preserve meaning
- reduce clutter
- classify documents by purpose
- batch same-kind migrations together
- repair numbering and links
- normalize documents to UTF-8

Do not migrate documents just to satisfy ceremony. Migrate them to make the project easier to navigate and easier to execute.

## Workflow

1. Inventory the current document set.
2. Classify each document family by purpose, activity, and quality.
3. Map the family into the target RedTeaPowers document type.
4. Choose the lightest migration action that fixes the problem.
5. Execute migration in batches, not one tiny file loop at a time.
6. Repair numbering, links, and UTF-8 encoding.
7. Leave a short migration report or `change` record when the pass materially reshapes active documentation.

## Quick Start

When the user wants a first migration pass but the document set is large, start with the checklist generator:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_migration_checklist.ps1 -SourceRoot <source-root> -Output <target-markdown>
```

Use the generated checklist to:

- see the candidate document families
- review suggested target types
- spot mixed-purpose long docs
- identify batch merge or archive opportunities

Treat the generated checklist as a migration plan input, not as unquestionable truth. Review the suggestions before applying structural changes.

On Unix-like platforms, use:

```sh
sh scripts/run_migration_checklist.sh <source-root> --output <target-markdown>
```

The launcher scripts detect `python`, `python3`, or `py` when available. If no Python runtime is available, they fall back to a manual migration checklist template so the migration pass can still start.

## Step 1: Inventory The Current Set

Start by scanning the current documents and grouping them into families such as:

- requirements and behavior docs
- implementation plans and checklists
- research or notes dumps
- meeting or discussion notes
- reference materials
- historical stage summaries
- utility scripts living in docs directories

Record only what matters for migration:

- current path
- rough purpose
- whether it is active or historical
- whether it is mixed-purpose
- whether it is too long, fragmented, or duplicative

Do not over-analyze every file if a directory-level pattern is already obvious.

## Step 2: Classify By Purpose

Classify the material by what job it actually does now, not by what its filename claims.

Examples:

- a file named `spec.md` may really be `discuss`, `reference`, or `todolist`
- a file named `notes.md` may really be `reference` or `archive`
- a file named `plan.md` may really be a short active queue better stored as `todolist`

Use `references/001-legacy-mapping-signals.md` for mapping cues.

## Step 3: Choose The Migration Action

Choose one primary action per document family:

| Action | Use when |
|--------|----------|
| Keep and rename | The content is good, but the type or naming is wrong |
| Move and renumber | The content is sound, but the directory/order is wrong |
| Split | One file mixes overview, reference, active tasks, and history |
| Merge | Several small files are really one topic and should move as a batch |
| Rewrite lightly | The structure is wrong, but the substance is still useful |
| Archive | The material is historical and should remain searchable, not active |
| Drop or ignore | The file is noise, generated clutter, or no longer worth preserving |

Prefer the smallest action that produces a clean result.

## Step 4: Migrate In Batches

Do not migrate legacy docs one file at a time when a family can be handled together.

Batch by:

- same topic
- same source directory
- same target type
- same kind of cleanup

Examples:

- convert four old `notes/` files into one `reference` set
- move several active task scraps into one numbered `todolist`
- split one giant mixed document into `guide`, `reference`, and `archive`

If 3 or more same-kind low-risk document changes are visible, treat that as one migration batch by default.

## Step 5: Normalize Structure

After moving content:

- place files in the standard target directory
- apply zero-padded numbering when order matters
- keep slugs short and stable
- split long files when readability clearly suffers
- update incoming and outgoing links
- preserve or convert all migrated docs to UTF-8

Use `managing-project-docs` references for directory and numbering rules when needed.

## Step 6: Handle Superpowers-Era Material

If the project already uses older superpowers-era wording, paths, or workflow assumptions:

- migrate `superpowers` naming to `redteapowers`
- reclassify old mandatory `spec` and `plan` material into the new taxonomy
- remove old implicit brainstorm-first or TDD-first assumptions when rewriting active guidance

Read `../using-redteapowers/references/migrating-from-superpowers.md` when the source material clearly comes from that ecosystem.

## Output

Produce a short migration decision before changing the files:

```text
Migration batch: docs/spec + docs/notes cleanup
Target: guide + reference + todolist + archive
Why: the current files mix orientation, lookup material, active tasks, and stale history
Actions: split 2 files, merge 3 files, renumber active docs, archive retired notes
```

After the migration pass, leave a short summary such as:

```text
Migrated:
- docs/spec/legacy-auth.md -> docs/guide/003-auth-overview.md
- docs/notes/api-chunks.md + docs/notes/schema.md -> docs/reference/004-auth-api.md
- docs/plan/auth-tasks.md -> docs/todolist/006-auth-followups.md

Archived:
- docs/spec/auth-v1-old.md -> docs/archive/009-auth-v1-history.md

Normalized:
- repaired internal links
- renumbered affected docs
- rewrote migrated files as UTF-8
```

## Guardrails

- Do not treat every old file as worth preserving.
- Do not preserve a bad document type just because the old filename sounded official.
- Do not leave active and historical material mixed together after the pass.
- Do not create a separate spec and plan for each tiny legacy subtopic during migration.
- Do not rewrite stable reference material more than needed.
- Do not change meaning silently while "cleaning up" wording.

## References

- Read [001-legacy-mapping-signals.md](references/001-legacy-mapping-signals.md) for mapping legacy file patterns into the RedTeaPowers taxonomy.
- Read [002-migration-pass-playbook.md](references/002-migration-pass-playbook.md) for batch migration procedure, output patterns, and safety checks.
