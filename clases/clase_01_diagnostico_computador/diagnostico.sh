#!/usr/bin/env bash
set -euo pipefail

echo "Arquitectura: $(uname -m)"
echo "Kernel: $(uname -sr)"
echo "Procesadores visibles: $(getconf _NPROCESSORS_ONLN)"
echo "Memoria aproximada:"
free -h | head -n 2
echo "Python resuelto por el shell:"
command -v python3 || true

