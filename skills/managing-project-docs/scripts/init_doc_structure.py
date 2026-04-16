#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


DOC_TYPES = ["guide", "discuss", "spec", "plan", "reference", "change", "archive"]
DOC_ROOT_CANDIDATES = ["docs", "doc", "documentation"]
SCRIPTS_ROOT_CANDIDATES = ["scripts", "tools", "bin"]
TEXT_EXTENSIONS = {
    ".md",
    ".markdown",
    ".mdx",
    ".txt",
    ".rst",
    ".adoc",
    ".org",
    ".wiki",
}
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".turbo",
    ".cache",
    "__pycache__",
}
PROFILE_CHOICES = {
    "new": ["minimal", "standard"],
    "legacy": ["audit", "standard"],
}
DEFAULT_PROFILE = {
    "new": "standard",
    "legacy": "standard",
}
PROFILE_TEMPLATE_CHAIN = {
    ("new", "minimal"): ["new-minimal"],
    ("new", "standard"): ["new-minimal", "new-standard"],
    ("legacy", "standard"): ["legacy-standard"],
}
DOC_TYPE_BLURBS = {
    "guide": "Use this directory for stage-level development charters or phased delivery outlines.",
    "discuss": "Use this directory for pre-execution requirement discussion, open questions, and alternatives.",
    "spec": "Use this directory for approved behavior, boundaries, and success conditions.",
    "plan": "Use this directory for durable implementation sequencing that should survive across sessions.",
    "reference": "Use this directory for stable lookup material such as APIs, schemas, rules, and design facts.",
    "change": "Use this directory for per-round change notes and decision trails.",
    "archive": "Use this directory for inactive but still useful material that should remain searchable.",
}
SIGNAL_TARGET_HINTS = {
    "guide": "guide",
    "discuss": "discuss",
    "spec": "spec",
    "plan": "plan",
    "reference": "reference",
    "change": "change",
    "archive": "archive",
}


@dataclass
class PlannedItem:
    path: Path
    kind: str
    reason: str
    content: str | None = None
    optional: bool = False


@dataclass
class EvaluatedItem:
    path: Path
    kind: str
    reason: str
    status: str
    content: str | None = None
    optional: bool = False


@dataclass
class AuditRecord:
    relative_path: str
    top_level: str
    encoding: str
    line_count: int
    signal: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Bootstrap a RedTeaPowers-compatible documentation tree for a new or "
            "legacy project."
        )
    )
    parser.add_argument("project_root", help="Project root to inspect or initialize")
    parser.add_argument("--mode", choices=sorted(PROFILE_CHOICES.keys()))
    parser.add_argument("--profile")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--with-index",
        action="store_true",
        help="Force creation of docs/README.md when the chosen profile allows it.",
    )
    parser.add_argument(
        "--with-seed-files",
        action="store_true",
        help="Force creation of optional seed files when the chosen profile exposes them.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files created by the initializer after confirmation.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the final confirmation prompt.",
    )
    parser.add_argument(
        "--existing-convention",
        choices=["keep", "redteapowers"],
        default="keep",
    )
    parser.add_argument(
        "--output",
        help="Optional markdown output path for legacy audit reports.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable execution results.",
    )
    return parser.parse_args()


def is_interactive() -> bool:
    return sys.stdin.isatty() and sys.stdout.isatty()


def prompt_choice(title: str, choices: list[str], default: str) -> str:
    print(title)
    for index, choice in enumerate(choices, start=1):
        suffix = " (default)" if choice == default else ""
        print(f"{index}. {choice}{suffix}")
    raw = input("> ").strip()
    if not raw:
        return default
    if raw.isdigit():
        selected = int(raw)
        if 1 <= selected <= len(choices):
            return choices[selected - 1]
    if raw in choices:
        return raw
    raise SystemExit(f"Invalid selection: {raw}")


def resolve_mode_and_profile(args: argparse.Namespace) -> tuple[str, str]:
    mode = args.mode
    profile = args.profile

    if mode is None:
        if not is_interactive():
            raise SystemExit("Mode is required in non-interactive usage. Pass --mode.")
        mode = prompt_choice("Mode:", sorted(PROFILE_CHOICES.keys()), "new")

    valid_profiles = PROFILE_CHOICES[mode]
    default_profile = DEFAULT_PROFILE[mode]

    if profile is None:
        if not is_interactive():
            profile = default_profile
        else:
            profile = prompt_choice("Profile:", valid_profiles, default_profile)

    if profile not in valid_profiles:
        raise SystemExit(
            f"Invalid profile '{profile}' for mode '{mode}'. "
            f"Expected one of: {', '.join(valid_profiles)}"
        )

    return mode, profile


def resolve_root_name(project_root: Path, preferred: list[str], default: str) -> str:
    for candidate in preferred:
        path = project_root / candidate
        if path.exists() and path.is_dir():
            return candidate
    return default


def resolve_structure_roots(project_root: Path, existing_convention: str) -> tuple[str, str]:
    if existing_convention == "keep":
        docs_root = resolve_root_name(project_root, DOC_ROOT_CANDIDATES, "docs")
        scripts_root = resolve_root_name(project_root, SCRIPTS_ROOT_CANDIDATES, "scripts")
        return docs_root, scripts_root
    return "docs", "scripts"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def should_scan(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.stat().st_size > 1024 * 1024:
        return False
    return True


def looks_like_doc(path: Path) -> bool:
    lowered_parts = {part.lower() for part in path.parts}
    lowered_name = path.name.lower()
    lowered_stem = path.stem.lower()
    return (
        bool(lowered_parts & {"docs", "doc", "documentation", "notes", "wiki", "spec", "specs", "plan", "plans"})
        or any(token in lowered_name for token in ("readme", "spec", "plan", "todo", "note", "change", "design"))
        or any(token in lowered_stem for token in ("requirements", "architecture", "roadmap", "research"))
    )


def detect_encoding(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "gb18030", "cp1252", "latin-1"):
        try:
            raw.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    return "latin-1-replace"


def iter_candidate_docs(project_root: Path) -> Iterable[Path]:
    for path in sorted(project_root.rglob("*")):
        if path.is_file() and should_scan(path) and looks_like_doc(path):
            yield path


def guess_doc_signal(relative_path: str) -> str:
    haystack = relative_path.lower()

    if any(token in haystack for token in ("archive", "legacy", "deprecated", "history", "retired", "/old/", "old-")):
        return "archive"
    if any(token in haystack for token in ("changelog", "change", "release-note", "release_notes", "update", "updates")):
        return "change"
    if any(token in haystack for token in ("todo", "tasks", "task", "plan", "roadmap", "milestone", "next-step", "next_steps", "implementation")):
        return "plan"
    if any(token in haystack for token in ("spec", "requirements", "requirement", "behavior")):
        return "spec"
    if any(token in haystack for token in ("proposal", "discussion", "decision", "question", "questions", "tradeoff")):
        return "discuss"
    if any(token in haystack for token in ("phase-guide", "stage-guide", "charter", "guide")):
        return "guide"
    return "reference"


def collect_audit_records(project_root: Path) -> list[AuditRecord]:
    records: list[AuditRecord] = []
    for path in iter_candidate_docs(project_root):
        encoding = detect_encoding(path)
        relative = path.relative_to(project_root)
        top_level = relative.parts[0] if len(relative.parts) > 1 else "(root)"
        try:
            line_count = path.read_text(encoding=encoding, errors="replace").count("\n") + 1
        except OSError:
            line_count = 0
        relative_path = relative.as_posix()
        records.append(
            AuditRecord(
                relative_path=relative_path,
                top_level=top_level,
                encoding=encoding,
                line_count=line_count,
                signal=guess_doc_signal(relative_path),
            )
        )
    return records


def build_legacy_audit_data(project_root: Path) -> dict[str, object]:
    records = collect_audit_records(project_root)
    encodings = Counter(record.encoding for record in records)
    top_level_dirs = Counter(record.top_level for record in records)
    signals = Counter(record.signal for record in records)
    families: dict[tuple[str, str], list[AuditRecord]] = {}
    for record in records:
        families.setdefault((record.top_level, record.signal), []).append(record)

    recommended_batches = []
    ranked_families = sorted(
        families.items(),
        key=lambda item: (-len(item[1]), item[0][0], item[0][1], item[1][0].relative_path),
    )
    for (top_level, signal), family_records in ranked_families[:8]:
        recommended_batches.append(
            {
                "source": top_level,
                "signal": signal,
                "likely_target": SIGNAL_TARGET_HINTS[signal],
                "count": len(family_records),
                "examples": [record.relative_path for record in family_records[:3]],
            }
        )

    return {
        "source_root": project_root.as_posix(),
        "generated": utc_now(),
        "candidate_count": len(records),
        "encodings": dict(encodings.most_common()),
        "top_level_dirs": dict(top_level_dirs.most_common()),
        "signals": dict(signals.most_common()),
        "samples": [
            {
                "path": record.relative_path,
                "encoding": record.encoding,
                "lines": record.line_count,
                "signal": record.signal,
            }
            for record in records[:30]
        ],
        "recommended_batches": recommended_batches,
    }


def build_legacy_audit_report(project_root: Path) -> str:
    data = build_legacy_audit_data(project_root)

    lines = [
        "# Legacy Documentation Audit",
        "",
        f"Source root: `{data['source_root']}`",
        f"Generated: {data['generated']}",
        "",
        "## Summary",
        "",
        f"- Candidate documentation files: {data['candidate_count']}",
        f"- Detected encodings: {', '.join(f'{key}={value}' for key, value in data['encodings'].items()) or 'none'}",
        f"- Top-level directories: {', '.join(f'{key}={value}' for key, value in data['top_level_dirs'].items()) or 'none'}",
        f"- Dominant signals: {', '.join(f'{key}={value}' for key, value in data['signals'].items()) or 'none'}",
        "",
        "## Candidate Directories",
        "",
    ]

    if data["top_level_dirs"]:
        for name, count in data["top_level_dirs"].items():
            label = f"`{name}/`" if name != "(root)" else "`(root)`"
            lines.append(f"- {label}: {count} file(s)")
    else:
        lines.append("- No obvious legacy documentation candidates were found.")

    lines.extend(
        [
            "",
            "## Suggested Migration Batches",
            "",
        ]
    )

    if data["recommended_batches"]:
        for batch in data["recommended_batches"]:
            label = f"`{batch['source']}/`" if batch["source"] != "(root)" else "`(root)`"
            examples = ", ".join(f"`{path}`" for path in batch["examples"])
            lines.append(
                f"- {label} -> likely `{batch['likely_target']}` from `{batch['signal']}` signals "
                f"({batch['count']} file(s)); examples: {examples}"
            )
    else:
        lines.append("- No migration batches were suggested because no candidate docs were detected.")

    lines.extend(
        [
            "",
            "## Sample Files",
            "",
            "| Path | Encoding | Lines | Signal |",
            "|------|----------|-------|--------|",
        ]
    )

    if data["samples"]:
        for sample in data["samples"]:
            lines.append(
                f"| `{sample['path']}` | `{sample['encoding']}` | {sample['lines']} | `{sample['signal']}` |"
            )
    else:
        lines.append("| none | n/a | 0 | n/a |")

    lines.extend(
        [
            "",
            "## Suggested Next Step",
            "",
            "- Review the suggested migration batches before touching active docs.",
            "- If the target structure is missing, run the initializer again with `--mode legacy --profile standard --dry-run`.",
            "- After the target tree looks right, use `migrating-project-docs` for the actual migration pass.",
            "",
        ]
    )
    return "\n".join(lines)


def load_template(skill_dir: Path, mode: str, profile: str, relative_path: str) -> str:
    chain = PROFILE_TEMPLATE_CHAIN[(mode, profile)]
    for template_dir in reversed(chain):
        candidate = skill_dir / "templates" / template_dir / relative_path
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    raise FileNotFoundError(f"Missing template for {mode}:{profile}: {relative_path}")


def render_text(template_text: str, context: dict[str, str]) -> str:
    rendered = template_text
    for key, value in context.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def render_directory_readme(doc_type: str, docs_root_name: str) -> str:
    title = doc_type.capitalize()
    blurb = DOC_TYPE_BLURBS[doc_type]
    return (
        f"# {title}\n\n"
        f"{blurb}\n\n"
        f"Keep files here focused, numbered when order matters, and linked from "
        f"`{docs_root_name}/README.md` when they become active navigation points.\n"
    )


def next_numbered_path(directory: Path, slug: str, reservations: dict[Path, int]) -> Path:
    reserved_next = reservations.get(directory)
    if reserved_next is None:
        current = 0
        if directory.exists() and directory.is_dir():
            for child in directory.iterdir():
                match = re.match(r"^(\d+)-", child.name)
                if match:
                    current = max(current, int(match.group(1)))
        reserved_next = current + 1
    reservations[directory] = reserved_next + 1
    return directory / f"{reserved_next:03d}-{slug}.md"


def build_context(
    project_root: Path,
    docs_root_name: str,
    scripts_root_name: str,
    mode: str,
    profile: str,
) -> dict[str, str]:
    return {
        "PROJECT_NAME": project_root.name,
        "PROJECT_ROOT": project_root.as_posix(),
        "DOCS_ROOT": docs_root_name,
        "SCRIPTS_ROOT": scripts_root_name,
        "GENERATED_AT": utc_now(),
        "MODE": mode,
        "PROFILE": profile,
    }


def build_plan(
    project_root: Path,
    skill_dir: Path,
    mode: str,
    profile: str,
    docs_root_name: str,
    scripts_root_name: str,
    with_index: bool,
    with_seed_files: bool,
) -> list[PlannedItem]:
    if mode == "legacy" and profile == "audit":
        return []

    docs_root = project_root / docs_root_name
    scripts_root = project_root / scripts_root_name
    context = build_context(project_root, docs_root_name, scripts_root_name, mode, profile)
    reservations: dict[Path, int] = {}
    items: list[PlannedItem] = []

    items.append(PlannedItem(path=docs_root, kind="dir", reason="Create the documentation root."))
    for doc_type in DOC_TYPES:
        items.append(
            PlannedItem(
                path=docs_root / doc_type,
                kind="dir",
                reason=f"Create the `{doc_type}` directory.",
            )
        )
    items.append(PlannedItem(path=scripts_root, kind="dir", reason="Create the scripts directory."))

    include_index = with_index or mode == "legacy" or profile == "standard"
    if include_index:
        if mode == "legacy":
            template = load_template(skill_dir, mode, "standard", "docs/README.md")
        else:
            template = load_template(skill_dir, mode, profile, "docs/README.md")
        items.append(
            PlannedItem(
                path=docs_root / "README.md",
                kind="file",
                reason="Create the top-level docs index.",
                content=render_text(template, context),
            )
        )

    include_directory_guidance = profile == "standard" or (mode == "legacy" and profile == "standard")
    if include_directory_guidance:
        for doc_type in DOC_TYPES:
            items.append(
                PlannedItem(
                    path=docs_root / doc_type / "README.md",
                    kind="file",
                    reason=f"Add quick guidance for the `{doc_type}` directory.",
                    content=render_directory_readme(doc_type, docs_root_name),
                )
            )

    if mode == "new" and profile == "standard":
        template = load_template(skill_dir, mode, profile, "docs/change/project-doc-bootstrap.md")
        bootstrap_path = next_numbered_path(docs_root / "change", "project-doc-bootstrap", reservations)
        items.append(
            PlannedItem(
                path=bootstrap_path,
                kind="file",
                reason="Record the documentation bootstrap decision.",
                content=render_text(template, context),
            )
        )

    if mode == "new" and profile == "standard":
        starter_templates = [
            ("docs/spec/starter-spec.md", "spec", "starter-spec", "Create an optional starter spec template."),
            ("docs/plan/starter-plan.md", "plan", "starter-plan", "Create an optional starter plan template."),
            (
                "docs/reference/starter-reference.md",
                "reference",
                "starter-reference",
                "Create an optional starter reference template.",
            ),
        ]
        for template_path, doc_type, slug, reason in starter_templates:
            template = load_template(skill_dir, mode, profile, template_path)
            target = next_numbered_path(docs_root / doc_type, slug, reservations)
            items.append(
                PlannedItem(
                    path=target,
                    kind="file",
                    reason=reason,
                    content=render_text(template, context),
                    optional=not with_seed_files,
                )
            )

    if mode == "legacy" and profile == "standard":
        change_template = load_template(skill_dir, mode, profile, "docs/change/doc-migration-bootstrap.md")
        plan_template = load_template(skill_dir, mode, profile, "docs/plan/doc-migration-plan.md")
        change_path = next_numbered_path(docs_root / "change", "doc-migration-bootstrap", reservations)
        plan_path = next_numbered_path(docs_root / "plan", "doc-migration-plan", reservations)
        items.extend(
            [
                PlannedItem(
                    path=change_path,
                    kind="file",
                    reason="Record the docs migration bootstrap pass.",
                    content=render_text(change_template, context),
                ),
                PlannedItem(
                    path=plan_path,
                    kind="file",
                    reason="Create a durable migration plan starting point.",
                    content=render_text(plan_template, context),
                ),
            ]
        )

    return items


def evaluate_plan(items: list[PlannedItem], force: bool) -> list[EvaluatedItem]:
    evaluated: list[EvaluatedItem] = []
    for item in items:
        path = item.path
        if item.optional:
            status = "optional"
        elif item.kind == "dir":
            if path.exists() and path.is_file():
                status = "conflict"
            elif path.exists():
                status = "skip"
            else:
                status = "create"
        else:
            if path.exists() and path.is_dir():
                status = "conflict"
            elif path.exists():
                status = "overwrite" if force else "skip"
            else:
                status = "create"
        evaluated.append(
            EvaluatedItem(
                path=item.path,
                kind=item.kind,
                reason=item.reason,
                status=status,
                content=item.content,
                optional=item.optional,
            )
        )
    return evaluated


def relative_display(project_root: Path, path: Path) -> str:
    try:
        return path.relative_to(project_root).as_posix()
    except ValueError:
        return path.as_posix()


def print_preview(
    project_root: Path,
    mode: str,
    profile: str,
    evaluated: list[EvaluatedItem],
    docs_root_name: str,
    scripts_root_name: str,
) -> None:
    will_create = [item for item in evaluated if item.status == "create" and not item.optional]
    will_overwrite = [item for item in evaluated if item.status == "overwrite" and not item.optional]
    skipped = [item for item in evaluated if item.status == "skip"]
    conflicts = [item for item in evaluated if item.status == "conflict"]
    optional = [item for item in evaluated if item.status == "optional"]

    print(f"Mode: {mode}")
    print(f"Profile: {profile}")
    print(f"Docs root: {docs_root_name}/")
    print(f"Scripts root: {scripts_root_name}/")
    print("")

    print("Will create:")
    if will_create:
        for item in will_create:
            print(f"- {relative_display(project_root, item.path)}")
    else:
        print("- nothing")

    if will_overwrite:
        print("")
        print("Will overwrite:")
        for item in will_overwrite:
            print(f"- {relative_display(project_root, item.path)}")

    print("")
    print("Will not do:")
    if mode == "legacy":
        print("- move existing documents")
        print("- rewrite existing documents")
        print("- archive files automatically")
    else:
        print("- create speculative docs beyond the chosen profile")
        print("- fill every directory with empty placeholders")
        print("- overwrite existing files unless --force is enabled")

    if skipped:
        print("")
        print("Existing paths kept:")
        for item in skipped:
            print(f"- {relative_display(project_root, item.path)}")

    if optional:
        print("")
        print("Optional seed files not included in this run:")
        for item in optional:
            print(f"- {relative_display(project_root, item.path)}")

    if conflicts:
        print("")
        print("Conflicts:")
        for item in conflicts:
            print(f"- {relative_display(project_root, item.path)}")


def confirm_execution() -> bool:
    if not is_interactive():
        raise SystemExit("Confirmation required in non-interactive usage. Pass --yes to continue.")
    answer = input("Continue? [y/N] ").strip().lower()
    return answer in {"y", "yes"}


def apply_plan(evaluated: list[EvaluatedItem]) -> dict[str, list[str]]:
    results = {"created": [], "overwritten": [], "skipped": [], "conflicts": []}
    for item in evaluated:
        display_path = item.path.as_posix()
        if item.status == "optional":
            continue
        if item.status == "conflict":
            results["conflicts"].append(display_path)
            continue
        if item.status == "skip":
            results["skipped"].append(display_path)
            continue
        if item.kind == "dir":
            item.path.mkdir(parents=True, exist_ok=True)
            results["created"].append(display_path)
            continue
        item.path.parent.mkdir(parents=True, exist_ok=True)
        item.path.write_text(item.content or "", encoding="utf-8", newline="\n")
        bucket = "overwritten" if item.status == "overwrite" else "created"
        results[bucket].append(display_path)
    return results


def build_text_result(project_root: Path, results: dict[str, list[str]], next_step: str) -> str:
    lines: list[str] = []
    if results["created"]:
        lines.append("Created:")
        for path in results["created"]:
            lines.append(f"- {relative_display(project_root, Path(path))}")
        lines.append("")
    if results["overwritten"]:
        lines.append("Overwritten:")
        for path in results["overwritten"]:
            lines.append(f"- {relative_display(project_root, Path(path))}")
        lines.append("")
    if results["skipped"]:
        lines.append("Skipped:")
        for path in results["skipped"]:
            lines.append(f"- {relative_display(project_root, Path(path))}")
        lines.append("")
    if results["conflicts"]:
        lines.append("Conflicts:")
        for path in results["conflicts"]:
            lines.append(f"- {relative_display(project_root, Path(path))}")
        lines.append("")
    lines.append("Next:")
    lines.append(f"- {next_step}")
    return "\n".join(lines)


def preview_payload(
    project_root: Path,
    mode: str,
    profile: str,
    docs_root_name: str,
    scripts_root_name: str,
    evaluated: list[EvaluatedItem],
) -> dict[str, object]:
    return {
        "mode": mode,
        "profile": profile,
        "project_root": project_root.as_posix(),
        "docs_root": docs_root_name,
        "scripts_root": scripts_root_name,
        "plan": {
            "create": [relative_display(project_root, item.path) for item in evaluated if item.status == "create"],
            "overwrite": [relative_display(project_root, item.path) for item in evaluated if item.status == "overwrite"],
            "skip": [relative_display(project_root, item.path) for item in evaluated if item.status == "skip"],
            "conflict": [relative_display(project_root, item.path) for item in evaluated if item.status == "conflict"],
            "optional": [relative_display(project_root, item.path) for item in evaluated if item.status == "optional"],
        },
        "next": next_step_for(mode, profile),
    }


def next_step_for(mode: str, profile: str) -> str:
    if mode == "legacy" and profile == "audit":
        return "Review the audit report, then rerun with `--mode legacy --profile standard` if the repo needs a migration-ready target tree."
    if mode == "legacy":
        return "Use `migrating-project-docs` to classify and migrate the existing documentation into the new structure."
    if mode == "new" and profile == "standard":
        return "Create only the real docs that materially help the project, and use the optional starter templates only when they still fit the work."
    return "Decide whether this repo now needs only a minimal docs skeleton or whether it should be re-run in `standard` mode for navigable project docs."


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    if not project_root.exists() or not project_root.is_dir():
        raise SystemExit(f"Project root does not exist or is not a directory: {project_root}")

    mode, profile = resolve_mode_and_profile(args)
    skill_dir = Path(__file__).resolve().parent.parent
    docs_root_name, scripts_root_name = resolve_structure_roots(project_root, args.existing_convention)

    if mode == "legacy" and profile == "audit":
        audit_data = build_legacy_audit_data(project_root)
        report = build_legacy_audit_report(project_root)
        if args.output:
            output_path = Path(args.output).resolve()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report, encoding="utf-8", newline="\n")
        if args.json:
            payload = {
                "mode": mode,
                "profile": profile,
                "project_root": project_root.as_posix(),
                "audit": audit_data,
                "output": str(Path(args.output).resolve()) if args.output else None,
                "next": next_step_for(mode, profile),
            }
            print(json.dumps(payload, indent=2))
        else:
            print(report)
            if args.output:
                print("")
                print(f"Wrote audit report to {Path(args.output).resolve().as_posix()}")
        return 0

    plan = build_plan(
        project_root=project_root,
        skill_dir=skill_dir,
        mode=mode,
        profile=profile,
        docs_root_name=docs_root_name,
        scripts_root_name=scripts_root_name,
        with_index=args.with_index,
        with_seed_files=args.with_seed_files,
    )
    evaluated = evaluate_plan(plan, force=args.force)

    if args.dry_run:
        if args.json:
            print(
                json.dumps(
                    preview_payload(
                        project_root=project_root,
                        mode=mode,
                        profile=profile,
                        docs_root_name=docs_root_name,
                        scripts_root_name=scripts_root_name,
                        evaluated=evaluated,
                    ),
                    indent=2,
                )
            )
        else:
            print_preview(project_root, mode, profile, evaluated, docs_root_name, scripts_root_name)
        return 0

    print_preview(project_root, mode, profile, evaluated, docs_root_name, scripts_root_name)

    if not args.yes and not confirm_execution():
        print("Aborted.")
        return 1

    results = apply_plan(evaluated)
    next_step = next_step_for(mode, profile)

    if args.json:
        payload = {
            "mode": mode,
            "profile": profile,
            "project_root": project_root.as_posix(),
            "docs_root": docs_root_name,
            "scripts_root": scripts_root_name,
            "results": results,
            "next": next_step,
        }
        print(json.dumps(payload, indent=2))
    else:
        print("")
        print(build_text_result(project_root, results, next_step))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
