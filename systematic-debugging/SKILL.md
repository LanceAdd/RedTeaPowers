---
name: systematic-debugging
description: Use when encountering a bug, failing test, flaky behavior, broken integration, or any unexpected technical result before proposing fixes. Keep the investigation evidence-based, isolate the real cause, and only then apply the smallest safe correction with the right validation.
---

# Systematic Debugging

## Overview

Debugging is an investigation skill, not a sequence of guesses.

Core principle: isolate the cause before changing the code. Keep the loop short when the evidence is clear, but never skip the evidence.

For obvious single-point mistakes, a short investigation is enough. For unstable or cross-boundary failures, slow down and gather better evidence before touching implementation.

## Workflow

1. Read the failure carefully.
2. Reproduce it or gather enough evidence to define the failure surface.
3. Trace where the wrong value, state, timing, or configuration first appears.
4. Compare the broken path with a working path when the pattern is not obvious.
5. State one concrete root-cause hypothesis.
6. Test that hypothesis with the smallest useful probe.
7. Fix the cause, not the symptom.
8. Re-run the failing path and the chosen validation before claiming success.

## Investigation Rules

- Do not stack speculative fixes.
- Do not change multiple variables at once unless the batch itself is the smallest testable probe.
- Do not call it root cause until you can explain why the failure happens.
- If you cannot reproduce the issue yet, gather logs, inputs, environment facts, or timing evidence instead of guessing.
- If three fix attempts have already failed, question the architecture or boundary assumptions before trying a fourth.

## Fast Path For Obvious Failures

Use the fast path only when the evidence already isolates one concrete mistake such as:

- wrong import or file path
- inverted condition
- incorrect config key
- bad variable or field mapping
- missing argument or dependency wiring

In those cases:

1. name the cause plainly
2. apply the smallest safe fix
3. verify the original failure path
4. verify the surrounding risk with the chosen validation

## Cross-Boundary Failures

When the issue crosses components, services, processes, or environments:

- inspect inputs and outputs at each boundary
- verify config and environment propagation
- find the first boundary where reality diverges from expectation
- fix the upstream cause when possible instead of patching downstream fallout

## Validation

After isolating the cause:

- choose the lightest validation that protects the real risk
- use `redteapowers:choosing-test-strategy` if the right validation mode is not obvious
- use `redteapowers:verification-before-completion` before claiming the bug is fixed

Good debugging evidence may include:

- a reliable reproduction
- a failing and then passing regression test
- a build or integration check
- explicit manual verification steps
- targeted logs or traces that show the failure disappearing for the right reason

## Stop Signals

Stop and reset the investigation when you catch yourself doing any of these:

- proposing a fix before naming the cause
- bundling several guesses into one patch
- saying "it is probably X"
- relying on old test output instead of fresh evidence
- repeating the same failed idea with small wording changes

## Output

Before fixing, produce a short debugging statement such as:

```text
Observed failure: settings save returns 500 after the new auth refactor.
Current evidence: token is present in the UI but missing at the API boundary.
Root-cause hypothesis: the fetch wrapper stopped forwarding the auth header in the new call path.
Next probe: compare the working profile update request with the failing settings request.
```

## References

Read these only when the situation calls for them:

- `root-cause-tracing.md` for deeper tracing patterns
- `condition-based-waiting.md` for race conditions, flake, and timing issues
- `defense-in-depth.md` for layered fixes after the actual cause is known
- `find-polluter.sh` for isolation help in polluted test suites
