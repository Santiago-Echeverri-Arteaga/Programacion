-- Preguntas sugeridas para practicar en papel:
-- 1. Anticipe las columnas y la granularidad del resultado.
-- 2. Explique qué filas se excluyen y por qué.
-- 3. Identifique un índice potencial y justifique si sería útil.

SELECT e.nombre, COUNT(m.id) AS n, AVG(m.valor) AS media
FROM experimentos AS e
LEFT JOIN sensores AS s
  ON s.experimento_id = e.id
LEFT JOIN mediciones AS m
  ON m.sensor_id = s.id
 AND m.calidad = 'valida'
GROUP BY e.id, e.nombre
HAVING COUNT(m.id) >= 2
ORDER BY media DESC NULLS LAST;
