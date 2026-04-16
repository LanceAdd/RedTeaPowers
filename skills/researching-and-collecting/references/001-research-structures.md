# Research Structures

Use these structures when the research pass needs more shape than an inline note.

## Inventory Pattern

Use for:

- module or directory scans
- endpoint lists
- dependency surveys
- legacy surface mapping

Recommended fields:

| Field | Meaning |
|-------|---------|
| Item | the thing being inventoried |
| Location | where it lives |
| Current role | what it appears to do |
| Evidence | what source supports that understanding |
| Status | active, stale, duplicate, unclear, or historical |
| Notes | only the useful follow-up detail |

## Comparison Pattern

Use for:

- option selection
- implementation comparison
- old-vs-new pattern review

Recommended fields:

| Option | Strengths | Risks | Fit for current need | Evidence |
|--------|-----------|-------|----------------------|----------|

Keep criteria explicit. Do not compare options against shifting hidden standards.

## Source Log Pattern

Use when the source set is large or mixed.

Recommended fields:

| Source | Type | What it tells us | Reliability | Follow-up |
|--------|------|------------------|-------------|-----------|

This helps separate:

- current sources from stale ones
- direct evidence from interpretation
- useful sources from noise

## Split Rule

When one research document starts mixing too many jobs:

- move stable factual material into `reference`
- keep pre-execution requirement questions and unresolved recommendation debate in `discuss`
- move durable execution work into `plan`, and keep very short-lived next actions in `TodoWrite` / `update_plan`

Do not let one long research note become an all-purpose dump.
