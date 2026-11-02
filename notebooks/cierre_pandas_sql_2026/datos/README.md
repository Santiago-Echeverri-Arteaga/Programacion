# Datos del observatorio: procedencia y contrato científico

La muestra contiene **180 registros reales de reanálisis**, no mediciones de estaciones municipales. Se descargó desde Open-Meteo y se conservaron los bytes de seis respuestas en `originales/`; cada fecha de descarga UTC, URL y SHA-256 está en `procedencia.json`. `meteorologia.csv` es la unión sin duplicados, con nombres de columnas traducidos y sin imputación. Las repeticiones entre respuestas se usan para enseñar actualizaciones.

## Producto y consulta verificados

Se revisó la [documentación histórica oficial](https://open-meteo.com/en/docs/historical-weather-api) el 2 de noviembre de 2026. Se seleccionó **ERA5**, evitando Best Match. ERA5-Land se consideró, pero la matriz de variables no ofrece precipitación independiente de ERA5; preferimos el producto que proporciona las tres variables de manera consistente.

Endpoint: `https://archive-api.open-meteo.com/v1/archive`. Parámetros explícitos: `models=era5`, `daily=temperature_2m_max,temperature_2m_min,precipitation_sum`, `timezone=America/Bogota`, `temperature_unit=celsius`, `precipitation_unit=mm`, `timeformat=iso8601`, `cell_selection=land`, coordenadas y fechas. Máximas/mínimas se expresan en °C a 2 m; precipitación diaria en mm. Son agregados de 24 horas de datos horarios. La documentación indica cobertura ERA5 desde 1940, rejilla de 0,25° y actualización diaria con cinco días de retraso. Las fechas cerradas de 2024 evitan depender de esa latencia.

| Etapa | Periodo inclusivo por ciudad | Recibidas | Nuevas respecto a inicial |
|---|---|---:|---:|
| Inicial | 2024-01-01 a 2024-01-31 | 93 | 93 |
| Actualización | 2024-01-25 a 2024-02-29 | 108 | 87 |
| Unión | 2024-01-01 a 2024-02-29 | 180 únicas | — |

La documentación no establece aquí un umbral universal de completitud intradiaria que debamos inventar. El programa conserva los `null` recibidos como `None`/SQL NULL, nunca como cero. Comprueba longitudes, secuencia diaria, unidades y zona; rechaza respuestas mal formadas. En esta copia las tres variables están completas. Tener todos los días publicados no demuestra que cada valor sea exacto ni permite auditar por sí solo todas las horas originales.

## Coordenadas verificadas

Se utilizó la [API de geocodificación de Open-Meteo](https://open-meteo.com/en/docs/geocoding-api), basada en GeoNames, filtrando Colombia y eligiendo los identificadores indicados, no simplemente el primer homónimo. El manifiesto conserva las consultas y registros seleccionados.

| Identificador | Ciudad | GeoNames | Latitud WGS84 | Longitud WGS84 |
|---|---|---:|---:|---:|
| armenia | Armenia, Quindío | 3689560 | 4.53656 | -75.67263 |
| bogota | Bogotá | 3688689 | 4.60971 | -74.08175 |
| barranquilla | Barranquilla | 3689147 | 10.96854 | -74.78132 |

Son coordenadas solicitadas, no ubicaciones de instrumentos. Las coordenadas de rejilla y elevación devueltas están en cada JSON; la API aplica sus reglas de selección de celda y ajuste por elevación. No se presupone resolución de barrio ni atribución causal de diferencias a una sola característica urbana.

## Uso y atribución

**Fuente:** Open-Meteo; ERA5, Copernicus Climate Change Service (C3S), ECMWF. Datos bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Las derivaciones de este módulo renombraron campos, unieron fechas y calcularon resúmenes; no alteraron las cifras originales ni imputaron ausencias. La información de ubicación procede de GeoNames vía Open-Meteo.

Según las [condiciones oficiales](https://open-meteo.com/en/terms), la API gratuita se destina a uso no comercial, incluido educativo; límites publicados: menos de 600 llamadas/minuto, 5000/hora y 10 000/día, con 300 000/mes en la tabla de planes. El servicio no garantiza disponibilidad o exactitud. No automatizar descargas masivas del curso: cada fase usa tres solicitudes y la copia offline evita repetirlas en cada computador. Uso comercial o necesidades distintas requieren revisar el plan correspondiente. Condiciones y disponibilidad pueden cambiar; revisarlas antes de reutilizar fuera de este curso.

## Reproducibilidad y límites

Online consulta las mismas URLs, pero una revisión de la fuente podría cambiar resultados o hashes (incluso metadatos de tiempo de generación cambian). Offline verifica bytes congelados. Bronze guarda primera recepción por clave ciudad–fecha; no es un historial de revisiones API. Corregir un registro requiere un procedimiento distinto, explícito y documentado.

Gold usa cobertura sobre todos los días del mes y solo publica precipitación acumulada con 100%. Las medias térmicas llevan coberturas y no equivalen a temperatura media diaria. No se infieren tendencias climáticas de dos meses ni incertidumbre a partir del promedio. Una revisión de la licencia o del producto exige conservar atribución y registrar cambios en esta documentación.
