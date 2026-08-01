# Infraestructura reproducible

Este módulo permite mostrar PostgreSQL y Docker desde cero sin depender de una
instalación local del servidor de base de datos.

## Inicio rápido

Desde este directorio:

```bash
cp .env.example .env
docker-compose up -d db
docker-compose exec db psql -U fisica -d observatorio
```

En instalaciones donde funciona el complemento moderno, `docker compose` puede
usarse en lugar de `docker-compose`.

La contraseña de `.env.example` es únicamente didáctica y local. Debe cambiarse
antes de exponer un servicio a una red.

## Contenido

- `compose.yaml`: servidor PostgreSQL y aplicación Python de demostración.
- `postgresql/init/`: esquema y datos ejecutados al crear el volumen por primera
  vez.
- `postgresql/consultas_guiadas.sql`: consultas para la clase de SQL puro.
- `docker/Dockerfile`: imagen mínima para la aplicación de análisis.
- `docker/app.py`: cliente Python que se conecta al servidor por la red interna.

## Ciclo de vida

```bash
# Ver servicios
docker-compose ps

# Ver registros
docker-compose logs db

# Ejecutar el cliente Python dentro de un contenedor
docker-compose --profile demo run --rm analisis

# Detener sin eliminar los datos
docker-compose down
```

Para reinicializar completamente la base se debe eliminar el volumen. Esta acción
borra los datos y solo debe hacerse en el entorno didáctico:

```bash
docker-compose down --volumes
```

Los scripts de `postgresql/init/` solo se ejecutan cuando el volumen está vacío.

