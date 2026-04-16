# Module Design Record Template

Use this template when a new module's technical design is too large or too important to leave as short notes inside the `spec`.

This is not a new document type. In RedTeaPowers, store this as a `reference` document unless the project already uses a stronger convention.

## Placement

Default location:

```text
docs/reference/NNN-module-name-design.md
```

## When To Write It

Write a separate design record when:

- the module has several internal responsibilities that need explicit separation
- integration boundaries need diagrams or detailed explanation
- the data flow or state flow is easy to get wrong
- later contributors will need to understand why the module was shaped this way

Do not write it when a few short sections inside the `spec` already cover the real risk.

## Suggested Structure

```markdown
# [Module Name] Design Record

## Relationship To The Spec

- Spec: [path to module spec]
- This design record exists because: [why the design detail deserves its own document]

## Chosen Shape

[Short summary of the selected design approach.]

## Responsibilities

| Part | Responsibility | Does Not Own |
|------|----------------|--------------|
| [component] | [job] | [explicit non-job] |
| [component] | [job] | [explicit non-job] |

## Interfaces And Contracts

- Public entry points:
  - [interface]
- Internal seams:
  - [interface]
- Dependency contracts:
  - [interface]

## Data Or State Flow

1. [step]
2. [step]
3. [step]

## Lifecycle And Control Flow

- initialization:
  - [what happens]
- mainline path:
  - [what happens]
- failure path:
  - [what happens]

## Integration Points

- Upstream:
  - [integration]
- Downstream:
  - [integration]

## Risk Points

- [risk and why it matters]
- [risk and why it matters]

## Decisions That The Plan Must Respect

- [decision]
- [decision]

## Deferred Work

- [future idea that is intentionally not part of the first implementation]
```

## Writing Rules

- Explain the chosen shape, not every possible alternative.
- Keep design details aligned with the approved `spec`.
- Call out seams, invariants, and risk points that should shape task decomposition later.
- Do not hide implementation sequencing here; that belongs in `plan`.
