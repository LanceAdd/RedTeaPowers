---
name: brainstorming
description: Use when a request needs collaborative design before implementation, especially when requirements are unclear, multiple approaches are plausible, or system boundaries need agreement. Do not use for straightforward small changes that are already understood and ready for direct execution, batching, or a simple checklist.
---

# Brainstorming Ideas Into Designs

## Overview

Clarify uncertain work before implementation. Use brainstorming to reduce ambiguity and align on approach, not to force a spec for every small task.

Before using this skill, route the work with `shaping-work`. If the work is already understood well enough to execute directly or with a checklist, do that instead.
If the key uncertainty disappears quickly, stop brainstorming and hand off immediately to execution or a todolist.
Stay within a small convergence budget unless the topic has real decision risk.

## When To Use

Use this skill when:
- Requirements are still fuzzy
- Several approaches have meaningful tradeoffs
- The work changes system boundaries, workflow structure, or user experience in a non-trivial way
- The team needs alignment before implementation

Do not use this skill when:
- The request is a bounded change with clear expected behavior
- Several same-kind small issues should simply be batched and fixed
- A spec would mostly restate obvious implementation details

## Process

1. Explore project context first: files, docs, recent work, and constraints.
2. Ask the minimum focused clarifying questions needed where uncertainty matters, usually no more than 1-3 in one round.
3. Propose 2-3 approaches when the choice is non-obvious.
4. Present a concise recommended direction.
5. Choose the right artifact for the outcome: no doc, `discuss`, `guide`, `spec`, checklist, or direct handoff to planning or execution.

Prefer the lightest outcome that preserves the useful decision.
Prefer at most one new active artifact before execution starts.

## Output Choices

End brainstorming with one of these outcomes:

| Outcome | Use when |
|---------|----------|
| Direct execution | The discussion resolved the only real uncertainty |
| Todolist or checklist | The work is now clear and should move in a small batch |
| `discuss` doc | Useful decisions were made, but the topic is not approved as a spec |
| `guide` doc | The result is a durable direction or working outline |
| `spec` doc | The behavior and boundaries need an approved reference before implementation |

Do not default to `spec`.

## Documentation

If brainstorming produces a durable document, use `managing-project-docs` to choose the right type and location.

Prefer:
- `docs/discuss/NNN-topic.md` for unresolved or provisional outcomes
- `docs/guide/NNN-topic.md` for development outlines and working guidance
- `docs/spec/NNN-topic.md` only for approved target behavior

Write any saved brainstorming artifact in UTF-8 encoding.

## Handoff

After brainstorming, choose the next step deliberately:

- Use `writing-plans` if the chosen route needs an implementation plan
- Use `choosing-test-strategy` before planning or implementation if validation is still undecided
- Skip directly to execution if the work is clear and no plan is needed

## Key Principles

- Ask only enough questions to remove meaningful uncertainty.
- Favor one good decision over performative thoroughness.
- Do not keep slicing work smaller after the topic is already understood.
- Batch related follow-up work once the first slice opens the topic.
- If the first slice settled the approach, move the remaining same-kind work into a batch within the next 1-2 rounds.
- Prefer direct execution over another discussion round once the path is clear.
- Keep outputs short unless the problem truly needs more structure.

## Visual Companion

A browser-based companion for mockups, diagrams, and visual options during brainstorming. Offer it when visual material would clarify the discussion better than plain text.

Offer it in its own message and wait for the user's response before continuing. If they decline, stay text-only.
