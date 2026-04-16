# Library Status Matrix

Use this matrix to decide which top-level skill directories stay in the active product, which still need another rewrite pass, and which can move out of the default package.

All active documents and references should be read and written as UTF-8 text.

## Status Meanings

- `Keep`: already aligned enough with the modernized workflow to stay in the active set
- `Rewrite`: still valuable, but needs another pass before being treated as settled
- `Archive candidate`: useful history or niche workflow, but should not ship as a default active skill unless you explicitly want it

## Top-Level Directory Matrix

| Directory | Status | Why | Next action |
|-----------|--------|-----|-------------|
| `using-redteapowers` | Keep | Active entrypoint for the modernized routing model | Keep as the main onboarding skill |
| `shaping-work` | Keep | New core routing skill that fixes over-scoping and fake granularity | Treat as a required top-level process skill |
| `choosing-test-strategy` | Keep | New core validation router | Keep and reference before TDD decisions |
| `managing-project-docs` | Keep | New doc taxonomy and UTF-8 policy live here | Keep as the documentation control layer |
| `brainstorming` | Keep | Rewritten to be conditional instead of mandatory | Keep, but only trigger when real design uncertainty exists |
| `writing-plans` | Keep | Rewritten to support plans and lighter execution artifacts | Keep for formal execution planning |
| `executing-plans` | Keep | Rewritten to execute plans or checklists without adding ceremony | Keep as the inline execution path |
| `subagent-driven-development` | Keep | Rewritten for task-or-batch execution with scope-first review | Keep as the same-session delegated execution path |
| `systematic-debugging` | Keep | Still central, now routed through validation strategy selection | Keep as the default bug workflow |
| `verification-before-completion` | Keep | Still essential and now strategy-neutral | Keep as the final evidence gate |
| `using-git-worktrees` | Keep | Still useful and now supports plan or checklist execution | Keep as an environment/setup helper |
| `requesting-code-review` | Keep | Still useful and now aligned to requirements, scope, and UTF-8 doc checks | Keep as the outward review workflow |
| `receiving-code-review` | Keep | Still useful and not in direct conflict with the new process model | Keep |
| `finishing-a-development-branch` | Keep | Still useful as a completion/branch integration workflow | Keep |
| `test-driven-development` | Keep | No longer a default process skill, but still valuable when explicitly chosen | Keep as an optional specialized skill |
| `writing-skills` | Rewrite | Valuable, but still strongly framed as universal TDD rather than specialized skill-authoring discipline | Do one more pass to tighten the scope boundary and modernize references/examples |
| `dispatching-parallel-agents` | Archive candidate | Parts of its value are now covered by `subagent-driven-development`; still useful, but no longer core for the default package | Keep only if you want a standalone generic parallel-debugging skill |

## Support Material Notes

These are not top-level skills, but they matter for packaging:

- `systematic-debugging/archive/` is already archived history and should stay out of the active workflow surface
- historical creation logs should live under `archive/`, not beside active skill instructions
- examples that teach old default assumptions should either be rewritten or moved under archive/reference labels

## Recommended Product Cut

If you are packaging a clean `RedTeaPowers` set, start with:

- `using-redteapowers`
- `shaping-work`
- `choosing-test-strategy`
- `managing-project-docs`
- `brainstorming`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `systematic-debugging`
- `verification-before-completion`
- `using-git-worktrees`
- `requesting-code-review`
- `receiving-code-review`
- `finishing-a-development-branch`
- `test-driven-development`

Hold back or separately label:

- `writing-skills`
- `dispatching-parallel-agents`

## Archive Policy

Move a whole skill directory out of the default package when all of the following are true:

1. Its core value is already covered by another active skill
2. Keeping it active would reintroduce outdated process defaults
3. Its remaining value is historical, niche, or training-oriented

When archiving:

- preserve the files as UTF-8 text
- put a short status note at the top saying the material is historical or optional
- remove active cross-references from onboarding docs unless the archive is intentionally discoverable
