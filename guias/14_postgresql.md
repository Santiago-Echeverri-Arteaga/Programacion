# Guía 14 — PostgreSQL desde SQL puro hasta Python

## Ficha

- Realización: martes 3 de noviembre y primera parte del miércoles 4 de noviembre
  de 2026.
- Duración: hasta 180 minutos.
- Nivel de IA: 1.
- Resultados: RA 4, RA 8 y RA 10.
- Infraestructura: `infraestructura/compose.yaml`.

## Objetivo

Dar una visión realista de una base de datos como servicio independiente. Python
es un cliente posible, no el lugar donde “vive SQL”.

## Encuentro A — SQL puro

### Modelo conceptual

- servidor, cliente, base de datos y sesión;
- tabla, fila, columna, tipo y valor nulo;
- clave primaria, clave foránea y restricción;
- consulta y resultado;
- transacción;
- esquema y procedencia.

### Inicio

```bash
cd infraestructura
cp .env.example .env
docker-compose up -d db
docker-compose exec db psql -U fisica -d observatorio
```

Dentro de `psql`:

```text
\conninfo
\dt
\d mediciones
\i /material/consultas_guiadas.sql
```

Se debe aclarar que los comandos con `\` pertenecen a `psql`, no al lenguaje
SQL.

### Contenido SQL

1. `SELECT`, alias y expresiones.
2. `WHERE`, valores nulos y operadores.
3. `ORDER BY` y `LIMIT`.
4. `JOIN` con claves explícitas.
5. `GROUP BY`, agregados y `HAVING`.
6. Una demostración breve de transacción: `BEGIN`, `ROLLBACK`, `COMMIT`.
7. Restricciones como evidencia de calidad de datos.

No se cubren administración, optimización avanzada, procedimientos ni permisos
complejos.

## Encuentro B — Python y servicio remoto

### Conexión local

Desde el host, la URL tiene forma:

```text
postgresql://fisica:CLAVE@localhost:5432/observatorio
```

Desde otro contenedor del mismo Compose, el host es `db`, no `localhost`.

```bash
export DATABASE_URL='postgresql://fisica:CLAVE@localhost:5432/observatorio'
python ../Codigos/15_sql_postgresql/conexion_postgresql.py
```

### Puntos obligatorios

- credenciales en variables de entorno, no en el código;
- consultas parametrizadas, nunca concatenación de entradas;
- conexiones y cursores como administradores de contexto;
- transacciones, confirmación y reversión;
- diferencia entre traer todos los datos y calcular en el servidor;
- no versionar `.env`.

### Base remota

El docente suministra una cuenta temporal y de solo lectura. La conexión debe
exigir TLS:

```text
postgresql://usuario:clave@host-remoto:5432/base?sslmode=require
```

Demostración recomendada:

1. ejecutar la misma consulta con `psql`;
2. ejecutar el cliente Python sin cambiar el código, solo `DATABASE_URL`;
3. mostrar latencia y explicar que los datos cruzan una red;
4. intentar una escritura y verificar que el usuario de lectura no tiene permiso;
5. revocar o rotar las credenciales después de la clase.

No se proyectarán secretos reales ni se entregará una cuenta con privilegios de
administración.

## Salida individual

Escribir una consulta que responda una pregunta física con `JOIN` y agregación, y
explicar qué trabajo realiza PostgreSQL y qué trabajo debería quedar en Python.

## Referencias

- Tutorial oficial: <https://www.postgresql.org/docs/current/tutorial-sql.html>
- Psycopg 3: <https://www.psycopg.org/psycopg3/docs/basic/usage.html>
