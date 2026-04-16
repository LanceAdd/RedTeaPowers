# Migration Pass Playbook

Use this playbook when performing a legacy documentation migration pass.

## Goal

Reshape an existing document set into the RedTeaPowers taxonomy with the least necessary rewriting.

## Recommended Pass Order

1. Inventory the current files
2. Group them into migration families
3. Choose target document types
4. Choose migration actions
5. Execute the migration in batches
6. Repair numbering and links
7. Normalize UTF-8
8. Leave a short migration summary

## Migration Families

Group by the cleanup pattern, not just by file extension.

Examples:

- old spec-heavy folder that really contains phase-guide, reference, and archive material
- notes folder that should become reference plus discuss
- several task scraps that should merge into one plan
- old roadmap and plan docs that should become archive plus a fresh active plan

## Batch-First Rule

If 3 or more same-kind low-risk document actions are visible, migrate them as one batch by default.

Examples:

- rename and renumber several active `todo` files together
- move multiple stale plans into `archive` in one pass
- merge related API notes into one `reference` set

Do not preserve fake granularity by migrating each tiny file in isolation.

## Action Checks

For each batch, check:

- Are the source files still active?
- Are they mixed-purpose?
- Are they too long?
- Are they duplicated?
- Are they misnamed?
- Are they in the wrong directory?
- Are links likely to break?
- Is the content already UTF-8?

## Safe Rewrite Rules

- Preserve approved meaning unless the migration explicitly updates it.
- Rewrite structure before rewriting substance.
- Move stable facts with minimal paraphrase.
- Archive stale content instead of force-fitting it into active guidance.
- Prefer one good migration pass over repeated tiny cleanup rounds.

## Recommended Outputs

### Before execution

Write a short migration decision:

```text
Migration batch: docs/notes + docs/spec cleanup
Targets: reference + guide + archive
Actions: merge 3 files, split 1 file, archive 2 stale docs
```

### After execution

Write a short summary or `change` entry:

```text
Completed migration:
- merged old API notes into docs/reference/005-payments-api.md
- split docs/spec/payments.md into guide + spec + reference when it mixed phase charter, approved behavior, and lookup material
- moved retired launch notes into docs/archive/011-payments-launch-history.md
- updated links and renumbered affected files
- rewrote migrated files as UTF-8
```

## Link Repair

After moving or splitting files:

- update incoming and outgoing links
- update index docs or parent docs
- keep active docs pointing to new references
- add a `change` note when the migration materially changes active navigation

## UTF-8 Rule

Treat encoding normalization as part of the migration, not as optional cleanup.

Every migrated or rewritten document should end in UTF-8.

If a legacy file looks corrupted, preserve the source, diagnose the encoding carefully, and only then rewrite the migrated target.

## Escalation Rules

Escalate from a simple migration pass into heavier process only when:

- the legacy docs contain unresolved product decisions
- multiple target structures are plausible and expensive to unwind
- the migration would silently change approved behavior
- the docs reveal that implementation scope is still unstable

When that happens:

- use `brainstorming` for unresolved design decisions
- use `managing-project-docs` for target doc placement
- use `writing-plans` if the migration itself becomes multi-stage work
