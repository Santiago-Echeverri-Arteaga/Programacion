# Docker

Material mínimo para la clase 42.

- `Dockerfile`: imagen Python pequeña.
- `app.py`: programa que muestra el entorno dentro del contenedor.

La demostración completa de dos servicios usa
[`infraestructura/compose.yaml`](../../infraestructura/compose.yaml).
Este ejemplo aislado permite leer `FROM`, `WORKDIR`, `COPY` y `CMD` antes de
introducir Compose.
