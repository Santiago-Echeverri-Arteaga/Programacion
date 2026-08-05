#!/usr/bin/env bash
set -euo pipefail

base="${TMPDIR:-/tmp}/curso_rutas_${USER}"
mkdir -p "$base/experimento uno/datos" "$base/scripts"
printf 't_s,x_m\n0,0\n1,2\n' > "$base/experimento uno/datos/serie.csv"
echo "Árbol creado en: $base"
find "$base" -maxdepth 3 -print
echo "Pruebe rutas relativas desde: $base/scripts"

