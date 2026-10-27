# Pandas y PostgreSQL · tres clases de 90 minutos

- Clase 1: Pandas en Colab (90 min).
- Clase 2: Pandas (45 min) y SQL puro (45 min).
- Clase 3: PostgreSQL con psql, archivos SQL y Bash en VS Code conectado a Ubuntu WSL2 (90 min).

Abre `01_clases_magistrales.ipynb` en Colab para Pandas y como lectura. Antes de la segunda clase, completa `GUIA_POSTGRESQL.md`; la instalación se hace fuera de los 270 minutos. Ejecuta SQL desde Ubuntu, sin conectar Colab al servidor. `02_practica_sin_nota.ipynb` contiene práctica autónoma y sin respuestas. El cierre muestra un pipeline local `.sh + .py + .sql`; su modificación y el cliente Psycopg quedan como ampliación en `ampliacion/`.

Se usa [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/), datos científicos públicos, licencia CC0. El notebook lee un CSV por URL; `datos/penguins.csv` es la copia de contingencia. Incluye opciones de Kaggle, Google Drive y lectura desde PC. Los IDs son claves de fila de esta copia, no identificadores biológicos.

Descarga el paquete completo para conservar guías, scripts y datos. Las soluciones del docente se distribuyen por separado. No se proporcionan modelos, convoluciones, FFT ni verificaciones del trabajo final, y no se añade SQL a sus requisitos.

Estado de comprobación: notebooks Python y componentes Python del pipeline probados con la copia local del CSV. La instalación WSL2, los scripts SQL y el pipeline completo requieren una prueba en PostgreSQL antes de clase.
