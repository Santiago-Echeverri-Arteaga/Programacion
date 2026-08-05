# Inicialización de la base didáctica

PostgreSQL ejecuta estos archivos, en orden alfabético, solamente cuando crea un
directorio de datos vacío:

- `01_esquema.sql`: tablas, claves, restricciones e índices.
- `02_datos.sql`: conjunto pequeño y determinista para consultas y validación.

Editar estos scripts no modifica automáticamente un volumen ya existente. Borrar
un volumen elimina datos; consulte antes el ciclo de vida descrito en
[`../../README.md`](../../README.md).
