---
name: choosing-test-strategy
description: Choose an appropriate validation strategy before implementation or planning. Use when deciding whether work needs TDD, regression tests, integration checks, manual verification, exploratory coding, or no immediate tests instead of defaulting to a single testing doctrine.
---

# Choosing Test Strategy

## Overview

Choose the cheapest validation strategy that still protects the work from the real failure mode. Decide the testing approach before writing the plan or implementation, not after habits have already taken over.

TDD is one valid strategy, not the default answer to every task.

## Workflow

1. Identify the real risk: logic bugs, integration breakage, regressions, UX mismatch, or pure exploration.
2. Choose one primary validation strategy from the table below.
3. Add secondary checks only when the first strategy leaves an exposed risk.
4. State the chosen strategy before planning or implementation.
5. Re-evaluate if the work changes shape.

## Strategy Table

| Strategy | Use when | Typical evidence |
|----------|----------|------------------|
| TDD | Behavior is clear, logic is local, and tests can drive the interface | Failing test first, then passing test |
| Regression test | A bug already exists and needs a durable guardrail | Reproduction test that fails before the fix and passes after |
| Integration check | Components may work alone but fail together | End-to-end flow, API call, build, or system test |
| Manual verification | UX, copy, layout, or exploratory interaction matters most | Screens, recorded checks, or explicit manual steps |
| Exploration first | You are still learning the shape of the solution | Notes, spikes, or limited proof-of-concept evidence |

## Guardrails

- Do not force TDD when the interface is still being discovered.
- Do not skip all verification for durable or risky changes.
- Mix strategies across layers when needed. For example, use manual verification for UI polish and a regression test for a bug in the same feature.
- Let the chosen strategy drive the completion evidence later.

## Output

Produce a short testing decision before the work starts:

```text
Primary strategy: regression test
Secondary strategy: manual verification
Why: The bug is known and easy to reproduce, but the visible UI state still needs a human check.
```

## References

- Read [001-testing-strategy-matrix.md](references/001-testing-strategy-matrix.md) for selection heuristics, combinations, and examples.
