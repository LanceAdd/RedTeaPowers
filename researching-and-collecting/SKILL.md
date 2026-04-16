---
name: researching-and-collecting
description: Use when work first needs factual research, inventory, comparison, source gathering, or evidence synthesis before design or execution. Best for codebase scans, legacy surface mapping, API or dependency inventory, option comparison, and gathering findings from the current project, user-specified local references, local materials, or external sources into a clear reference, discuss doc, or next-step recommendation.
---

# Researching And Collecting

## Overview

Research before decisions when the missing piece is facts, not design.

Use this skill to gather and normalize evidence, batch same-kind collection work, and turn the result into a usable handoff instead of a pile of notes.

## When To Use

Use this skill when you need to:

- inventory an existing codebase, module family, document set, API surface, or dependency area
- collect facts from several files, commands, docs, or other sources before deciding what to do
- compare multiple options, implementations, or patterns against explicit criteria
- gather findings from the current project plus user-specified local reference projects, local materials, or external sources
- turn scattered findings into one reusable research artifact
- identify gaps, unknowns, or contradictions before brainstorming or planning

Do not use this skill when:

- the work is already clear enough for direct execution
- the task is mainly collaborative design rather than fact gathering
- the investigation is a bug workflow that should use `systematic-debugging`

## Workflow

1. Define the research question, decision target, or inventory boundary.
2. Choose the smallest useful source set that can answer it.
3. Batch same-kind collection work instead of inspecting one item per loop.
4. Capture findings in a normalized structure.
5. Separate confirmed facts from inferences and open questions.
6. Synthesize patterns, gaps, risks, and recommended next steps.
7. Hand off to the right next skill or document type.

## Scope Rules

- Research only until the result can change a real decision, route, or implementation.
- Prefer one bounded pass over many tiny collection loops.
- If 3 or more same-kind items are visible, inventory them as one batch by default.
- Stop expanding the source set once added inputs no longer meaningfully change the picture.
- Call out when a conclusion is inferred instead of directly evidenced.

## Source Intake

Support these source modes:

- current project sources
- user-specified local reference projects
- user-specified local reference materials
- external sources when the task or risk justifies them

Start from the current project by default.
Bring in local references when the user names them or when comparison against another local artifact is part of the task.
Use external sources when the answer depends on information not present locally, when the user explicitly wants outside research, or when current external facts could materially change the conclusion.

Do not silently widen the source surface without a reason.

## Source Handling

Typical source buckets include:

- repository files and directories
- local reference repositories or workspaces
- existing project documents
- user-provided notes, PDFs, specs, exports, or discussion records
- command output
- test or build evidence
- API or schema references
- comparison targets such as libraries, implementations, historical variants, or external products

For each source, capture only what matters:

- what it is
- what fact it supports
- whether it is current, stale, partial, or contradictory

## Source Priority And Trust

Prefer sources in this order unless the task clearly requires a different weighting:

1. current project facts
2. user-specified local reference projects or materials
3. official external sources
4. secondary external sources

Never treat these as interchangeable:

- current implementation facts
- reference examples
- provisional discussion material
- external commentary

If two sources conflict, say so explicitly and keep the conflict visible in the output.

## External Research Guardrails

When using external sources:

- prefer official or primary sources for technical, product, API, or standards questions
- use secondary sources only to supplement or triangulate
- do not let external examples silently override current project constraints
- record the source role clearly: authoritative, comparative, historical, or anecdotal
- if the user asked for local-only research, stay local

When the task has a strong local answer already, do not expand into external search just because more sources exist.

## Evidence Labels

Label findings using these categories:

- `project-fact`
- `local-reference`
- `user-material`
- `official-external`
- `secondary-external`
- `discussion-note`
- `inference`

## Output Shapes

Choose the lightest useful output:

| Output | Use when |
|--------|----------|
| Inline summary | The findings are small and immediately actionable |
| `reference` doc | The result is a factual inventory, lookup surface, or reusable evidence base |
| `discuss` doc | The findings support a recommendation, but the decision is not yet final |
| `guide` doc | The research stabilizes into durable operating guidance |
| `todolist` | The research mainly reveals actionable follow-up items |

Use `managing-project-docs` if the right document type or split strategy is not obvious.
Write any research artifact in UTF-8.

## Handoff

After research:

- use `brainstorming` if several approaches still need design discussion
- use `shaping-work` if the findings change the delivery route
- use `writing-plans` if the work is now understood and needs a formal execution artifact
- skip directly to execution if the facts are sufficient and the next step is already clear

## Output

Produce a short research summary shaped like:

```text
Research scope: settings area loading-state behavior across the dashboard surfaces
Sources: 6 React components, 2 hooks, 1 design note
Confirmed facts:
- [project-fact] three components use the old spinner contract
- [local-reference] the reference admin panel already uses the newer loading-state shape

Open questions:
- whether the admin screen still depends on the legacy prop path

Recommendation:
- batch the four same-kind UI follow-ups together
- create docs/reference/005-settings-loading-surface.md
- then route to writing-plans only if the batch grows beyond one execution pass
```

## References

- Read [001-research-structures.md](references/001-research-structures.md) for inventory, comparison, and source-log patterns.
- Read [002-synthesis-and-handoffs.md](references/002-synthesis-and-handoffs.md) for stop rules, evidence labeling, and next-step routing.
- Read [003-source-intake-and-trust.md](references/003-source-intake-and-trust.md) for multi-source intake, priority, and external research guardrails.
