SELECT isla, COUNT(masa_g) AS n, AVG(masa_g) AS media_g
FROM curso_penguins.observaciones GROUP BY isla ORDER BY isla;
