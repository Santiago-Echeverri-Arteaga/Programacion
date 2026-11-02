-- Se ejecuta dentro de la MISMA transaccion que la ingesta Bronze.
-- Las restricciones Silver rechazan el lote si hay valores invalidos.
INSERT INTO silver.observaciones
 (ciudad_id, fecha, tmax_c, tmin_c, precipitacion_mm)
SELECT ciudad_id, fecha, tmax_c, tmin_c, precipitacion_mm
FROM bronze.observaciones
ON CONFLICT (ciudad_id, fecha) DO NOTHING;
