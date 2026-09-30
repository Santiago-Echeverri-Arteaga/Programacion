# Biblioteca de física del curso

Ejemplo de apoyo adaptado del paquete trabajado en clase. El nombre de
distribución `fisica-uq-ejemplo` es ilustrativo; no se afirma que esté disponible
en PyPI. El nombre que se importa es `Libreria`.

Desde esta carpeta, con el entorno del curso activo:

```bash
python -m pip install -e .
```

```python
from Libreria import velocidad, integrar_cuadrado
print(velocidad(20, 5))
print(integrar_cuadrado(0, 1, 8))
```

`velocidad` recibe desplazamiento en metros e intervalo positivo en segundos.
La posición y el desplazamiento pueden ser negativos. `integrar_cuadrado`
aproxima la integral de x² por puntos medios, con límites crecientes y un número
entero positivo de subintervalos. `leer_posiciones` recibe una ruta `Path` a un
CSV pequeño con encabezado `tiempo_s,posicion_m` y dos números finitos por fila.
Rechaza archivos sin mediciones. El orden temporal se valida en el análisis.

Solo se utilizan módulos de la biblioteca estándar de Python. `pytest`, `build`
y `twine` son herramientas de prueba/distribución, no dependencias de ejecución.

Antes de publicar una adaptación: escoger nombre disponible y licencia,
identificar autoría, documentar uso y limitaciones, cambiar versión, construir
y probar una instalación normal en un entorno limpio. Este ejemplo no se sube
automáticamente a ningún índice.
