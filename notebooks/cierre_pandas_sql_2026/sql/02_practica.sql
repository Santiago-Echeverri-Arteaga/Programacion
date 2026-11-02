-- S1 · Filtrar y ordenar
-- Obtén los cinco días de Armenia con mayor precipitación; muestra fecha, precipitación y máxima. Excluye ausentes y resuelve empates por fecha. Reproduce en Pandas para el mismo periodo y compara.
-- Escribe aqui tu consulta.

-- S2 · NULL, claves y conteos
-- Por ciudad informa filas, máximas presentes y ausentes mediante dos conteos. Explica por qué tmax_c = NULL no funciona. Justifica la clave primaria compuesta: ¿por qué no basta ciudad o fecha? Consulta claves repetidas y explica qué esperas antes de ejecutar.
-- Escribe aqui tu consulta.

-- S3 · WHERE y HAVING
-- Resume por ciudad entre máximas presentes y conserva grupos con media superior a 24 °C. Explica la diferencia con filtrar días superiores a 24 antes de agrupar. Escribe una pregunta en lenguaje natural para cada consulta.
-- Escribe aqui tu consulta.

-- S4 · Conservar categorías
-- Cuenta días de precipitación >=50 mm por ciudad, incluidas ciudades con cero casos. Decide INNER o LEFT JOIN, dónde poner el filtro y qué columna contar. Explica cómo una unión de dos tablas diarias solo por ciudad multiplicaría resultados.
-- Escribe aqui tu consulta.

-- S5 · Transacción y restricciones
-- En una transacción crea una tabla temporal ensayo_practica con clave primaria y una medida no negativa, inserta una fila artificial válida, consulta y revierte. Explica qué rechaza cada restricción, cómo trata NULL un CHECK y por qué la tabla desaparece tras ROLLBACK. No cambies los datos reales.
-- Escribe aqui tu consulta.

-- S6 · Pipeline y actualización
-- En una base de pruebas nueva ejecuta inicial y consulta Gold. Predice conteos, ejecuta actualización y vuelve a consultar Gold. Repite actualización y comprueba que se conservan filas previas sin duplicados. Explica por qué DO NOTHING no corrige valores ya guardados. Si ya actualizaste tu base, pide una base nueva; no borres datos para reiniciarla.
-- Escribe aqui tu consulta.

-- S7 · Cambiar una consulta
-- En una copia de sql/resumen_mensual.sql agrega un filtro para devolver solo una ciudad. Usa esa copia en una copia del pipeline y adapta el informe si cambias columnas. Verifica qué recibe Python y cuándo aparece COMPLETADO.txt. Ensaya un error de consulta en la copia: ¿hay carpeta parcial?, ¿qué cambios de base permanecen?
-- Escribe aqui tu consulta.

-- S8 · Localizar cálculo y memoria
-- Dibuja PostgreSQL remoto de 500 GB y Python local. Compara SELECT *, WHERE y GROUP BY; marca qué cruza la red y qué queda almacenado. Explica por qué 100 filas de resumen no necesitan 500 GB de RAM. Propón una operación por lotes y otra que necesite estado entre lotes. Distingue Python remoto de procesamiento distribuido.
-- Escribe aqui tu consulta.
