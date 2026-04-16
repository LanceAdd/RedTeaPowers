---
name: brainstorming
description: Use when a request needs collaborative design before implementation, especially when requirements are unclear, multiple approaches are plausible, or system boundaries need agreement. Do not use for straightforward small changes that are already understood and ready for direct execution, batching, or session task tracking.
---

# Brainstorming Ideas Into Designs

## Overview

Use brainstorming to reduce meaningful uncertainty before implementation, not to force a spec for every small task.

Before using this skill, route the work with `shaping-work`. If the uncertainty disappears quickly, stop brainstorming and hand off immediately to execution or session task tracking.

## When To Use

Use this skill when:

- requirements are still fuzzy
- several approaches have meaningful tradeoffs
- the work changes system boundaries, workflow structure, or user experience in a non-trivial way
- the team needs alignment before implementation

## Do Not Use When

Do not use this skill when:

- the request is a bounded change with clear expected behavior
- several same-kind small issues should simply be batched and fixed
- a spec would mostly restate obvious implementation details

## Workflow

1. Explore the relevant project context: files, docs, constraints, and recent work.
2. Ask the minimum focused questions needed to remove meaningful uncertainty.
3. Propose 2-3 approaches when the choice is non-obvious.
4. Present a concise recommended direction.
5. Choose the lightest useful outcome: no doc, session task tracking, `discuss`, `guide`, `spec`, or direct handoff.

Default convergence budget:

- usually no more than 1-3 clarifying questions in one round
- prefer at most one new active artifact before execution starts
- once the path is clear, stop discussing and move the work forward

## Output Choices

End brainstorming with one of these outcomes:

| Outcome | Use when |
|---------|----------|
| Direct execution | The discussion resolved the only real uncertainty |
| Session task tracking (`TodoWrite` / `update_plan`) | The work is now clear and should move in a small batch |
| `discuss` doc | Requirements, options, or open questions still need discussion, and the work should not enter execution yet |
| `guide` doc | The result is a stage-level development charter or phased development outline |
| `spec` doc | The team has decided to execute and needs approved behavior and boundaries recorded before implementation |

Do not default to `spec`.

## Documentation

If brainstorming produces a durable document, use `managing-project-docs` to choose the right type and location.

Write any saved brainstorming artifact in UTF-8.

## Handoff

After brainstorming:

- use `writing-plans` if the chosen route needs an implementation plan
- use `choosing-test-strategy` before planning or implementation if validation is still undecided
- skip directly to execution if the work is clear and no plan is needed

## References

- Use [visual-companion.md](visual-companion.md) when mockups, diagrams, or visual options would clarify the discussion better than plain text.
- Use [spec-document-reviewer-prompt.md](spec-document-reviewer-prompt.md) when a spec draft needs focused review.
