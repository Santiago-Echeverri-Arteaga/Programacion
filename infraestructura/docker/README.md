# Cliente de análisis en Docker

Esta carpeta define la imagen del cliente Python del ejemplo PostgreSQL.

- `Dockerfile`: fija la imagen base, dependencias, usuario y comando.
- `app.py`: espera `DATABASE_URL`, consulta de forma parametrizada y presenta un
  resumen.

La imagen se construye mediante el servicio `analisis` de
[`../compose.yaml`](../compose.yaml); no se ejecuta este directorio aisladamente
sin configurar la red y la base.
