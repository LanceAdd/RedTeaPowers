# Document Taxonomy

Use this reference to decide which document to create or update.

## Directory Layout

Prefer this structure inside the project:

- `docs/guide/`
- `docs/discuss/`
- `docs/spec/`
- `docs/plan/`
- `docs/reference/`
- `docs/change/`
- `docs/archive/`
- `scripts/`

Rename the folders only when the project already has a stronger convention.

## Type Boundaries

### guide

Use for stage-level development guidance:
- Phase or stage development charter
- Development outline for the current delivery stage
- Stage-specific working principles
- Bounded development direction that should steer the next execution phase

### discuss

Use for material that is not yet entering execution:
- Requirement discussion before execution
- Open questions blocking commitment
- Alternative proposals under evaluation
- Notes that may later become a `spec` once the team decides to execute

### spec

Use for approved behavior:
- What the system should do
- Boundaries and decisions
- Success criteria

Do not use `spec` for:
- Raw research dumps
- Implementation task lists
- Every small tweak

### plan

Use for execution:
- Ordered steps
- Milestones
- Dependencies between tasks
- Durable batch execution notes that should persist across sessions

Do not use `plan` when direct execution or session task tracking in `TodoWrite` / `update_plan` is enough.

### reference

Use for stable facts that people need to look up:
- Schemas
- API notes
- Rules
- Glossaries

### change

Use for per-round change tracking:
- What changed this round
- Why it changed
- Follow-up actions

### archive

Use for materials that are no longer active but should stay searchable:
- Retired plans
- Finished stage summaries
- Outdated but historically useful discussions

### scripts

Use for reusable helpers:
- Build scripts
- Test scripts
- Run scripts
- Migration and maintenance helpers

## Selection Shortcuts

If the material answers "what are we doing?" use `spec`.

If it answers "what are we still discussing before deciding to execute?" use `discuss`.

If it answers "what development charter are we following in this phase?" use `guide`.

If it answers "how will we do it?" use `plan`.

If it answers "what should we do next right now in this session?" use session task tracking in `TodoWrite` or `update_plan`, not a document type.

If it answers "what changed?" use `change`.

If it answers "what facts should we look up?" use `reference`.
