# Bootstrap Initializer CLI

Use this reference when a project needs an initial RedTeaPowers-compatible documentation structure.

## Goal

Initialize the lightest useful documentation tree for either:

- a new project that needs a clean starting point
- a legacy project that needs a target structure before documentation migration

This initializer should create structure, navigation, and a small amount of seed guidance.

It should not create a large pile of empty documents and should not silently migrate legacy content.

## Command Shape

Recommended primary command:

```text
init-doc-structure <project-root> [options]
```

Recommended implementation layout inside this skill:

```text
skills/managing-project-docs/
|- scripts/
|  |- init_doc_structure.py
|  |- init_doc_structure.ps1
|  `- init_doc_structure.sh
`- templates/
   |- new-minimal/
   |- new-standard/
   `- legacy-standard/
```

## Mode Selection

Practical entrypoints in this repo:

```text
python skills/managing-project-docs/scripts/init_doc_structure.py <project-root> [options]
powershell -File skills/managing-project-docs/scripts/init_doc_structure.ps1 <project-root> [options]
sh skills/managing-project-docs/scripts/init_doc_structure.sh <project-root> [options]
```

The initializer should always ask the user what kind of project state they are in before creating files.

Modes:

- `new`: the project is starting fresh and needs an initial docs tree
- `legacy`: the project already has documentation and needs a migration-ready target structure

## Profile Selection

After mode selection, ask for a profile.

### New Project Profiles

- `minimal`: create only the baseline directory structure and the smallest useful seed files
- `standard`: create the standard directory structure, top-level docs index, directory guidance, and a bootstrap `change` record

Default for `new`: `standard`

### Legacy Project Profiles

- `audit`: inspect the current documentation tree and generate migration planning output only
- `standard`: create the target RedTeaPowers docs tree, plus migration bootstrap files, without moving or rewriting existing content

Default for `legacy`: `standard`

## Standard Directory Targets

When structure creation is needed, prefer:

- `docs/guide/`
- `docs/discuss/`
- `docs/spec/`
- `docs/plan/`
- `docs/reference/`
- `docs/change/`
- `docs/archive/`
- `scripts/`

Rename only when the repository already has a stronger established convention.

## Profile Outcomes

### `new:minimal`

Create:

- standard docs directories

Optional:

- `docs/README.md` when `--with-index` is enabled

Do not create:

- bootstrap docs
- empty `spec`, `plan`, or `guide` files just to fill the tree
- placeholder files in every directory

### `new:standard`

Create:

- standard docs directories
- `docs/README.md`
- short README or guidance files for key active directories
- `docs/change/001-project-doc-bootstrap.md`

Optional when `--with-seed-files` is enabled:

- one example `spec` template
- one example `plan` template
- one example `reference` template

Guardrail:

- keep starter templates few, explicit, and easy to delete

### Quick Difference

- `new:minimal`: create the directory skeleton only, unless `--with-index` is explicitly requested
- `new:standard`: create a navigable docs tree with index, directory guidance, and a bootstrap change record

### `legacy:audit`

Create:

- migration assessment output only

Recommended outputs:

- console summary
- optional migration report markdown
- suggested migration batches grouped by source area and likely target type

Do not create:

- target docs tree
- bootstrap files
- moved or rewritten docs

### `legacy:standard`

Create:

- standard docs directories
- `docs/README.md`
- `docs/change/001-doc-migration-bootstrap.md`
- `docs/plan/001-doc-migration-plan.md` or equivalent migration planning artifact

Do not create:

- automatic file moves
- automatic archive passes
- automatic content rewriting

## Interaction Model

Keep the interaction short and fixed-choice.

Recommended prompt flow:

1. choose mode
2. choose profile for that mode
3. show dry-run preview
4. ask for final confirmation

Do not turn initialization into an open-ended interview.

## Recommended CLI Options

- `--mode new|legacy`
- `--profile <name>`
- `--dry-run`
- `--output <path>`
- `--with-index`
- `--with-seed-files`
- `--force`
- `--yes`
- `--existing-convention keep|redteapowers`
- `--json`

## Option Semantics

- `--dry-run`: show what would be created or skipped without writing files
- `--output`: write the legacy audit markdown report to a file when running `legacy:audit`
- `--with-index`: force creation of `docs/README.md` when the chosen profile allows it
- `--with-seed-files`: create optional seed files exposed by the chosen profile, such as the extra starter templates in `new:standard`
- `--force`: allow overwriting initializer-managed files only after explicit confirmation
- `--yes`: skip the final confirmation prompt
- `--existing-convention keep`: preserve stronger existing repo conventions where possible
- `--existing-convention redteapowers`: normalize to the standard RedTeaPowers directory layout
- `--json`: emit machine-readable create, skip, and conflict results

Profiles should still work sensibly without requiring every flag.

## Command Examples

New project, standard profile, preview only:

```text
python skills/managing-project-docs/scripts/init_doc_structure.py . --mode new --profile standard --dry-run
```

New project, standard profile, include the extra starter templates:

```text
python skills/managing-project-docs/scripts/init_doc_structure.py . --mode new --profile standard --with-seed-files --yes
```

Legacy project, audit only, and write the report to disk:

```text
python skills/managing-project-docs/scripts/init_doc_structure.py . --mode legacy --profile audit --output docs-migration-audit.md
```

Legacy project, create the migration-ready target tree:

```text
powershell -File skills/managing-project-docs/scripts/init_doc_structure.ps1 . --mode legacy --profile standard --dry-run
```

## Preview Requirements

Before writing files, show a preview like:

```text
Mode: legacy
Profile: standard

Will create:
- docs/guide/
- docs/discuss/
- docs/spec/
- docs/plan/
- docs/reference/
- docs/change/
- docs/archive/
- scripts/
- docs/README.md
- docs/change/001-doc-migration-bootstrap.md
- docs/plan/001-doc-migration-plan.md

Will not do:
- move existing documents
- rewrite existing documents
- archive files automatically
```

The preview should also list:

- existing paths that will be kept
- conflicts that need attention
- files that would only be created when `--with-seed-files` is enabled

When `--json` is used together with `--dry-run`, emit the preview as structured JSON instead of the text preview.

## Output Contract

After execution, report:

- created paths
- skipped paths
- conflicts
- next suggested action

Example:

```text
Created:
- docs/guide/
- docs/discuss/
- docs/spec/
- docs/plan/
- docs/reference/
- docs/change/
- docs/archive/
- scripts/
- docs/README.md

Skipped:
- docs/spec/ already exists
- scripts/ already exists

Next:
- decide whether current work needs `guide`, `spec`, `plan`, or only session task tracking
```

Example preview JSON shape:

```json
{
  "mode": "new",
  "profile": "standard",
  "project_root": "/path/to/project",
  "docs_root": "docs",
  "scripts_root": "scripts",
  "plan": {
    "create": [
      "docs",
      "docs/guide",
      "docs/README.md"
    ],
    "overwrite": [],
    "skip": [],
    "conflict": [],
    "optional": []
  },
  "next": "Create only the real docs that materially help the project, and use the optional starter templates only when they still fit the work."
}
```

## Safety Rules

- keep the initializer idempotent
- default to no overwrite
- write template content as UTF-8
- do not move or rewrite legacy files unless the user chose a dedicated migration flow outside the initializer
- do not generate large numbers of empty files

## Handoff

After initialization:

- use `managing-project-docs` to decide which real documents deserve to be created next
- use `migrating-project-docs` when a legacy repo now needs a true migration pass
- use `writing-plans` only if the migration or setup work itself needs durable execution sequencing
