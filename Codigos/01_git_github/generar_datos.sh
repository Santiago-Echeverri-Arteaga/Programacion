#!/usr/bin/env bash
set -euo pipefail

salida="${1:-mediciones_demo.csv}"
printf 'tiempo_s,posicion_m\n0.0,0.0\n0.5,1.2\n1.0,2.4\n' > "$salida"
echo "Creado $salida; inspeccione git status y git diff."

