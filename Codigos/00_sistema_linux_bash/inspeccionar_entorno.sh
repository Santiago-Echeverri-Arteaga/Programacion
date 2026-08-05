#!/usr/bin/env bash
set -euo pipefail

echo "Sistema y kernel:"
uname -a

echo "Directorio de trabajo:"
pwd

echo "Shell actual:"
printf '%s\n' "${SHELL:-no disponible}"

echo "Procesos del usuario:"
ps -u "$(id -u)" -o pid,comm --sort=comm | head

echo "Uso del sistema de archivos:"
df -h .

