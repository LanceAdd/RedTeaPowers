---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs. Require fresh evidence that matches the chosen validation strategy, whether that evidence comes from tests, builds, manual verification, reproduction steps, or artifact inspection.
---

# Verification Before Completion

## Overview

Claiming work is complete without fresh evidence is dishonesty, not efficiency.

Core principle: evidence before claims, always.

## The Iron Law

```text
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you have not produced the relevant evidence in this session, you cannot claim success.

## The Gate Function

Before claiming any status:

1. Identify what evidence would prove the claim.
2. Run or perform the full verification now.
3. Read the result carefully.
4. State the claim only if the evidence actually supports it.
5. Otherwise report the real status with the evidence you do have.

Skip any step and you are guessing, not verifying.

## Match Evidence To Strategy

| Claim type | Acceptable evidence |
|------------|---------------------|
| Tests pass | Fresh test output with the expected result |
| Build succeeds | Fresh build output or exit code |
| Bug fixed | Original reproduction no longer fails, plus any required regression coverage |
| UI change is correct | Explicit manual verification steps and what was confirmed |
| Requirements met | Checklist against the artifact, backed by the chosen validation evidence |
| Agent completed work | Verified file changes plus fresh validation of the result |

## Red Flags

- "Should work now"
- "Probably fixed"
- "Looks right"
- "Tests passed earlier"
- "The agent said it was done"
- Any success wording before verification

All of these mean stop and verify properly.

## Common Failures

| Claim | Requires | Not sufficient |
|-------|----------|----------------|
| Tests pass | Fresh test command output | A previous run |
| Build passes | Fresh build output | Lint passing alone |
| Bug fixed | Reproduction and chosen validation evidence | Code changed, assumed fixed |
| UI looks correct | Manual verification notes | Reading the diff |
| Requirements met | Requirement-by-requirement check | "Most tests passed" |

## Key Patterns

Tests:
```text
Run the relevant command now, read the result, then claim it passes.
```

Manual verification:
```text
List the steps you checked, what screen or flow you inspected, and what matched expectations.
```

Delegated work:
```text
Do not trust the agent's report alone. Check the changes and verify the result yourself.
```

## Bottom Line

No shortcuts.

Run the right check. Read the result. Then make the claim.
