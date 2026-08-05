#!/usr/bin/env bash
set -euo pipefail

for ruta in README.md datos scripts resultados; do
    if [[ ! -e "$ruta" ]]; then
        echo "Falta: $ruta" >&2
        exit 1
    fi
done
echo "Estructura mínima presente"

