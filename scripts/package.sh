#!/bin/bash
# package.sh — Zip every *-plugin/ folder into a .plugin file in /tmp/.
#
# Usage:
#   ./scripts/package.sh                 # all plugins
#   ./scripts/package.sh productivity    # one plugin (matched by prefix)
#
# Outputs go to /tmp/<plugin-name>.plugin

set -e

REPO="$(cd "$(dirname "$0")/.." && pwd)"
FILTER="${1:-}"
OUT_DIR="/tmp"

# Make sure all plugins pass validation first
echo "Running check.py before packaging..."
python3 "$REPO/scripts/check.py" || {
  echo ""
  echo "Validation failed. Fix errors before packaging."
  exit 1
}
echo ""

for plugin_dir in "$REPO"/*-plugin/; do
  plugin_name=$(basename "$plugin_dir")

  # Filter if a name was passed
  if [ -n "$FILTER" ] && [[ "$plugin_name" != *"$FILTER"* ]]; then
    continue
  fi

  # Read the plugin name from manifest (this is the canonical name for the .plugin file)
  manifest="$plugin_dir/.claude-plugin/plugin.json"
  if [ ! -f "$manifest" ]; then
    echo "  SKIP: $plugin_name has no plugin.json"
    continue
  fi

  canonical_name=$(python3 -c "import json; print(json.load(open('$manifest'))['name'])")
  out_file="$OUT_DIR/$canonical_name.plugin"

  echo "Packaging $plugin_name → $out_file"

  # Use --symlinks so symlinks are preserved; -X strips macOS extended attrs
  cd "$plugin_dir"
  rm -f "$out_file"
  zip -r -X "$out_file" . -x "*.DS_Store" -x "*.bak" > /dev/null
  cd "$REPO"

  size=$(du -h "$out_file" | cut -f1)
  echo "  ✓ $size"
done

echo ""
echo "Done. Files in $OUT_DIR/:"
ls -lh "$OUT_DIR"/*.plugin 2>/dev/null || true
