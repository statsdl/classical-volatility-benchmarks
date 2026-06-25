#!/usr/bin/env bash
set -euo pipefail

git add docs/results
if git diff --cached --quiet; then
  echo "No docs/results changes to commit."
else
  git commit -m "Add classical volatility benchmarks results"
  git push
fi
