-- Ejecutar después de infraestructura/postgresql/init/01_esquema.sql y 02_datos.sql.

SELECT s.experimento_id, COUNT(*) AS cantidad,
       AVG(m.valor) AS media, STDDEV_SAMP(m.valor) AS desviacion
FROM mediciones AS m
JOIN sensores AS s ON s.id = m.sensor_id
GROUP BY s.experimento_id
ORDER BY s.experimento_id;

SELECT e.nombre, m.instante, m.valor, s.unidad
FROM experimentos AS e
JOIN sensores AS s ON s.experimento_id = e.id
JOIN mediciones AS m ON m.sensor_id = s.id
WHERE m.calidad = 'valida'
ORDER BY e.nombre, m.instante;

EXPLAIN
SELECT * FROM mediciones WHERE sensor_id = 1;
