# Clase 42 — Docker desde cero y reproducibilidad

## Propósitos

- distinguir imagen, contenedor, registro, volumen y red;
- leer y construir un `Dockerfile` pequeño;
- explicar qué reproduce un contenedor y qué queda por controlar.

## Preparación

Instalar Docker según la guía institucional y verificar `docker version`. Revisar
[`Dockerfile`](Dockerfile), [`demo.py`](demo.py) y
[`../../guias/15_docker.md`](../../guias/15_docker.md).

## Secuencia (120 min)

1. Problema de reproducibilidad y modelo de Docker (25 min).
2. Imagen, capas y contexto de construcción (25 min).
3. Construcción y ejecución del ejemplo (25 min).
4. Volúmenes, redes, variables y Compose (30 min).
5. Ejercicio de salida individual (15 min).

## Evidencia

Comando reproducible, explicación de cada instrucción y registro de versión de la
imagen. No se evalúa solo una captura del contenedor ejecutándose.
