-- Consultas docentes; ejecutar con psql -X -v ON_ERROR_STOP=1 -f ...
SELECT version(), current_database(), current_user;
SELECT ciudad_id, fecha, tmax_c, tmax_c+273.15 AS tmax_k
FROM silver.observaciones WHERE ciudad_id='armenia' AND tmax_c>=24
ORDER BY tmax_c DESC, fecha LIMIT 8;
SELECT ciudad_id, fecha FROM silver.observaciones
WHERE tmax_c IS NULL ORDER BY ciudad_id, fecha;
SELECT ciudad_id, fecha FROM silver.observaciones
WHERE ciudad_id IN ('armenia','bogota') AND (precipitacion_mm>10 OR tmin_c<10)
ORDER BY ciudad_id, fecha;
SELECT ciudad_id, COUNT(*) AS dias, COUNT(tmax_c) AS disponibles,
       AVG(tmax_c) AS media_c, STDDEV_SAMP(tmax_c) AS dispersion_c,
       MIN(tmin_c) AS minima_c, MAX(tmax_c) AS maxima_c,
       SUM(precipitacion_mm) AS lluvia_disponible_mm
FROM silver.observaciones GROUP BY ciudad_id ORDER BY ciudad_id;
SELECT ciudad_id, COUNT(tmax_c) AS n, AVG(tmax_c) AS media_c
FROM silver.observaciones GROUP BY ciudad_id
HAVING COUNT(tmax_c)>=30 ORDER BY ciudad_id;
SELECT ciudad_id, COUNT(*) AS n, AVG(tmax_c) AS media_c
FROM silver.observaciones WHERE tmax_c>24 GROUP BY ciudad_id ORDER BY ciudad_id;
SELECT ciudad_id, COUNT(tmax_c) AS n, AVG(tmax_c) AS media_c
FROM silver.observaciones GROUP BY ciudad_id HAVING AVG(tmax_c)>24 ORDER BY ciudad_id;
SELECT c.ciudad_id, COUNT(o.fecha) AS dias_muy_lluviosos
FROM silver.ciudades AS c LEFT JOIN silver.observaciones AS o
ON c.ciudad_id=o.ciudad_id AND o.precipitacion_mm>50
GROUP BY c.ciudad_id ORDER BY c.ciudad_id;
-- Al mover el filtro a WHERE se pierden ciudades sin coincidencias:
SELECT c.ciudad_id, COUNT(o.fecha) AS dias_muy_lluviosos
FROM silver.ciudades AS c LEFT JOIN silver.observaciones AS o ON c.ciudad_id=o.ciudad_id
WHERE o.precipitacion_mm>50 GROUP BY c.ciudad_id ORDER BY c.ciudad_id;
SELECT COUNT(*) AS filas_unidas
FROM silver.observaciones AS o INNER JOIN silver.ciudades AS c ON o.ciudad_id=c.ciudad_id;
BEGIN;
CREATE TEMP TABLE ensayo_curso (id INTEGER PRIMARY KEY, medida DOUBLE PRECISION CHECK(medida>=0));
INSERT INTO ensayo_curso VALUES (1, 2.5); -- dato artificial, solo en tabla temporal
SELECT * FROM ensayo_curso;
ROLLBACK;
WITH medias AS (
 SELECT ciudad_id, AVG(tmax_c) AS media_ciudad_c FROM silver.observaciones GROUP BY ciudad_id
)
SELECT o.ciudad_id, o.fecha, o.tmax_c, m.media_ciudad_c,
       o.tmax_c-m.media_ciudad_c AS desviacion_media_c
FROM silver.observaciones AS o JOIN medias AS m ON o.ciudad_id=m.ciudad_id
ORDER BY o.ciudad_id, o.fecha;
SELECT * FROM gold.mensual ORDER BY ciudad_id,mes;
-- Debe devolver cero filas tanto antes como despues de actualizar:
SELECT ciudad_id,fecha,COUNT(*) FROM silver.observaciones
GROUP BY ciudad_id,fecha HAVING COUNT(*)>1;
SELECT 'bronze' AS etapa,COUNT(*) FROM bronze.observaciones
UNION ALL SELECT 'silver',COUNT(*) FROM silver.observaciones;
