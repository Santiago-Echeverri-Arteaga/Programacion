#!/usr/bin/env bash
set -euo pipefail

python --version
git rev-parse --short HEAD
git status --short
python -m pip check
python -m pytest -q

echo "Comprobaciones automáticas terminadas; falta la validación científica."
