# New Module Spec Template

Use this template when a new module has been approved for execution and the team needs one clear source of truth for what the module should do.

## Placement

Store the spec under:

```text
docs/spec/NNN-module-name.md
```

If the project already has a stronger convention, follow it.

## What Belongs Here

Keep the spec focused on:

- approved behavior
- module boundary
- scope and non-goals
- capability contract
- acceptance signals

If durable technical design explanation grows too large, move that detail into a separate `reference` document instead of overcrowding the spec.

## Suggested Structure

```markdown
# [Module Name] Spec

## Goal

[What business or product outcome this module exists to enable.]

## Scope

- In scope:
  - [capability]
  - [capability]
- Out of scope:
  - [non-goal]
  - [non-goal]

## Primary Scenarios

1. [scenario]
2. [scenario]
3. [scenario]

## Module Boundary

The module is responsible for:

- [responsibility]
- [responsibility]

The module is not responsible for:

- [responsibility outside boundary]
- [responsibility outside boundary]

## Inputs And Outputs

- Inputs:
  - [input/event/request]
- Outputs:
  - [response/state change/emitted effect]

## External Contracts

- Upstream callers:
  - [who calls the module and what they expect]
- Downstream dependencies:
  - [what the module depends on]

## Rules And Invariants

- [rule that must stay true]
- [rule that must stay true]
- [failure or rejection condition]

## Acceptance Signals

- [observable signal that the module is behaving correctly]
- [observable signal that integration works]
- [observable signal that failure handling is acceptable]

## Open Design Follow-Ups

- [design detail that still needs to be elaborated before or during planning]
```

## Writing Rules

- Make responsibilities explicit enough that a plan can be written without guessing.
- Keep scenarios concrete enough that the first implementation slice can be chosen deliberately.
- Do not turn the spec into an implementation plan.
- Do not leave placeholder requirements such as `TBD` or unnamed behavior decisions.
