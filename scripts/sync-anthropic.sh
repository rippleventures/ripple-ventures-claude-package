#!/bin/bash
# sync-anthropic.sh — Pull updates to bundled Anthropic skills from a local clone of
# https://github.com/anthropics/financial-services.
#
# Usage:
#   ./scripts/sync-anthropic.sh /path/to/anthropic-financial-services
#
# Walks the agent-plugins in the source repo and updates matching skill folders
# in deals-plugin/skills/ and microsoft-office-plugin/skills/. Does NOT overwrite
# our custom skills (vc-general-counsel, investment-memo-drafter, the orchestration skills).

set -e

REPO="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${1:-}"

if [ -z "$SRC" ] || [ ! -d "$SRC" ]; then
  echo "Usage: $0 /path/to/anthropic-financial-services"
  exit 1
fi

if [ ! -d "$SRC/plugins/agent-plugins" ]; then
  echo "Error: $SRC doesn't look like a clone of anthropics/financial-services"
  echo "(missing $SRC/plugins/agent-plugins/)"
  exit 1
fi

# Skills we want to keep updated from upstream
ANTHROPIC_SKILLS=(
  3-statement-model
  competitive-analysis
  comps-analysis
  dcf-model
  deck-refresh
  earnings-analysis
  earnings-preview
  ib-check-deck
  ic-memo
  idea-generation
  lbo-model
  model-update
  morning-note
  pitch-deck
  portfolio-monitoring
  returns-analysis
  sector-overview
)

# MS Office foundation skills (live in microsoft-office-plugin)
MSOFFICE_SKILLS=(audit-xls xlsx-author pptx-author)

# Scan agent-plugins for the skills
echo "Scanning $SRC/plugins/agent-plugins/ for updates..."
echo ""

updated=0
for skill in "${ANTHROPIC_SKILLS[@]}"; do
  # Find the first agent-plugin that has this skill
  found=""
  for agent_dir in "$SRC"/plugins/agent-plugins/*/; do
    candidate="$agent_dir/skills/$skill"
    if [ -d "$candidate" ]; then
      found="$candidate"
      break
    fi
  done

  if [ -z "$found" ]; then
    echo "  SKIP $skill — not found in any agent-plugin"
    continue
  fi

  dest="$REPO/deals-plugin/skills/$skill"
  if [ ! -d "$dest" ]; then
    mkdir -p "$dest"
  fi

  echo "  $skill ← $(basename $(dirname $(dirname $found)))"
  cp -r "$found"/* "$dest/" 2>/dev/null || true
  updated=$((updated+1))
done

echo ""
echo "MS Office foundation skills:"
for skill in "${MSOFFICE_SKILLS[@]}"; do
  found=""
  for agent_dir in "$SRC"/plugins/agent-plugins/*/; do
    candidate="$agent_dir/skills/$skill"
    if [ -d "$candidate" ]; then
      found="$candidate"
      break
    fi
  done

  if [ -z "$found" ]; then
    echo "  SKIP $skill"
    continue
  fi

  dest="$REPO/microsoft-office-plugin/skills/$skill"
  if [ ! -d "$dest" ]; then
    mkdir -p "$dest"
  fi

  echo "  $skill ← $(basename $(dirname $(dirname $found)))"
  cp -r "$found"/* "$dest/" 2>/dev/null || true
  updated=$((updated+1))
done

echo ""
echo "Synced $updated skills. Run scripts/check.py to validate."
