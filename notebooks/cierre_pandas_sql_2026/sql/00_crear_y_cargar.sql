-- Crea estructuras y catalogo; la API se carga con ampliacion/01_preparar.py.
-- Repetible en una base propia. No borra ni migra estructuras preexistentes.
BEGIN;
CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
CREATE TABLE IF NOT EXISTS silver.ciudades (
 ciudad_id TEXT PRIMARY KEY,
 nombre TEXT NOT NULL UNIQUE,
 latitud DOUBLE PRECISION NOT NULL CHECK (latitud BETWEEN -90 AND 90),
 longitud DOUBLE PRECISION NOT NULL CHECK (longitud BETWEEN -180 AND 180)
);
INSERT INTO silver.ciudades VALUES
 ('armenia','Armenia, Quindío',4.53656,-75.67263),
 ('bogota','Bogotá',4.60971,-74.08175),
 ('barranquilla','Barranquilla',10.96854,-74.78132)
ON CONFLICT (ciudad_id) DO NOTHING;
-- Bronze conserva la primera recepcion de cada ciudad/dia, sin imputar.
-- Simplificacion docente: no archiva todas las revisiones posteriores de la API.
CREATE TABLE IF NOT EXISTS bronze.observaciones (
 ciudad_id TEXT NOT NULL REFERENCES silver.ciudades(ciudad_id),
 fecha DATE NOT NULL,
 tmax_c DOUBLE PRECISION,
 tmin_c DOUBLE PRECISION,
 precipitacion_mm DOUBLE PRECISION,
 fuente_url TEXT NOT NULL,
 sha256 TEXT NOT NULL CHECK (length(sha256)=64),
 cargado_en TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (ciudad_id, fecha)
);
CREATE TABLE IF NOT EXISTS silver.observaciones (
 ciudad_id TEXT NOT NULL REFERENCES silver.ciudades(ciudad_id),
 fecha DATE NOT NULL,
 tmax_c DOUBLE PRECISION CHECK (tmax_c > '-Infinity'::float8 AND tmax_c < 'Infinity'::float8),
 tmin_c DOUBLE PRECISION CHECK (tmin_c > '-Infinity'::float8 AND tmin_c < 'Infinity'::float8),
 precipitacion_mm DOUBLE PRECISION CHECK (precipitacion_mm >= 0 AND precipitacion_mm < 'Infinity'::float8),
 PRIMARY KEY (ciudad_id, fecha),
 FOREIGN KEY (ciudad_id, fecha) REFERENCES bronze.observaciones(ciudad_id, fecha),
 CHECK (tmin_c <= tmax_c)
);
-- Cobertura respecto al mes completo, incluso dias aun no incorporados.
CREATE OR REPLACE VIEW gold.mensual AS
WITH grupos AS (
 SELECT ciudad_id, date_trunc('month',fecha)::date AS mes,
        COUNT(*) AS dias, COUNT(tmax_c) AS n_tmax, COUNT(tmin_c) AS n_tmin,
        COUNT(precipitacion_mm) AS n_precipitacion,
        AVG(tmax_c) AS tmax_media_c, AVG(tmin_c) AS tmin_media_c,
        SUM(precipitacion_mm) AS suma_disponible_mm
 FROM silver.observaciones GROUP BY ciudad_id, date_trunc('month',fecha)::date
), calendario AS (
 SELECT *, EXTRACT(DAY FROM mes + INTERVAL '1 month - 1 day')::integer AS dias_esperados
 FROM grupos
)
SELECT ciudad_id, mes, dias, dias_esperados, n_tmax, n_tmin, n_precipitacion,
       n_tmax::double precision/dias_esperados AS cobertura_tmax,
       n_tmin::double precision/dias_esperados AS cobertura_tmin,
       n_precipitacion::double precision/dias_esperados AS cobertura_precipitacion,
       tmax_media_c, tmin_media_c,
       CASE WHEN n_precipitacion=dias_esperados THEN suma_disponible_mm
            ELSE NULL END AS precipitacion_total_mm
FROM calendario;
COMMIT;
