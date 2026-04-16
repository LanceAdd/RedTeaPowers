---
name: systematic-debugging
description: Use when encountering a bug, failing test, flaky behavior, broken integration, or any unexpected technical result before proposing fixes. Keep the investigation evidence-based, isolate the real cause, and only then apply the smallest safe correction with the right validation.
---

# Systematic Debugging

## Overview

Debugging is an investigation skill, not a sequence of guesses.

The goal is to isolate the cause before changing code. Keep the loop short when the evidence is clear, but do not skip the evidence.

## When To Use

Use this skill when:

- a bug, failing test, flaky behavior, broken integration, or unexpected technical result needs investigation
- the failure cause is not yet isolated
- the safest next step is to gather evidence before proposing a fix

## Do Not Use When

Do not use this skill when:

- the issue is already isolated to one obvious concrete mistake
- the task is mainly design or planning rather than failure investigation
- the next step is no longer investigation but completion verification

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

- do not stack speculative fixes
- do not change multiple variables at once unless the batch is the smallest useful probe
- do not call it root cause until you can explain why the failure happens
- if you cannot reproduce the issue, gather logs, inputs, environment facts, or timing evidence instead of guessing
- if several fix attempts have already failed, question the boundary or architecture assumptions before trying again

## Fast Path

Use a short investigation only when the evidence already isolates one concrete mistake such as:

- wrong import or file path
- inverted condition
- incorrect config key
- bad field mapping
- missing argument or dependency wiring

In that case:

1. name the cause plainly
2. apply the smallest safe fix
3. verify the original failure path
4. verify the surrounding risk with the chosen validation

## Validation

After isolating the cause:

- choose the lightest validation that protects the real risk
- use `choosing-test-strategy` if the right validation mode is not obvious
- use `verification-before-completion` before claiming the bug is fixed

## Output

Before fixing, produce a short debugging statement such as:

```text
Observed failure: settings save returns 500 after the new auth refactor.
Current evidence: token is present in the UI but missing at the API boundary.
Root-cause hypothesis: the fetch wrapper stopped forwarding the auth header in the new call path.
Next probe: compare the working profile update request with the failing settings request.
```

## Handoff

After debugging:

- execute the smallest safe fix once the cause is isolated
- use `choosing-test-strategy` if the validation mode still needs a decision
- use `verification-before-completion` before any success claim
- use `shaping-work` only if the investigation reveals the problem is really a broader route or scope issue

## References

- Use [root-cause-tracing.md](root-cause-tracing.md) for deeper tracing patterns.
- Use [condition-based-waiting.md](condition-based-waiting.md) for race conditions, flake, and timing issues.
- Use [defense-in-depth.md](defense-in-depth.md) for layered fixes after the actual cause is known.
- Use [find-polluter.sh](find-polluter.sh) for polluted test-suite isolation.
