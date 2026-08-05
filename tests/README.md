# Pruebas del repositorio

Esta carpeta contiene comprobaciones automáticas de los ejemplos públicos y de la
infraestructura docente. No contiene soluciones de laboratorios ni preguntas de
evaluación.

Desde la raíz del repositorio:

```bash
python -m pytest -q
```

`pytest.ini` limita la recolección a esta carpeta. Los archivos de prueba dentro
de `clases/` son material didáctico y se ejecutan desde su clase correspondiente.

Las pruebas verifican comportamientos concretos; aprobarlas no demuestra por sí
solo corrección física, calidad de análisis o cumplimiento de una guía.
