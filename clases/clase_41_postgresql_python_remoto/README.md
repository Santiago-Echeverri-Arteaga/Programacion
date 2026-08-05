# Clase 41 — PostgreSQL desde Python y bases remotas

## Propósitos

- conectar Python a PostgreSQL sin escribir secretos en el código;
- ejecutar consultas parametrizadas y cerrar recursos;
- comprender TLS, latencia, permisos y límites de una base remota.

## Preparación

Configurar `DATABASE_URL` según la guía. Nunca publicar credenciales ni copiar la
URL real a un notebook o repositorio.

## Secuencia (120 min)

1. Repaso cliente–servidor y cadena de conexión (20 min).
2. Variables de entorno, permisos y TLS (20 min).
3. Consulta parametrizada con [`cliente.py`](cliente.py) (30 min).
4. Demostración docente de servicio remoto de solo lectura (25 min).
5. Fallos, latencia y ejercicio individual (25 min).

## Evidencia

Consulta parametrizada reproducible y explicación de qué cambia entre conexión
local y remota. La cuenta remota será temporal y de mínimos privilegios.
