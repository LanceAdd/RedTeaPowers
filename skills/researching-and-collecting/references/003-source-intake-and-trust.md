# Source Intake And Trust

Use this reference when the research pass spans more than one source family.

## Source Families

Treat sources as belonging to one of these families:

| Label | Meaning |
|-------|---------|
| `project-fact` | facts from the current project code, docs, configs, commands, or artifacts |
| `local-reference` | a user-specified local project or workspace used for comparison |
| `user-material` | local files the user explicitly wants included, such as PDFs, notes, exports, or drafts |
| `official-external` | primary outside source such as official docs, standards, vendor references, or upstream repos |
| `secondary-external` | blog posts, articles, third-party summaries, forum explanations, or other indirect sources |
| `discussion-note` | provisional notes or discussions that describe intent but not final truth |
| `inference` | a conclusion drawn from evidence rather than a directly quoted fact |

## Intake Order

Use this intake order by default:

1. confirm what the current project already says
2. load any user-specified local references or materials
3. add official external sources only if local evidence is insufficient or the task explicitly needs outside facts
4. add secondary external sources only when they help compare, interpret, or triangulate

This keeps local truth ahead of outside noise.

## Trust Rules

- current project behavior beats external examples
- an official external source beats a secondary explanation on factual disputes
- a local reference project is a comparison target, not an automatic requirement
- a discussion note can explain intent, but it does not override implemented reality unless the user says it should
- an inference must stay marked as an inference

## Conflict Handling

When sources disagree:

1. name the conflict directly
2. show which source families disagree
3. state what is authoritative for the current decision, if known
4. preserve the unresolved conflict in the final output if it still matters

Do not flatten contradictions into a fake single answer.

## External Search Guardrails

External research is justified when:

- the needed fact is not available locally
- the question is about a live standard, product, API, version, or ecosystem option
- the user explicitly asks for outside comparison or market-style scanning

External research is not justified when:

- the current project already answers the question
- the real task is to inspect a user-provided local reference
- outside examples would only distract from the current repo constraints
