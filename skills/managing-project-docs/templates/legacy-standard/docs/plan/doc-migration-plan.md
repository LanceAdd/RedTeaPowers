# Docs Migration Plan

Created: {{GENERATED_AT}}

## Goal

- Normalize legacy documentation into the RedTeaPowers taxonomy without changing meaning silently.

## Suggested Batches

1. Inventory the current doc families and identify active versus historical material.
2. Decide which families should become `discuss`, `spec`, `plan`, `reference`, `change`, or `archive`.
3. Migrate one same-kind batch at a time, then repair links and numbering.

## Checks

- Confirm active docs remain easy to find.
- Keep migrated files in UTF-8.
- Leave a short migration summary in `{{DOCS_ROOT}}/change/`.
