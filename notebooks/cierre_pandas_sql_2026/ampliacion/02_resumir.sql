-- Ejecutado por psql desde el directorio de esta ejecución del pipeline.
-- La tabla es temporal: no sobrescribe las tablas de clase ni deja una carga parcial.
BEGIN;
CREATE TEMP TABLE mediciones_pipeline (
 registro_id INTEGER PRIMARY KEY,
 especie TEXT NOT NULL,
 isla TEXT NOT NULL,
 anio INTEGER NOT NULL,
 masa_g DOUBLE PRECISION CHECK(masa_g>0),
 aleta_mm DOUBLE PRECISION CHECK(aleta_mm>0)
) ON COMMIT DROP;
\copy mediciones_pipeline FROM 'datos.csv' WITH (FORMAT CSV, HEADER true, NULL '')
-- COPY devuelve resultados al cliente; \copy escribe en el equipo que ejecuta psql.
-- Cada metaorden \copy debe ocupar una sola línea.
\copy (SELECT isla, COUNT(*) AS total, COUNT(masa_g) AS masas_presentes, AVG(masa_g) AS masa_media_g, STDDEV_SAMP(masa_g) AS masa_sd_g, 100.0*COUNT(masa_g)/COUNT(*) AS cobertura_pct FROM mediciones_pipeline GROUP BY isla ORDER BY isla) TO 'resumen.csv' WITH (FORMAT CSV, HEADER true)
COMMIT;
