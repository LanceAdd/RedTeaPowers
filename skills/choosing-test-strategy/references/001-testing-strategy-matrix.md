# Testing Strategy Matrix

Use this reference when choosing between TDD, regression, integration, manual checks, or exploration.

## Decide From Risk

Answer these questions quickly:

1. Is the target behavior already clear?
2. Is the change mostly local logic or mostly system interaction?
3. Is the main risk "wrong code" or "wrong user experience"?
4. Is the work exploratory enough that tests would harden the wrong shape too early?
5. What evidence will actually convince someone the work is done?

## Strategy Fit

| Situation | Primary strategy | Notes |
|-----------|------------------|-------|
| Small, well-understood logic change | TDD | Good when the expected interface is stable |
| Existing bug with reproducible failure | Regression test | Often the best fit for bug fixes |
| Cross-service, async, config, or environment change | Integration check | Unit tests alone will not prove the work |
| Visual polish, UX, copy, or animation change | Manual verification | Pair with screenshots or explicit check steps |
| Early spike or uncertain design | Exploration first | Limit the scope and add durable tests later if the code survives |

## Combination Patterns

Use `regression test + manual verification` when:
- A bug fix changes visible UI
- The logic can be guarded automatically but the final state still needs a human eye

Use `integration check + targeted unit or regression test` when:
- The full path is risky
- One critical rule inside the path still deserves a stable automated check

Use `exploration first -> follow-up regression or TDD` when:
- The first round is mainly for discovery
- The code will remain in the product after the shape becomes clear

## Skip Or Delay Tests Carefully

Delay durable tests only when:
- The code is a short-lived spike
- The work is still searching for the right abstraction
- The cost of writing tests now would mostly lock in a bad interface

If the code remains after the exploration round, pick a durable strategy before calling the work complete.

## Completion Evidence

Match the evidence to the strategy:

- `TDD`: show the targeted test passing after being used to drive implementation
- `Regression test`: show the reproduction is now covered and passes
- `Integration check`: show the command, flow, or environment-level check succeeding
- `Manual verification`: show the steps completed and what was visually or behaviorally confirmed
- `Exploration first`: clearly say the work is exploratory and what still needs durable validation

## Examples

```text
Task: Fix a form validator that accepts an empty email.
Primary: regression test
Why: known bug with stable expected behavior
```

```text
Task: Try two interaction patterns for a new panel before choosing one.
Primary: exploration first
Secondary: manual verification
Why: the design is still moving
```
