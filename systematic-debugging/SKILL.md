---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. Keep the investigation explicit and evidence-based, and allow fast correction only after the root cause is actually isolated.
---

# Systematic Debugging

## Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** find root cause before attempting fixes. Symptom fixes are failure.

For obvious single-point mistakes, keep the investigation short, explicit, and evidence-based, then correct them quickly and verify the result. Do not turn a clear typo or miswire into ritual, but do not skip verification.

## The Iron Law

```text
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you have not isolated the cause, you are not ready to fix it.

## When to Use

Use for any technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

Use this especially when:
- You are under time pressure
- "Just one quick fix" seems obvious
- You already tried multiple fixes
- A previous fix did not work
- You do not fully understand the issue

Do not skip just because:
- The issue seems simple
- You are in a hurry
- Someone wants it fixed immediately

## The Four Phases

Complete each phase in order. Keep the loop short when the evidence is clear, but do not skip the evidence.

### Phase 1: Root Cause Investigation

Before attempting any fix:

1. **Read error messages carefully**
   - Read the full error, warning, or failing assertion
   - Note line numbers, file paths, and error codes

2. **Reproduce consistently**
   - Can you trigger it reliably?
   - What exact steps cause it?
   - Does it happen every time?
   - If not reproducible, gather more data instead of guessing

3. **Check recent changes**
   - What changed that could cause this?
   - Review recent diffs, config changes, dependency updates, and environment differences

4. **Gather boundary evidence in multi-component systems**
   - Log or inspect what enters and exits each boundary
   - Verify config and environment propagation
   - Use one evidence-gathering pass to identify where the break actually occurs

5. **Trace data flow**
   - Where does the bad value or bad state originate?
   - What called this with the wrong input?
   - Trace backward until you find the source
   - Fix at the source, not at the symptom

6. **Short-circuit obvious single-point failures**
   - If the evidence already isolates one concrete mistake, write down that root cause plainly
   - Examples: wrong variable name, wrong import path, inverted condition, missing config key
   - Move to Phase 4 once the cause is explicit

### Phase 2: Pattern Analysis

Find the pattern before fixing:

1. **Find working examples**
   - Locate similar working code in the same codebase

2. **Compare against references**
   - Read the relevant implementation or docs completely when a pattern matters

3. **Identify differences**
   - List what differs between the working and broken paths
   - Do not dismiss small differences without checking them

4. **Understand dependencies**
   - Confirm required settings, config, environment, and calling assumptions

### Phase 3: Hypothesis and Testing

Use a simple scientific loop:

1. **Form one hypothesis**
   - State clearly: "I think X is the root cause because Y"

2. **Test minimally**
   - Make the smallest possible change or probe to test that hypothesis
   - Change one thing at a time

3. **Verify before continuing**
   - If it confirms the hypothesis, move to Phase 4
   - If not, form a new hypothesis instead of stacking more fixes

4. **Say when you do not know**
   - Name the gap
   - Research more or ask for help

### Phase 4: Implementation

Fix the root cause, not the symptom:

1. **Create a reproduction and pick validation**
   - Use the simplest useful reproduction
   - Choose automated regression coverage when it fits
   - Use a one-off script or manual steps when that is the right fit
   - Use `redteapowers:choosing-test-strategy` if the right validation mode is not obvious

2. **Implement the smallest safe fix**
   - Address the root cause identified
   - Keep the change set focused
   - Avoid "while I am here" improvements
   - Avoid bundled refactoring unless the root cause itself is shared and the batch is the smallest safe fix

3. **Verify the fix**
   - Reproduce the old failure path
   - Run the chosen validation
   - Check for regressions around the affected area

4. **If the fix does not work**
   - Stop
   - Return to Phase 1 with the new evidence
   - If you already failed 3 times, question the architecture before trying again

5. **If 3 or more fixes failed: question the architecture**
   - Ask whether the pattern itself is wrong
   - Ask whether hidden coupling or shared state is the real problem
   - Discuss with your human partner before attempting more fixes

## Red Flags

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "It is probably X, let me fix that"
- "I do not fully understand but this might work"
- "One more fix attempt" after repeated failures

Stop and go back to evidence gathering.

## Human Signals

These redirections usually mean the process is slipping:
- "Is that not happening?" means you assumed instead of verifying
- "Will it show us...?" means you need better evidence
- "Stop guessing" means you proposed fixes without understanding
- "We are stuck?" means your loop is no longer producing insight

Treat these as a signal to return to Phase 1.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "The issue is simple, we do not need process" | Simple issues still have causes, and quick evidence is still process. |
| "Emergency, no time for process" | Systematic debugging is faster than thrashing. |
| "I will write tests after I confirm the fix" | Unverified fixes do not stick. |
| "Multiple fixes at once saves time" | You lose the ability to tell what worked. |
| "I see the problem, let me fix it" | Seeing symptoms is not the same as isolating cause. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, trace evidence | Understand what failed and why |
| **2. Pattern** | Compare with working examples | Identify meaningful differences |
| **3. Hypothesis** | State and test one explanation | Confirmed cause or better evidence |
| **4. Implementation** | Apply focused fix and verify | Bug resolved and validated |

## When the Cause Is External

If systematic investigation shows the issue is environmental, timing-dependent, or external:

1. Document what you investigated
2. Implement the appropriate handling
3. Add monitoring or logging if future evidence will help

Do not label it "no root cause" until the investigation is genuinely complete.

## Supporting Techniques

These techniques are part of systematic debugging and available in this directory:

- `root-cause-tracing.md`
- `defense-in-depth.md`
- `condition-based-waiting.md`

Related skills:
- `redteapowers:choosing-test-strategy`
- `redteapowers:test-driven-development`
- `redteapowers:verification-before-completion`
