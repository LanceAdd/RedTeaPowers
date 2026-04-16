---
name: researching-and-collecting
description: Use when work first needs factual research, inventory, comparison, source gathering, or evidence synthesis before design or execution. Best for codebase scans, legacy surface mapping, API or dependency inventory, option comparison, and gathering findings from the current project, user-specified local references, local materials, or external sources into a clear reference, discuss doc, or next-step recommendation.
---

# Researching And Collecting

## Overview

Use this skill when the missing piece is facts, not design.

The core job is to gather evidence, normalize the findings, and turn them into a usable handoff instead of a pile of notes.

Research only until the result can change a real decision, route, or implementation.

## When To Use

Use this skill when you need to:

- inventory an existing codebase, module family, document set, API surface, or dependency area
- collect facts from several files, commands, documents, or other sources before deciding what to do
- compare multiple options, implementations, or patterns against explicit criteria
- gather findings from the current project plus user-specified local references, local materials, or external sources
- turn scattered findings into one reusable research artifact
- identify gaps, unknowns, or contradictions before planning or design discussion

## Do Not Use When

Do not use this skill when:

- the work is already clear enough for direct execution
- the task is mainly collaborative design rather than fact gathering
- the investigation is a bug workflow that belongs in `systematic-debugging`

## Workflow

1. Define the research question, decision target, or inventory boundary.
2. Choose the smallest useful source set that can answer it.
3. Batch same-kind collection work instead of inspecting one item per loop.
4. Capture findings in a normalized structure.
5. Separate confirmed facts from inferences, contradictions, and open questions.
6. Synthesize patterns, risks, and recommended next steps.
7. Hand off to the right next skill or document type.

## Scope Rules

- prefer one bounded pass over many tiny collection loops
- if 3 or more same-kind items are visible, inventory them as one batch by default
- stop expanding the source set once added inputs no longer meaningfully change the picture
- call out when a conclusion is inferred instead of directly evidenced
- do not silently widen the source surface without a reason

## Source Handling

Start from the current project by default.

Bring in user-specified local references or materials when the task calls for comparison or the user names them.

Use external sources when:

- the answer is not available locally
- the user explicitly wants outside research
- current external facts could materially change the conclusion

For each source, capture only what matters:

- what it is
- what fact it supports
- whether it is current, stale, partial, contradictory, or inferential

If sources conflict, keep the conflict visible in the output.

## Output Shapes

Choose the lightest useful output:

| Output | Use when |
|--------|----------|
| Inline summary | The findings are small and immediately actionable |
| `reference` doc | The result is a factual inventory, lookup surface, or reusable evidence base |
| `discuss` doc | The findings expose unresolved requirement questions and execution should stay paused |
| `guide` doc | The findings support a stage-level development charter or phased development outline |
| Inline recommendation plus `TodoWrite` / `update_plan` handoff | The research mainly reveals actionable follow-up items that do not need a durable document |

Use `managing-project-docs` if the right document type or split strategy is not obvious.
Write any research artifact in UTF-8.

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

## Handoff

After research:

- use `managing-project-docs` if the findings need a durable home and the document type is not obvious
- use `brainstorming` if several approaches still need design discussion
- use `shaping-work` if the findings change the delivery route
- use `writing-plans` if the work is now understood and needs a formal execution artifact
- skip directly to execution if the facts are sufficient and the next step is already clear

## References

- Read [001-research-structures.md](references/001-research-structures.md) for inventory, comparison, and source-log patterns.
- Read [002-synthesis-and-handoffs.md](references/002-synthesis-and-handoffs.md) for stop rules, evidence labeling, and next-step routing.
- Read [003-source-intake-and-trust.md](references/003-source-intake-and-trust.md) for multi-source intake, priority, and external research guardrails.
