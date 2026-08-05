#!/usr/bin/env bash
set -euo pipefail

destino="$(mktemp -d "${TMPDIR:-/tmp}/demo_git_curso.XXXXXX")"
echo "Repositorio temporal: $destino"
cd "$destino"
git init
git config user.name "Estudiante Demo"
git config user.email "demo@example.invalid"
printf 'print("primera versión")\n' > modelo.py
git add modelo.py
git commit -m "Agrega modelo mínimo"
printf 'print("segunda versión")\n' >> modelo.py
git status --short
git diff
