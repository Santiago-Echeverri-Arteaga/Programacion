-- Clase de PostgreSQL puro.
-- Las líneas que empiezan por barra invertida son comandos de psql, no SQL.

\dt
\d mediciones

-- 1. Seleccionar columnas y ordenar.
SELECT instante, valor, incertidumbre
FROM mediciones
WHERE sensor_id = 1
ORDER BY instante;

-- 2. Combinar tablas relacionadas.
SELECT
    e.nombre AS experimento,
    s.nombre AS sensor,
    s.magnitud,
    m.instante,
    m.valor,
    s.unidad,
    m.calidad
FROM mediciones AS m
JOIN sensores AS s ON s.id = m.sensor_id
JOIN experimentos AS e ON e.id = s.experimento_id
ORDER BY e.nombre, s.nombre, m.instante;

-- 3. Resumir grupos, excluyendo valores descartados.
SELECT
    s.nombre AS sensor,
    count(*) AS n,
    avg(m.valor) AS promedio,
    stddev_samp(m.valor) AS desviacion
FROM mediciones AS m
JOIN sensores AS s ON s.id = m.sensor_id
WHERE m.calidad <> 'descartada'
GROUP BY s.id, s.nombre
ORDER BY sensor;

-- 4. Filtrar después de agregar.
SELECT
    s.nombre AS sensor,
    avg(m.valor) AS promedio
FROM mediciones AS m
JOIN sensores AS s ON s.id = m.sensor_id
GROUP BY s.id, s.nombre
HAVING count(*) >= 4;

-- 5. Parámetro respecto a la primera medición de cada sensor.
WITH serie AS (
    SELECT
        sensor_id,
        instante,
        valor,
        first_value(valor) OVER (
            PARTITION BY sensor_id ORDER BY instante
        ) AS valor_inicial
    FROM mediciones
)
SELECT sensor_id, instante, valor, valor / valor_inicial AS fraccion_inicial
FROM serie
ORDER BY sensor_id, instante;

-- Preguntas para discutir:
-- a. ¿Por qué la incertidumbre no debe almacenarse como texto?
-- b. ¿Qué diferencia hay entre WHERE y HAVING?
-- c. ¿Qué evita la clave foránea sensor_id?
-- d. ¿Qué datos deberían llevar además información de procedencia?
-- e. ¿Cuándo sería incorrecto promediar mediciones de sensores diferentes?

