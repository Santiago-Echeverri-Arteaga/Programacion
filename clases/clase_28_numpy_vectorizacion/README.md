# Clase 28 — NumPy: vistas, broadcasting, vectorización y azar

## Fecha y práctica previa al laboratorio 4

Ruta vigente: 15 de octubre. Seguir `vectorizacion.py` y después
[`pasos_1d.py`](pasos_1d.py): esta demo 1D enseña `Generator.integers`, formas,
ejes, `cumsum`, posición inicial, media de cuadrados y comprobación de pasos.
No resuelve la caminata 2D del laboratorio. Explicar estas operaciones antes
de abrir el laboratorio el 20 de octubre; si falta una, simplificar su requisito.

Distribución de 120 min: formas/vistas 20, broadcasting 25, vectorización 20,
demo 1D y repetibilidad 35, práctica/cierre 20. Cambiar la semilla, comparar
`axis=0` con `axis=1` y predecir por qué hay una columna adicional de posiciones.

## Propósitos

- distinguir vista y copia;
- razonar sobre compatibilidad de formas en broadcasting;
- vectorizar una operación y controlar un generador aleatorio.

## Preparación

Anotar las formas intermedias de [`vectorizacion.py`](vectorizacion.py).

## Secuencia (120 min)

1. Vistas, copias y efectos laterales (25 min).
2. Reglas de broadcasting mediante formas (30 min).
3. Vectorización frente a ciclo explícito (25 min).
4. Aleatoriedad reproducible (25 min).
5. Cierre individual (15 min).

## Evidencia

Explicación de una operación de broadcasting, semilla declarada y verificación
contra un caso calculable a mano.
