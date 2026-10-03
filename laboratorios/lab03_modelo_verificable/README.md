# Laboratorio 3 — Biblioteca de integración verificable e instalable

| Campo | Especificación |
|---|---|
| Inicio | Jueves 15 de octubre de 2026 |
| Entrega | Martes 27 de octubre de 2026 |
| Dedicación por estudiante | 4–5 horas autónomas; incluye informe y video |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Python 3.12, biblioteca estándar, pytest y pip |

## Teoría breve

Una integral acumula contribuciones. En puntos medios se divide [a,b] en n
subintervalos iguales, se evalúa la función en cada centro y se suma su valor
por el ancho. El error de discretización se estudia comparando n, 2n y 4n con
una referencia conocida. Un resultado distinto de la referencia no implica por
sí solo un defecto del programa. Una biblioteca separa cálculo y presentación;
una distribución permite instalarla en otro entorno.

## Objetivos

- implementar el algoritmo de puntos medios practicado en clase;
- definir contratos y pruebas de resultados, límites y entradas inválidas;
- medir error absoluto/relativo y costo cualitativo al refinar;
- organizar una biblioteca propia y configurar pyproject.toml para instalación local;
- demostrar instalación normal y uso desde un entorno limpio externo al proyecto.

## Requerimientos y límites

- escribir solución y arquitectura propias, sin copiar el proyecto de apoyo;
- usar funciones y módulos, sin NumPy, SciPy, Pandas ni clases propias;
- seleccionar dos integrandos polinómicos sencillos con primitivas conocidas,
  uno distinto de x²; declarar límites y referencia analítica de cada uno;
- el algoritmo puede recibir una función como argumento solo si se explicó;
  también son válidas dos funciones específicas sin esa abstracción;
- preparar un nombre de distribución propio, README y versión;
- instalar localmente; construir un wheel es opcional y no suma requisitos; no exigir cuenta, publicación, token ni licencia
  pública como condición de aprobación;
- no usar Euler-Cromer ni estimación de periodos: el
  [péndulo anterior](extension_pendulo.md) es una extensión posterior.

## Procedimiento

1. Escriban el algoritmo y calculen a mano un caso con un subintervalo.
2. Definan contratos: número entero positivo de subintervalos, límites válidos
   y significado de las entradas/salidas. Las anotaciones no son validación.
3. Separen cálculo, experimento y presentación; no impriman desde el núcleo de cálculo.
4. Estudien al menos cuatro valores crecientes de n para ambos integrandos.
5. Calculen referencias, errores absolutos y relativos (cuando la referencia
   no sea cero), razones de error y número de iteraciones esperado.
6. Escriban al menos cinco pruebas pertinentes: caso manual, entrada inválida,
   caso límite, otro intervalo y una propiedad esperada. Usen tolerancias razonadas.
7. Configuren el proyecto instalable y prueben instalación editable durante desarrollo.
8. Instalen normalmente el proyecto local con `python -m pip install /ruta/al/proyecto` en un entorno limpio. Desde otra carpeta ejecuten un cliente que lo importe y registren la ruta del módulo. No se exige construir ni entregar wheel.
9. Registren instrucciones, versiones, pruebas, ruta del módulo importado y commit.

## Resultados puntuales

1. tabla de ambos integrandos con n, aproximación, referencia y errores;
2. explicación de costo y tendencia del error, sin atribuir todo a redondeo;
3. resultado visible de la suite y un defecto que una prueba detectaría;
4. código propio, pyproject.toml y README de la versión entregada;
5. evidencia de instalación limpia y llamada desde un cliente externo;
6. una limitación y un caso donde su implementación no debería utilizarse.

## Explicación escrita, video y evidencia individual

El informe justifica algoritmo, contratos, tolerancias, referencias y separación
de responsabilidades. El video de 3–5 min muestra una prueba, una tabla de error
y el uso de la biblioteca instalada; no publica nada. Cada estudiante traza un
paso de puntos medios, explica una prueba y distingue `pip install` de `import`.
La [rúbrica común](../README.md) conserva el peso del laboratorio.


## Entrega en GitHub

Deben **subir el código y el informe a GitHub**. Entregar URL del repositorio y commit evaluable. El README debe enlazar el informe Markdown o PDF e indicar comandos, dependencias y versiones para reproducirlo. Incluir datos permitidos o su fuente, resultados solicitados, evidencia de comprobaciones y enlace al video de 3–5 minutos. El informe responde las preguntas de esta guía, interpreta resultados y reconoce limitaciones; no es una colección de capturas. Cada integrante identifica su contribución. Si el repositorio es privado, habilitar los permisos de revisión antes de entregar.

Se aplica la [rúbrica común](../README.md). No subir `.venv`, cachés ni credenciales. Comprobar que código, informe y resultados son visibles en GitHub, no solo en el computador.


## Plan de trabajo y alcance

Apertura al cierre del 15 oct.; entrega el 27 oct.: doce días para distribuir 4–5 horas. Contratos y algoritmo: 60 min; pruebas y tablas: 90; instalación: 30–60; informe y video: 60–90. No programar trabajo obligatorio el día previo ni el día del parcial 2. La instalación se practica y consolida el 13 oct.

Usar cuatro refinamientos por integrando basta; no se exige interfaz gráfica, benchmark, publicación ni ecuaciones diferenciales. Si un error es cero, no dividir por él para obtener razones: registrarlo como no aplicable y explicarlo. IA nivel 1; evidencia individual nivel 0.

## Preguntas para el informe

1. ¿Por qué el punto medio se evalúa dentro de cada subintervalo y no en un extremo?
2. ¿Cómo cambian error y costo al duplicar n en cada integrando? ¿Qué no se puede concluir de cuatro valores?
3. ¿Qué detecta una prueba que la tabla de convergencia podría ocultar?
4. ¿Qué evidencia distingue una importación desde la fuente de una instalación normal?
