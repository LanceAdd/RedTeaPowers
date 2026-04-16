# Numbering And Splitting

Use this reference to keep the document set ordered and readable.

## Numbering Rule

Prefix ordered files with a zero-padded sequence:

- `001-topic.md`
- `002-topic.md`
- `003-topic.md`

Use numbering when order matters inside a directory, especially for:
- `discuss`
- `spec`
- `plan`
- `change`
- `archive`

Keep the slug short and stable. Rename only when clarity improves enough to justify fixing links.

## Choosing The Next Number

- Pick the next available number in that directory.
- Do not reuse old numbers for new topics.
- Keep related multi-part files under the same base number when useful.
- Keep document files in UTF-8 encoding when creating, splitting, or rewriting them.

Examples:

- `007-auth-overview.md`
- `007-auth-part-01.md`
- `007-auth-part-02.md`

## Splitting Long Documents

Split a document when:
- Scrolling makes the file hard to navigate
- One file is mixing overview, reference, and change history
- Readers need different sections at different times

Use one of these patterns:

### Index plus parts

```text
docs/spec/008-checkout-overview.md
docs/spec/008-checkout-part-01-flow.md
docs/spec/008-checkout-part-02-errors.md
```

### Main doc plus references

```text
docs/spec/011-sync-engine.md
docs/reference/011-sync-engine-api.md
docs/reference/012-sync-engine-data-model.md
```

## Link Maintenance

When splitting or moving files:
- Update incoming and outgoing links
- Keep the index or main document pointing to every part
- Note important moves in `change` if active work depends on them
- Preserve UTF-8 encoding across every new or rewritten file so readers and tools see consistent text

## Anti-Patterns

Avoid:
- Huge spec files that also contain implementation plans
- One-file dumps with no stable headings
- Creating a separate spec and plan for every tiny subissue
- Unnumbered files in otherwise ordered directories
- Mixed document encodings that break readers, validators, or diffs
