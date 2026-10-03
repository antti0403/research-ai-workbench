#!/usr/bin/env bash
# Local launcher. Does not change shell profiles, global Python, or account settings.
set -euo pipefail
workbench_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ "${WORKBENCH_FORCE_BOOTSTRAP:-0}" != 1 ]]; then
  for workbench_python in python3 python; do
    if command -v "$workbench_python" >/dev/null 2>&1 && "$workbench_python" -c 'import sys,venv; sys.exit(sys.version_info < (3,11))' >/dev/null 2>&1; then
      exec "$workbench_python" "$workbench_dir/workbench.py" setup "$@"
    fi
  done
fi
for workbench_argument in "$@"; do
  if [[ "$workbench_argument" == --offline ]]; then
    printf '%s\n' 'Offline mode requires an existing Python 3.11+; no download was started.' >&2
    exit 2
  fi
done
printf '%s\n' 'Preparing a local Python runtime. This downloads pinned uv and Python from Astral; no admin access or shell profile changes.'
workbench_workspace="$HOME/ResearchWorkbench"
workbench_expect_path=0
for workbench_argument in "$@"; do
  if [[ "$workbench_expect_path" == 1 ]]; then
    workbench_workspace="$workbench_argument"
    workbench_expect_path=0
  elif [[ "$workbench_argument" == --workspace ]]; then
    workbench_expect_path=1
  elif [[ "$workbench_argument" == --workspace=* ]]; then
    workbench_workspace="${workbench_argument#--workspace=}"
  fi
done
[[ "$workbench_expect_path" == 0 && -n "$workbench_workspace" ]] || { printf '%s\n' 'A workspace path is required.' >&2; exit 1; }
[[ "$workbench_workspace" != '~/'* ]] || workbench_workspace="$HOME/${workbench_workspace#\~/}"
mkdir -p "$workbench_workspace"
workbench_workspace="$(cd -- "$workbench_workspace" && pwd -P)"
if [[ "$workbench_workspace" == / || "$workbench_workspace" == "$HOME" || "$workbench_dir/" == "$workbench_workspace/"* ]]; then
  printf '%s\n' 'Choose a dedicated workspace outside the installer source.' >&2; exit 1
fi
workbench_bootstrap="$workbench_workspace/.workbench/bootstrap"
for workbench_path in "$workbench_workspace/.workbench" "$workbench_bootstrap"; do
  [[ ! -L "$workbench_path" ]] || { printf '%s\n' 'Preserved a symbolic link at the runtime destination.' >&2; exit 1; }
done
mkdir -p "$workbench_bootstrap"
export UV_UNMANAGED_INSTALL="$workbench_bootstrap/uv"
export UV_PYTHON_INSTALL_DIR="$workbench_bootstrap/python"
export UV_PYTHON_BIN_DIR="$workbench_bootstrap/bin"
export UV_CACHE_DIR="$workbench_bootstrap/cache"
if [[ ! -x "$UV_UNMANAGED_INSTALL/uv" ]]; then
  workbench_installer="$(mktemp "$workbench_bootstrap/installer.XXXXXX")"
  trap 'rm -f "$workbench_installer"' EXIT
  curl --fail --location --silent --show-error --proto '=https' --proto-redir '=https' --max-time 120 \
    https://astral.sh/uv/0.12.22/install.sh -o "$workbench_installer"
  if command -v shasum >/dev/null 2>&1; then
    workbench_hash="$(shasum -a 256 "$workbench_installer" | cut -d ' ' -f 1)"
  elif command -v sha256sum >/dev/null 2>&1; then
    workbench_hash="$(sha256sum "$workbench_installer" | cut -d ' ' -f 1)"
  else
    printf '%s\n' 'A SHA-256 tool is required; no downloaded code was executed.' >&2
    exit 1
  fi
  [[ "$workbench_hash" == 58488ae8dbd0773134c92c85e901430e33f99d975bd7f929d26aa9ab0c2f9390 ]] || { printf '%s\n' 'uv installer checksum mismatch.' >&2; exit 1; }
  sh "$workbench_installer"
fi
"$UV_UNMANAGED_INSTALL/uv" run --no-project --python 3.12 python "$workbench_dir/workbench.py" setup "$@"
