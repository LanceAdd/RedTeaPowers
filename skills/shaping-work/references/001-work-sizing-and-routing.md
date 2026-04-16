# Work Sizing And Routing

Use this reference when the route is not obvious from the request alone.

## Sizing Signals

Check each signal quickly:

| Signal | Low | High |
|--------|-----|------|
| Ambiguity | Expected behavior is already clear | Core behavior still needs decisions |
| Coupling | One area, one file group, low side effects | Changes cross subsystems or depend on sequencing |
| Accumulation | One isolated issue | Multiple same-kind issues should move together |
| Cost of mistake | Easy to revert | Expensive to redo or easy to misalign |
| Urgency | Can refine while moving | Need a route immediately to avoid thrash |

## Route Selection Heuristics

Choose `direct execution` when:
- The request is narrow and well understood
- Verification is straightforward
- Splitting the work further would add overhead, not clarity

Choose `direct execution with session task tracking` when:
- The request includes several related small changes
- The same files, component, or topic will be touched repeatedly
- The main risk is wasted setup time from over-splitting

Choose `lightweight plan` when:
- The work needs ordering across several steps
- The work needs a written artifact before implementation starts
- The task is too big for one reply but too clear for a formal spec

Choose `spec plus plan` when:
- The team needs alignment on behavior before coding
- There are multiple plausible approaches with meaningful tradeoffs
- The work creates or reshapes a long-lived system boundary

## Momentum Rules

- Open a topic with a minimal proving slice only when that slice reduces uncertainty.
- After the first slice works, stop shrinking the work further unless new uncertainty appears.
- Fold nearby small issues into the active batch while the context is warm.
- Prefer finishing a meaningful chunk in a few rounds over preserving tiny theoretical closure forever.

## Escalation And De-Escalation

Escalate the route when:
- New ambiguity appears
- The change starts touching extra subsystems
- Reviewers need a stable artifact before more coding

De-escalate the route when:
- The work turned out smaller than expected
- The open questions are already resolved
- A plan or spec would only restate obvious implementation steps

## Example Routes

```text
Request: "Fix the spacing, copy, and button states across three related settings cards."
Route: direct execution with session task tracking
Reason: same topic, same component family, low ambiguity
```

```text
Request: "Redesign the onboarding flow and decide whether to split it into stages."
Route: spec plus plan
Reason: product behavior and structure both need alignment
```

```text
Request: "Rename the env var and update the code path that reads it."
Route: direct execution
Reason: bounded change with clear verification
```
