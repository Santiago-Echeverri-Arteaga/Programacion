#!/usr/bin/env bash
set -euo pipefail

python3 -c 'import time; print("inicio"); time.sleep(5); print("fin")' &
pid=$!
echo "Proceso creado con PID $pid"
ps -p "$pid" -o pid,ppid,state,comm
wait "$pid"
echo "Código de salida: $?"

