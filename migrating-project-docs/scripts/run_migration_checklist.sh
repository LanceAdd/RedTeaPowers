#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SKILL_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
PYTHON_SCRIPT="$SCRIPT_DIR/generate_migration_checklist.py"
TEMPLATE_PATH="$SKILL_DIR/references/003-manual-migration-checklist-template.md"

if [ "$#" -lt 1 ]; then
  echo "Usage: sh scripts/run_migration_checklist.sh <source-root> [--output <target-markdown>] [--title <title>] [--force-fallback]" >&2
  exit 2
fi

SOURCE_ROOT=$1
shift
OUTPUT=""
TITLE="Legacy Documentation Migration Checklist"
FORCE_FALLBACK=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --output)
      OUTPUT=$2
      shift 2
      ;;
    --title)
      TITLE=$2
      shift 2
      ;;
    --force-fallback)
      FORCE_FALLBACK=1
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

find_python() {
  if [ "$FORCE_FALLBACK" -eq 1 ]; then
    return 1
  fi
  if command -v python >/dev/null 2>&1; then
    printf '%s\n' "python"
    return 0
  fi
  if command -v python3 >/dev/null 2>&1; then
    printf '%s\n' "python3"
    return 0
  fi
  return 1
}

render_template() {
  GENERATED_AT=$(date -u +"%Y-%m-%d %H:%M UTC")
  sed \
    -e "s|{{TITLE}}|$TITLE|g" \
    -e "s|{{SOURCE_ROOT}}|$RESOLVED_SOURCE_ROOT|g" \
    -e "s|{{GENERATED_AT}}|$GENERATED_AT|g" \
    "$TEMPLATE_PATH"
}

RESOLVED_SOURCE_ROOT=$(cd "$SOURCE_ROOT" && pwd)

if PYTHON_CMD=$(find_python); then
  if [ -n "$OUTPUT" ]; then
    "$PYTHON_CMD" "$PYTHON_SCRIPT" "$RESOLVED_SOURCE_ROOT" --output "$OUTPUT" --title "$TITLE"
  else
    "$PYTHON_CMD" "$PYTHON_SCRIPT" "$RESOLVED_SOURCE_ROOT" --title "$TITLE"
  fi
  exit 0
fi

echo "Python runtime not detected. Falling back to the manual migration checklist template." >&2

if [ -n "$OUTPUT" ]; then
  mkdir -p "$(dirname "$OUTPUT")"
  render_template > "$OUTPUT"
  printf '%s\n' "Wrote manual fallback checklist to $OUTPUT"
else
  render_template
fi
