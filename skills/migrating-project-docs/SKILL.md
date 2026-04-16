---
name: migrating-project-docs
description: Use when converting an existing project's legacy documents into the RedTeaPowers documentation system, especially when old notes, specs, plans, task queues, research dumps, or superpowers-era files need reclassification, splitting, renumbering, link repair, archiving, and UTF-8 normalization.
---

# Migrating Project Docs

## Overview

Use this skill for migration passes across existing documentation, not for choosing the document type for new work.

The goal is to convert a messy or outdated document set into the RedTeaPowers taxonomy without blindly rewriting everything from scratch.

Migrate only when it will make the project easier to navigate and easier to execute.

## When To Use

Use this skill when:

- a project already has legacy documentation that is messy, mixed-purpose, weakly linked, poorly ordered, or overly spec-and-plan heavy
- old notes, specs, plans, task queues, or research dumps need reclassification
- documentation families need splitting, merging, renumbering, archiving, or UTF-8 normalization
- superpowers-era document structure or wording still shapes the active docs

## Do Not Use When

Do not use this skill when:

- the user only needs to decide what type of document to create for current work
- the task is a simple doc-placement decision better handled by `managing-project-docs`
- there is no real migration batch, only a single straightforward edit

## Migration Goals

During migration:

- preserve meaning
- reduce clutter
- classify documents by purpose
- batch same-kind migrations together
- repair numbering and links
- normalize migrated documents to UTF-8

## Workflow

1. Inventory the current document set.
2. Group documents into families by topic, purpose, and activity.
3. Map each family into the target RedTeaPowers document type.
4. Choose the lightest migration action that fixes the problem.
5. Execute migration in batches, not one tiny file loop at a time.
6. Normalize numbering, links, placement, and UTF-8 encoding.
7. Leave a short migration summary or `change` record when the pass materially reshapes active docs.

## Inventory And Classification

Classify documents by what job they actually do now, not by what their filenames claim.

Record only what matters for migration:

- current path
- rough purpose
- whether the material is active or historical
- whether it is mixed-purpose, duplicated, too long, or too fragmented

Do not over-analyze every file if a directory-level pattern is already obvious.

## Migration Actions

Choose one primary action per document family:

| Action | Use when |
|--------|----------|
| Keep and rename | The content is good, but the type or naming is wrong |
| Move and renumber | The content is sound, but the directory or order is wrong |
| Split | One file mixes overview, reference, active tasks, and history |
| Merge | Several small files are really one topic and should move as a batch |
| Rewrite lightly | The structure is wrong, but the substance is still useful |
| Archive | The material is historical and should stay searchable, not active |
| Drop or ignore | The file is noise, generated clutter, or no longer worth preserving |

Prefer the smallest action that produces a clean result.

## Batch Rules

- batch by same topic, same source directory, same target type, or same kind of cleanup
- if 3 or more same-kind low-risk document changes are visible, treat that as one migration batch by default
- do not migrate legacy docs one file at a time when a family can be handled together

## Normalization Rules

After moving content:

- place files in the standard target directory
- apply zero-padded numbering when order matters
- keep slugs short and stable
- split long files only when readability clearly suffers
- update incoming and outgoing links
- preserve or convert all migrated docs to UTF-8

Use `managing-project-docs` when you need directory, numbering, or split rules for the target set.

## Superpowers-Era Material

If the source material clearly comes from older superpowers defaults:

- migrate `superpowers` naming to `redteapowers`
- reclassify old mandatory `spec` and `plan` material into the newer taxonomy
- remove old implicit brainstorm-first or TDD-first assumptions when rewriting active guidance

Read `../using-redteapowers/references/migrating-from-superpowers.md` when that migration layer matters.

## Output

Produce a short migration decision before changing files:

```text
Migration batch: docs/spec + docs/notes cleanup
Target: guide + reference + plan + archive
Why: the current files mix stage guidance, lookup material, active execution work, and stale history
Actions: split 2 files, merge 3 files, renumber active docs, archive retired notes
```

After the pass, leave a short summary of what was migrated, archived, and normalized.

## Guardrails

- Do not preserve a bad document type just because the old filename sounded official.
- Do not leave active and historical material mixed together after the pass.
- Do not create a separate spec and plan for each tiny legacy subtopic during migration.
- Do not rewrite stable reference material more than needed.
- Do not change meaning silently while cleaning up structure or wording.

## Handoff

After migration:

- use `managing-project-docs` if the cleaned document set still needs target placement or split decisions
- use `writing-plans` or `shaping-work` if the migration reveals fresh execution work
- keep the migration summary with the active docs when the pass materially changes project navigation

## References

- Read [001-legacy-mapping-signals.md](references/001-legacy-mapping-signals.md) for mapping legacy file patterns into the RedTeaPowers taxonomy.
- Read [002-migration-pass-playbook.md](references/002-migration-pass-playbook.md) for batch migration procedure, output patterns, and safety checks.
- Use [003-manual-migration-plan-template.md](references/003-manual-migration-plan-template.md) or the local scripts when a large migration needs a written plan-first starting point.
