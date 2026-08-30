# Clase regular — SciPy para problemas numéricos seleccionados

La carpeta conserva su nombre histórico, pero esta clase regular desarrolla solo
SciPy. SymPy se aborda exclusivamente en la recuperación 1.

## Propósitos

- reconocer cuándo conviene usar una rutina numérica probada;
- resolver un ejemplo de raíz, integración y ajuste;
- leer convergencia, estimación de error y residuos;
- verificar cada resultado contra un caso conocido o un cálculo independiente.

## Demo

[`herramientas.py`](herramientas.py) contiene tres ejemplos pequeños:

1. raíz de `x³-2` con intervalo acotado y comprobación del residuo;
2. integral de `x²` comparada con `1/3`;
3. ajuste lineal con inspección de residuos.

## Secuencia (120 min)

1. Mapa problema–rutina y lectura de documentación (20 min).
2. Raíces y necesidad de un intervalo válido (25 min).
3. Integración y estimación de error (25 min).
4. Ajuste, parámetros y residuos (30 min).
5. Verificación individual (20 min).

## Práctica

1. Cambie el intervalo de la raíz y explique un caso que deba fallar.
2. Integre una función con resultado analítico conocido y compare diferencias.
3. Agregue un dato atípico al ajuste, observe los parámetros y discuta el
   residuo sin eliminarlo silenciosamente.
4. Para cada resultado, escriba una comprobación que no dependa de confiar en la
   misma llamada de SciPy.

No se desarrollan aquí los algoritmos internos de SciPy ni cálculo simbólico.
