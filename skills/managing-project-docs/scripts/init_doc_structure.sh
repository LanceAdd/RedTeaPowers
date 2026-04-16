#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PYTHON_SCRIPT="$SCRIPT_DIR/init_doc_structure.py"

if [ "$#" -lt 1 ]; then
  echo "Usage: sh scripts/init_doc_structure.sh <project-root> [options]" >&2
  exit 2
fi

PROJECT_ROOT=$1
shift

find_python() {
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

if ! PYTHON_CMD=$(find_python); then
  echo "Python runtime not detected. Install Python or run the initializer through another wrapper." >&2
  exit 1
fi

RESOLVED_PROJECT_ROOT=$(cd "$PROJECT_ROOT" && pwd)
"$PYTHON_CMD" "$PYTHON_SCRIPT" "$RESOLVED_PROJECT_ROOT" "$@"
