#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Iterable


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

DOC_DIR_HINTS = {
    "docs",
    "doc",
    "notes",
    "wiki",
    "design",
    "spec",
    "specs",
    "plans",
    "plan",
}

TYPE_KEYWORDS = {
    "guide": {
        "guide",
        "phase charter",
        "stage charter",
        "development charter",
        "delivery charter",
        "phase guide",
        "stage guide",
        "phase outline",
        "stage outline",
        "phase principles",
        "stage principles",
    },
    "discuss": {
        "discussion",
        "requirements discussion",
        "open question",
        "tradeoff",
        "proposal",
        "proposed",
        "option",
        "alternative",
        "decision needed",
        "decision debate",
    },
    "spec": {
        "spec",
        "requirements",
        "should",
        "must",
        "success criteria",
        "scope",
        "behavior",
        "accepted",
    },
    "plan": {
        "plan",
        "milestone",
        "phase",
        "implementation",
        "step",
        "dependency",
        "sequence",
        "rollout",
    },
    "reference": {
        "reference",
        "overview",
        "architecture",
        "orientation",
        "how it works",
        "topic map",
        "schema",
        "api",
        "glossary",
        "lookup",
        "config",
        "field",
        "endpoint",
        "parameter",
    },
    "change": {
        "change",
        "changelog",
        "updated",
        "changed",
        "this round",
        "release note",
        "migration summary",
    },
    "archive": {
        "archive",
        "legacy",
        "retired",
        "deprecated",
        "historical",
        "history",
        "v1",
        "old",
    },
}


@dataclass
class DocRecord:
    path: Path
    relative_path: str
    detected_encoding: str
    suggested_type: str
    suggested_action: str
    batch_key: str
    reason: str
    line_count: int
    char_count: int
    mixed_purpose: bool
    active_state: str
    type_scores: Counter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan a legacy documentation tree and generate a RedTeaPowers "
            "migration plan in UTF-8 markdown."
        )
    )
    parser.add_argument("source_root", help="Root directory to scan")
    parser.add_argument(
        "--output",
        help="Optional markdown output path. If omitted, write to stdout.",
    )
    parser.add_argument(
        "--title",
        default="Legacy Documentation Migration Plan",
        help="Title for the generated markdown document",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=500,
        help="Maximum number of candidate files to include in the report",
    )
    return parser.parse_args()


def should_scan(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.stat().st_size > 1024 * 1024:
        return False
    return True


def looks_like_doc(path: Path) -> bool:
    lower_parts = {part.lower() for part in path.parts}
    stem = path.stem.lower()
    name = path.name.lower()
    return (
        bool(lower_parts & DOC_DIR_HINTS)
        or any(token in name for token in ("readme", "spec", "plan", "todo", "note", "change", "design"))
        or any(token in stem for token in ("requirements", "architecture", "roadmap", "research"))
    )


def iter_candidate_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file() and should_scan(path) and looks_like_doc(path):
            yield path


def read_text_with_guess(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "gb18030", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace"), "latin-1-replace"


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def score_types(path: Path, text: str) -> Counter:
    haystack = f"{path.name.lower()} {normalize_text(text[:20000])}"
    scores: Counter[str] = Counter()

    for doc_type, keywords in TYPE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in haystack:
                scores[doc_type] += 1

    if re.search(r"\bmust\b|\bshould\b", text.lower()):
        scores["spec"] += 1
    if re.search(r"\btask\b|\btodo\b|\bnext step\b|\bblocker\b", text.lower()):
        scores["plan"] += 1
    if re.search(r"\bapi\b|\bschema\b|\bfield\b|\bendpoint\b", text.lower()):
        scores["reference"] += 1
    if re.search(r"\bphase\b|\bmilestone\b|\bdependency\b|\brollout\b", text.lower()):
        scores["plan"] += 1
    if re.search(r"\bproposal\b|\btradeoff\b|\bopen question\b", text.lower()):
        scores["discuss"] += 1

    if not scores:
        scores["reference"] = 1
    return scores


def detect_active_state(path: Path, text: str, scores: Counter) -> str:
    name = path.as_posix().lower()
    if any(token in name for token in ("archive", "legacy", "deprecated", "retired", "/old/", "/history/")):
        return "historical"
    if scores["archive"] >= 2:
        return "historical"
    if scores["plan"] >= 2 or "next step" in text.lower() or "blocker" in text.lower():
        return "active"
    return "active"


def detect_mixed_purpose(scores: Counter, line_count: int) -> bool:
    nonzero = [doc_type for doc_type, score in scores.items() if score >= 2]
    strong = [doc_type for doc_type, score in scores.items() if score >= 3]
    return len(nonzero) >= 3 or (len(strong) >= 2 and line_count >= 80)


def pick_suggested_type(scores: Counter, mixed_purpose: bool) -> str:
    if mixed_purpose:
        ordered = [doc_type for doc_type, _ in scores.most_common(2)]
        return " + ".join(ordered)
    return scores.most_common(1)[0][0]


def choose_action(
    path: Path,
    suggested_type: str,
    mixed_purpose: bool,
    active_state: str,
    line_count: int,
    char_count: int,
) -> tuple[str, str]:
    lower_name = path.name.lower()
    if active_state == "historical":
        return "archive", "Historical or legacy signals are stronger than active-work signals."
    if mixed_purpose:
        return "split", "The file appears to mix multiple document purposes."
    if line_count >= 180 or char_count >= 14000:
        return "split", "The file is long enough that migration should likely split structure by purpose."
    if any(token in lower_name for token in ("todo", "tasks", "next-steps", "next_steps")):
        return "move", "The file looks like active execution work and should likely become a plan or be reduced into session task tracking."
    if any(token in lower_name for token in ("readme", "overview", "architecture")) and suggested_type in ("guide", "reference"):
        return "keep-and-rename", "The content looks structurally useful but may need target taxonomy naming."
    return "move-and-renumber", "The content seems reusable but should likely be moved into the target taxonomy."


def batch_key_for(path: Path, suggested_type: str, action: str) -> str:
    parent = path.parent.name or "."
    return f"{parent} -> {suggested_type} ({action})"


def build_records(root: Path, max_files: int) -> list[DocRecord]:
    records: list[DocRecord] = []
    for index, path in enumerate(iter_candidate_files(root)):
        if index >= max_files:
            break
        text, encoding = read_text_with_guess(path)
        line_count = text.count("\n") + 1
        char_count = len(text)
        scores = score_types(path, text)
        mixed = detect_mixed_purpose(scores, line_count)
        suggested_type = pick_suggested_type(scores, mixed)
        active_state = detect_active_state(path, text, scores)
        action, reason = choose_action(
            path=path,
            suggested_type=suggested_type,
            mixed_purpose=mixed,
            active_state=active_state,
            line_count=line_count,
            char_count=char_count,
        )
        records.append(
            DocRecord(
                path=path,
                relative_path=path.relative_to(root).as_posix(),
                detected_encoding=encoding,
                suggested_type=suggested_type,
                suggested_action=action,
                batch_key=batch_key_for(path, suggested_type, action),
                reason=reason,
                line_count=line_count,
                char_count=char_count,
                mixed_purpose=mixed,
                active_state=active_state,
                type_scores=scores,
            )
        )
    return records


def family_summaries(records: list[DocRecord]) -> list[tuple[str, list[DocRecord]]]:
    grouped: dict[str, list[DocRecord]] = defaultdict(list)
    for record in records:
        grouped[record.batch_key].append(record)
    ranked = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    return ranked


def render_markdown(title: str, root: Path, records: list[DocRecord]) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    action_counts = Counter(record.suggested_action for record in records)
    type_counts = Counter(record.suggested_type for record in records)
    encoding_counts = Counter(record.detected_encoding for record in records)
    family_items = family_summaries(records)

    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"Source root: `{root.as_posix()}`")
    lines.append(f"Generated: {generated_at}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Candidate files scanned: {len(records)}")
    lines.append(f"- Suggested actions: {', '.join(f'{k}={v}' for k, v in action_counts.most_common()) or 'none'}")
    lines.append(f"- Suggested target types: {', '.join(f'{k}={v}' for k, v in type_counts.most_common()) or 'none'}")
    lines.append(f"- Detected encodings: {', '.join(f'{k}={v}' for k, v in encoding_counts.most_common()) or 'none'}")
    lines.append("")
    lines.append("## Recommended Migration Batches")
    lines.append("")

    if not family_items:
        lines.append("- No candidate files were detected.")
    else:
        for batch_key, batch_records in family_items:
            target_types = Counter(record.suggested_type for record in batch_records)
            actions = Counter(record.suggested_action for record in batch_records)
            lines.append(f"### {batch_key}")
            lines.append("")
            lines.append(f"- Files: {len(batch_records)}")
            lines.append(f"- Target types: {', '.join(f'{k}={v}' for k, v in target_types.most_common())}")
            lines.append(f"- Actions: {', '.join(f'{k}={v}' for k, v in actions.most_common())}")
            if len(batch_records) >= 3:
                lines.append("- Batch note: same-kind cleanup is visible; migrate this set as one pass by default.")
            lines.append("- Suggested files:")
            for record in batch_records[:10]:
                suffix = " mixed-purpose" if record.mixed_purpose else ""
                lines.append(
                    f"  - `{record.relative_path}` -> `{record.suggested_type}` via `{record.suggested_action}`"
                    f" ({record.active_state}, {record.line_count} lines,{suffix or ' focused'})"
                )
            if len(batch_records) > 10:
                lines.append(f"  - ... and {len(batch_records) - 10} more")
            lines.append("")

    lines.append("## File-Level Decisions")
    lines.append("")
    lines.append("| Source | Suggested type | Action | State | Encoding | Notes |")
    lines.append("|--------|----------------|--------|-------|----------|-------|")
    for record in records:
        notes = [record.reason]
        if record.mixed_purpose:
            notes.append("mixed-purpose")
        if record.detected_encoding not in {"utf-8", "utf-8-sig"}:
            notes.append("normalize to utf-8")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{record.relative_path}`",
                    f"`{record.suggested_type}`",
                    f"`{record.suggested_action}`",
                    record.active_state,
                    f"`{record.detected_encoding}`",
                    "; ".join(notes),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Recommended Follow-Up")
    lines.append("")
    lines.append("- Review the suggested batches before rewriting files.")
    lines.append("- Split mixed-purpose long docs before polishing wording.")
    lines.append("- Merge same-kind low-risk fragments into fewer active docs.")
    lines.append("- Archive clearly historical material instead of leaving it active.")
    lines.append("- Renumber moved docs and repair internal links.")
    lines.append("- Rewrite all migrated outputs as UTF-8.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.source_root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Source root does not exist or is not a directory: {root}")

    records = build_records(root, max_files=args.max_files)
    markdown = render_markdown(args.title, root, records)

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8", newline="\n")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
