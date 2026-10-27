-- Reconocer la conexión
SELECT version(), current_database(), current_user;

-- Control de carga
SELECT COUNT(*) AS registros, COUNT(masa_g) AS masas_presentes,
       COUNT(sexo) AS sexos_presentes
FROM curso_penguins.observaciones;

-- Adelie con masa de al menos 4000 g
SELECT registro_id, especie, isla, masa_g/1000.0 AS masa_kg
FROM curso_penguins.observaciones WHERE especie='Adelie' AND masa_g>=4000
ORDER BY masa_g DESC, registro_id LIMIT 8;

-- Localizar masas ausentes
SELECT registro_id, especie, isla FROM curso_penguins.observaciones
WHERE masa_g IS NULL ORDER BY registro_id;

-- Resumen de masas por especie
SELECT especie, COUNT(*) AS registros, COUNT(masa_g) AS masas_presentes,
       AVG(masa_g) AS masa_media_g, STDDEV_SAMP(masa_g) AS dispersion_g
FROM curso_penguins.observaciones GROUP BY especie ORDER BY especie;

-- Especie y año con al menos 40 masas
SELECT especie, anio, COUNT(masa_g) AS n, AVG(masa_g) AS media_g
FROM curso_penguins.observaciones GROUP BY especie, anio
HAVING COUNT(masa_g)>=40 ORDER BY especie, anio;

-- Filtrar individuos antes de agrupar
SELECT especie, COUNT(*) AS n, AVG(masa_g) AS media_g
FROM curso_penguins.observaciones WHERE masa_g>4000 GROUP BY especie ORDER BY especie;

-- Filtrar especies después de agrupar
SELECT especie, COUNT(masa_g) AS n, AVG(masa_g) AS media_g
FROM curso_penguins.observaciones GROUP BY especie HAVING AVG(masa_g)>4000 ORDER BY especie;

-- Conservar todas las especies
SELECT e.especie, COUNT(o.registro_id) AS mayores_5000g
FROM curso_penguins.especies AS e LEFT JOIN curso_penguins.observaciones AS o
ON e.especie=o.especie AND o.masa_g>5000
GROUP BY e.especie ORDER BY e.especie;

-- Cambiar la pregunta con WHERE
SELECT e.especie, COUNT(o.registro_id) AS mayores_5000g
FROM curso_penguins.especies AS e LEFT JOIN curso_penguins.observaciones AS o ON e.especie=o.especie
WHERE o.masa_g>5000 GROUP BY e.especie ORDER BY e.especie;

-- Comprobar que el catálogo no multiplica registros
SELECT COUNT(*) AS filas_unidas
FROM curso_penguins.observaciones AS o JOIN curso_penguins.especies AS e ON o.especie=e.especie;

-- Ensayar y revertir un cambio
BEGIN;
CREATE TEMP TABLE ensayo_curso (id INTEGER PRIMARY KEY, nota TEXT);
INSERT INTO ensayo_curso VALUES (1, 'prueba reversible');
SELECT * FROM ensayo_curso;
ROLLBACK;

-- Incorporar una media de grupo
WITH medias AS (
 SELECT especie, AVG(masa_g) AS media_especie_g FROM curso_penguins.observaciones GROUP BY especie
)
SELECT o.registro_id, o.especie, o.masa_g, m.media_especie_g,
       o.masa_g-m.media_especie_g AS desviacion_media_g
FROM curso_penguins.observaciones AS o JOIN medias AS m ON o.especie=m.especie
ORDER BY o.registro_id;
