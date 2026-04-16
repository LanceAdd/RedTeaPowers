# New Module Development Flow

Use this reference when the work is not a small fix, but a new module, subsystem, or capability that needs a deliberate opening move before implementation.

## Goal

Open new-module work without skipping design thinking and without falling into process-heavy churn.

The default RedTeaPowers answer is still "use the lightest workflow that is safe," but new-module work usually needs a sharper sequence than ordinary feature polish or cleanup.

## When This Flow Applies

Use this flow when most of these are true:

- the work introduces a new capability or module boundary
- the module will own non-trivial behavior, data flow, or integration points
- several implementation orders are plausible
- poor early design would create rework across more than one file or subsystem

Do not use this flow for:

- small bounded changes inside an existing stable module
- obvious same-kind follow-up work after the module shape is already proven
- bug fixing that belongs in `systematic-debugging`

## Serial Flow

Treat new-module work as a serial flow unless there is a strong reason to collapse steps:

1. Route the work with `shaping-work`.
2. If the team is intentionally not entering implementation yet, keep the topic in `discuss`.
3. If the work happens inside a new delivery stage or architecture phase, record the phase-level charter in `guide`.
4. Once execution is approved, write the module `spec`.
5. If technical design details are too large for the `spec`, write a separate design record in `reference`.
6. Choose the validation strategy before execution planning when it is not already obvious.
7. Write the `plan`.
8. Execute with session task tracking in `TodoWrite` / `update_plan`.
9. Run review.
10. After review closes, write `change`.

## Document Placement

RedTeaPowers does not need a separate default `design` document type.

Place module-design material like this:

- `discuss` for requirement or scope debate before commitment
- `guide` for stage-level direction that governs several related module decisions
- `spec` for approved behavior, module boundary, capability contract, and acceptance signals
- `reference` for durable technical design explanation, architecture notes, data-flow sketches, interface mapping, or rationale that would overcrowd the `spec`
- `plan` for execution sequencing only

## Decomposition Order

Do not start with task lists.

Decompose new-module work in this order:

### 1. Business decomposition

Clarify:

- why the module exists
- which scenarios it must support
- what outcome counts as success
- what it explicitly does not own

### 2. Module design decomposition

Clarify:

- the module boundary
- responsibilities inside the boundary
- upstream and downstream integrations
- data or state flow
- exposed interfaces or contracts
- failure behavior and invariants
- the parts most likely to change later

### 3. Execution decomposition

Only after the first two are stable enough, decide:

- what the first meaningful implementation batch is
- what must be built before integration work can start
- what can wait until the mainline path is proven
- how completion will be verified batch by batch

## First Implementation Slice

For a new module, the first slice should prove the mainline path, not fake completeness.

A good first slice usually gives you:

- one viable module boundary in code
- one working happy-path flow through the module
- one real integration point exercised end to end
- enough evidence to tell whether the chosen shape is holding

Do not spend the first slice on:

- every edge case
- every adapter
- every future extension point
- exhaustive polish before the core path works

## Plan Shape After Design

Once the spec and design are stable enough, the plan should usually move through batches like:

1. Module skeleton and mainline path
2. Core rules and state handling
3. External integrations and adapters
4. Error handling, edge cases, and observability
5. Batch cleanup, consistency, and durable references

Rename or merge batches as needed, but keep them outcome-shaped and verifiable.

## Stop Signals

Stop and re-route before implementation if:

- the module boundary is still moving
- core scenarios are still being debated
- the design record keeps changing the spec instead of elaborating it
- the plan is turning into design discovery instead of execution sequencing

## Anti-Patterns

Avoid:

- writing tasks before the module boundary is clear
- hiding design decisions inside a loose checklist
- using `guide` as a generic design dump
- stuffing technical design detail into `plan`
- splitting the first implementation into many tiny ceremonial slices after the main risk is already known
