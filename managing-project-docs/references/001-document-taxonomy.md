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
- `docs/todolist/`
- `scripts/`

Rename the folders only when the project already has a stronger convention.

## Type Boundaries

### guide

Use for orientation and direction:
- Development outline
- Topic map
- Shared principles
- "How this area works" material

### discuss

Use for material that is not yet approved:
- Requirement discussion
- Open questions
- Alternative proposals
- Notes that may later become a spec

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

Do not use `plan` when a short checklist or todolist is enough.

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

### todolist

Use for active operational work:
- Near-term tasks
- Preconditions
- Open blockers
- Batched issue lists

### scripts

Use for reusable helpers:
- Build scripts
- Test scripts
- Run scripts
- Migration and maintenance helpers

## Selection Shortcuts

If the material answers "what are we doing?" use `spec`.

If it answers "how will we do it?" use `plan`.

If it answers "what should we do next?" use `todolist`.

If it answers "what changed?" use `change`.

If it answers "what facts should we look up?" use `reference`.
