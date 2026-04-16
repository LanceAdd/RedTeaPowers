# Document Taxonomy Clarifications

Use this reference when `guide` and `discuss` start drifting back toward vague or overly broad meanings.

## Goal

Keep the RedTeaPowers document taxonomy sharp enough that active work does not hide in the wrong document type.

The two document types most likely to blur are `discuss` and `guide`.

## discuss

`discuss` is for pre-execution requirement discussion.

Use `discuss` when:

- requirements are still being debated
- open questions still block commitment
- alternative proposals still need comparison
- the team is intentionally not entering implementation yet

Do not use `discuss` when:

- the team has already decided to execute
- approved behavior and boundaries are now known
- the document is acting as the current source of truth for implementation

Once the team decides to execute, move the approved behavior and boundaries into `spec` instead of leaving active decisions inside `discuss`.

## guide

`guide` is for a stage-level development charter or phased development outline.

Use `guide` when:

- a delivery stage needs a bounded development charter
- the team needs stage-specific direction before or during execution
- the document exists to steer the next phase of work

Do not use `guide` for:

- general explanatory notes
- architecture overview by itself
- "how this area works" material
- stable lookup material that people revisit mainly for facts

Those usually belong in `reference`.

## Quick Selection Rule

Use this shortcut when the boundary is fuzzy:

- if the work is still being discussed and should not enter implementation yet, use `discuss`
- if execution is approved and behavior needs to be locked, use `spec`
- if a delivery phase needs a charter or staged development outline, use `guide`
- if the document mostly explains or describes facts, use `reference`

## Migration Rule

When migrating older documents:

- move unresolved pre-execution requirement debate into `discuss`
- move phase charters or staged development outlines into `guide`
- move general orientation, architecture overview, and explanatory material into `reference`
- move approved execution-bound behavior into `spec`
