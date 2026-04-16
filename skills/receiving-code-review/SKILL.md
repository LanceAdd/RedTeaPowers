---
name: receiving-code-review
description: Use when review feedback arrives and you need to decide what to accept, question, defer, or reject before changing code. Verify each comment against requirements, codebase reality, existing evidence, and current constraints instead of reacting performatively or implementing blindly.
---

# Receiving Code Review

## Overview

Review feedback is input to evaluate, not a script to obey automatically.

Treat every comment as a technical claim that needs context, verification, and a deliberate response. Respect the reviewer, but do not outsource engineering judgment.

## Workflow

1. Read the full feedback without acting on the first comment in isolation.
2. Group comments by theme, severity, and dependency.
3. Clarify any unclear item before implementing related changes.
4. Verify each comment against:
   - the current code
   - the original requirements or plan
   - the chosen validation strategy
   - known compatibility, architecture, or product constraints
5. Decide the handling:
   - accept
   - partially accept
   - push back with reasoning
   - defer for a later batch
   - escalate to the user when the feedback changes scope or architecture
6. Implement accepted items in sensible batches.
7. Re-verify the affected behavior before claiming the feedback is addressed.

## Handling Rules

- Do not implement unclear comments.
- Do not respond with agreement before you know whether the comment is correct for this codebase.
- Do not treat external review as automatically authoritative.
- Do not ignore valid feedback just because the tone is awkward.
- Do not split tightly related review fixes into fake micro-loops if one bounded batch is safer and clearer.

## Good Reasons To Push Back

Push back when the comment:

- conflicts with the approved requirements
- breaks existing supported behavior
- assumes context the reviewer does not have
- asks for overbuilding or unused features
- contradicts the chosen validation strategy
- creates a larger architectural change than the current scope allows

When pushing back, be specific:

- what the comment claims
- what you verified
- why that evidence changes the conclusion
- whether you want a decision from the user

## When To Escalate

Escalate to the user instead of deciding alone when:

- feedback changes requirements or system boundaries
- two valid comments conflict
- a suggested fix carries non-obvious product or maintenance cost
- you cannot verify the comment from available evidence

## Output

Use a response summary shaped like:

```text
Accepted:
- comment 1: null handling bug is real; fixing in the API adapter batch

Pushed back:
- comment 2: removing the fallback would break the supported offline path; confirmed in app bootstrap and manual verification

Need decision:
- comment 3 expands scope into a schema redesign; user decision required before implementation
```

## Integration

- `redteapowers:requesting-code-review` prepares the incoming review context
- `redteapowers:choosing-test-strategy` helps when feedback implies a different validation need
- `redteapowers:verification-before-completion` confirms the post-review state before any success claim
