-- S1 · Filtrar y ordenar
-- Obtén los cinco registros Chinstrap con mayor longitud de aleta. Muestra identificador, isla, aleta y masa; resuelve empates por identificador ascendente. Excluye aletas ausentes explícitamente.

-- S2 · NULL y conteos
-- Por especie, informa filas totales, masas válidas y masas ausentes. Formula las ausencias como diferencia entre dos conteos. Explica por qué masa_g = NULL no responde la pregunta.

-- S3 · WHERE y HAVING
-- Entre registros con masa observada, resume por isla y conserva grupos cuya masa media supere 4000 g. Explica cómo cambiaría el significado si filtras cada registro por masa mayor que 4000 antes de agrupar.

-- S4 · Conservar categorías
-- Usa el catálogo especies para contar registros con masa de al menos 6000 g por especie, incluidas las especies sin tales registros. Decide dónde ubicar el filtro y qué columna contar.

-- S5 · Transacción y restricciones
-- En una sola ejecución, abre una transacción, crea una tabla temporal ensayo_practica con id como clave primaria y medida positiva, inserta una fila válida, consúltala y revierte. Explica qué rechazarían las restricciones y por qué la tabla no queda disponible después del rollback. No cambies las observaciones originales.
