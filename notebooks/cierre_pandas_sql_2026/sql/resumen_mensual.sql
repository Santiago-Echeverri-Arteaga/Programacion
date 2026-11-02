SELECT c.nombre, m.* FROM gold.mensual AS m
JOIN silver.ciudades AS c USING (ciudad_id)
ORDER BY ciudad_id, mes;
