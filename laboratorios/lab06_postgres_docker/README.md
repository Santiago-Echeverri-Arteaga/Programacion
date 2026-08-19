# Laboratorio 6 — De PostgreSQL a una figura reproducible

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con comprobación individual |
| Herramientas | PostgreSQL, `psql`, Python, psycopg y Docker Compose |
| IA | Nivel 2: crítica/pruebas después de una primera versión propia; declarar |
| Archivo inicial | [`consulta_y_figura.py`](consulta_y_figura.py) |

## Sincronización

- Realización: martes 10 de noviembre de 2026.
- Último contenido requerido: miércoles 4 de noviembre; el jueves 5 es integración
  guiada y congelamiento de requisitos del proyecto.
- La guía suministra el esquema, el archivo Compose y la estructura del cliente;
  no se exige diseñar infraestructura desde cero.

## 2. Pregunta de trabajo

¿Puede construirse un análisis verificable cuyo origen sea una base PostgreSQL y
que se ejecute de la misma manera dentro de un contenedor?

## 3. Marco teórico breve

PostgreSQL es un sistema cliente–servidor: SQL define y consulta relaciones bajo
restricciones. Una unión combina tablas según claves y una agregación cambia la
unidad de análisis; ambas deben validarse. Las consultas parametrizadas separan
datos de instrucciones. Docker empaqueta sistema y dependencias en imágenes y
ejecuta contenedores aislados; Compose conecta servicios mediante una red y
volúmenes. Dentro de un contenedor, `localhost` se refiere al propio contenedor.
Contenerizar mejora repetibilidad, pero no valida datos ni resultados físicos.

## 4. Objetivos

- formular y probar una consulta científica primero en SQL puro;
- conectar Python mediante parámetros y secretos externos;
- validar granularidad, unidades y al menos un resultado manual;
- reproducir el flujo completo con Docker Compose.

## 5. Materiales, seguridad y acceso

- infraestructura de [`../../infraestructura/`](../../infraestructura/README.md);
- Docker, Compose, `psql` y Python;
- credenciales locales de desarrollo suministradas mediante `.env` no versionado;
- cuenta remota temporal de solo lectura, si el docente la habilita.

Nunca publique credenciales ni datos sensibles. El acceso remoto usa TLS y mínimo
privilegio; al terminar se revoca. La IA no recibe URLs, credenciales o datos no
autorizados. Declare su uso en `AI_USAGE.md`.

## 6. Procedimiento

1. Dibuje la arquitectura: cliente, servicio PostgreSQL, volumen, red y salida.
2. Inicie la infraestructura y compruebe estado y registros sin borrar volúmenes.
3. Explore tablas, claves y restricciones desde `psql`.
4. Formule una pregunta que requiera al menos un `JOIN` y una agregación.
5. Escriba la consulta en un archivo `.sql`; prediga columnas y número de filas.
6. Ejecútela en `psql` y valide clave de agrupación, nulos, unidades y granularidad.
7. Calcule manualmente un subconjunto y compárelo con SQL.
8. Ejecute la consulta parametrizada desde Python; no concatene valores externos.
9. Construya una tabla o figura científica a partir del resultado.
10. Construya el contenedor del cliente y ejecútelo en la red de Compose usando el
    nombre del servicio, no `localhost`.
11. Pruebe desde un entorno limpio siguiendo únicamente el README.
12. Si hay cuenta remota, cambie solo `DATABASE_URL`, exija TLS y compare esquema,
    latencia y resultado; no incluya la URL en evidencias.
13. Registre consulta, dependencias, comandos, versión Git y asistencia de IA.

## 7. Resultados y discusión

Presente esquema relacional mínimo, consulta comentada, validación manual, salida
y figura. Discuta:

1. ¿Qué trabajo debe realizar SQL y cuál Python en este caso?
2. ¿Cómo podría un `JOIN` duplicar filas sin que el programa falle?
3. ¿Por qué cambia `localhost` dentro del contenedor?
4. ¿Qué persiste al eliminar un contenedor y por qué?
5. ¿Qué reproduce Docker y qué factores externos siguen sin controlar?

## 8. Qué se debe presentar

- informe PDF de 5–7 páginas según
  [`../plantilla_informe.md`](../plantilla_informe.md);
- `compose.yaml`, Dockerfile, SQL, código Python, pruebas y README;
- figura/tabla, salida de validación y diagrama de arquitectura;
- `.env.example` sin secretos y `AI_USAGE.md` completo;
- identificador de versión Git y evidencia individual.

No se acepta una entrega con credenciales versionadas. Una consulta que funciona
pero cuya granularidad no puede explicarse carece de validación científica.

## 9. Evidencia individual

Dibujar la arquitectura, anticipar una modificación de la consulta y explicar
oralmente variables de entorno, parámetros SQL, red y persistencia.
