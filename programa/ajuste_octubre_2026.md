# Diagnóstico y fundamento del ajuste — 2 de octubre de 2026

## Evidencia revisada

Se actualizó el repositorio por fast-forward a `8ed5859` y se comparó la planeación del 30 de septiembre con la carpeta local `2026-2/` y el reporte docente. La carpeta es evidencia de trabajo en clase, no una biblioteca de referencia validada; se conserva sin corregir sus originales.

| Evidencia | Qué permite continuar | Qué conviene comprobar |
|---|---|---|
| `funciones_contrato.py` | Funciones, listas, copia, `zip`, `*args` | Valida el intervalo después de dividir: usar el caso cero para discutir orden de validación. Un comentario sobre causalidad no justifica restringir x₀ a 50 m. |
| Reporte docente de cierre de colecciones y args/kwargs | Reanudar sin repetir todo Python básico | Una función corta que distinga argumentos posicionales y nombrados; no se exige usarlos artificialmente en laboratorios. |
| `importar_datos.py` | Path, ruta desde `__file__`, `with`, CSV, conversiones y errores de fila | El docstring dice tiempo_m pero el encabezado usa tiempo_s; comprobar unidades, archivo vacío, tiempo repetido y valores no finitos antes del análisis. |
| `biblioteca/Libreria/cinematica/codigo.py` | Módulos, contratos y `integrar_cuadrado` por puntos medios | `primos(1)` y n no entero son casos de discusión; separar `print` y cálculo. No asumir pruebas automatizadas dominadas. |
| `ejemplo.py` e inicializadores | `sys.path`, `__file__`, importaciones relativas y reexportación | Contrastar con instalación local; explicar `import *` antes de sustituirlo por nombres explícitos. |
| `recursividad.py`, `condicionales.py` y scripts iniciales | Casos base, flujo y entrada/salida | Recursión no agrega requisitos de laboratorio; entradas negativas son casos de revisión. En `edad.py`, reemplazar `eval(input(...))` por conversión explícita en una copia didáctica; `script.sh` requiere revisar activación del entorno. |
| Guías 03–05 y proyecto de biblioteca del repositorio | Continuidad de archivos → pruebas → error numérico | El ejemplo terminado no acredita que se haya trabajado completo. |

El 24 sep. estaba planeado para archivos, pero el docente reporta cierre de colecciones y funciones. La semana 29 sep.–1 oct. se registra por avance conjunto: lectura e importaciones, no pytest ni empaquetado acreditados.

## Por qué este orden

La sesión 2 se mantiene el 6 oct. El miércoles 7 se dedica a un compendio individual autogestionado de nueve ejercicios en dos horas: análisis y corrección de ciclos, colecciones, recursividad, argumentos, paquetes, archivos, puntos medios y entorno/Git ya trabajados; no depende de pytest ni empaquetado. La sesión 3 de error pasa al 13 oct. (75 min), seguida de instalación local (25 min), pregunta del proyecto (10 min) y cierre (10 min). Wheel y publicación siguen como extensión. El laboratorio del 8 exige Python y archivos ya trabajados; pytest puede usarse tras la sesión 2, sin convertirse en barrera de entrada.

Los cinco pendientes son labs. 2–6, con progresión: archivo validado → algoritmo verificable → arreglos y figura → datos imperfectos → auditoría reproducible. El lab. 3 tiene doce días y alcance acotado; el lab. 6 reutiliza evidencia previa con una comprobación nueva. Así no compite con el proyecto como una segunda investigación.

Se mantienen resultados del curso: escribir, depurar y explicar Python; resolver una pregunta física; contrastar resultados; procesar datos; comunicar con Git y reproducibilidad. Los temas avanzados siguen disponibles sin convertir su lectura autónoma en requisito de aprobación.

El 21 oct. y el 12 nov. se reservan para exámenes. La nueva entrega de proyecto del 16 nov. es una decisión de este rediseño, no una fecha institucional suministrada por el docente. Las exposiciones conservan el 17–19. Pesos y registro histórico del lab. 1 no cambian.


## Revisión de cobertura del taller del 7 de octubre

La versión de ejercicios básicos no representaba suficientemente el avance: omitía recursividad, `while`, `for…else`, búsqueda de importaciones y el algoritmo de puntos medios presente en los códigos. La versión vigente mantiene nueve problemas independientes, pero exige razonar sobre contratos y efectos del código, detectar casos que una comprobación normal no revela y reparar algoritmos. No contiene instrucciones de administración del tiempo.

| Evidencia de clase | Cobertura en el taller |
|---|---|
| `edad.py`, `condicionales.py` y calculadora de `codigo.py` | Ej. 1: entrada, tipos, conversión, `while`, condiciones, contador, `break` y excepciones |
| `funciones_contrato.py` y reporte de colecciones | Ej. 2: listas, tuplas, diccionarios, copia, alias y estado compartido |
| `primos` en `codigo.py` | Ej. 3: rango, módulo, búsqueda, `break`, `for…else` y casos límite |
| `recursividad.py` | Ej. 4: Euclides, factorial, caso base, progreso y retorno de llamadas |
| `funciones_contrato.py` y reporte docente sobre kwargs | Ej. 5: `*args`, `**kwargs`, desempaquetado, `zip`, contratos y validación |
| `ejemplo.py` y los dos `__init__.py` | Ej. 6: paquetes, importaciones relativas, reexportación, `sys.path`, `__file__`, `__name__` y `Path` |
| `importar_datos.py` | Ej. 7: `with`, encabezado, cadenas, conversión, enumeración, excepciones específicas y datos omitidos |
| `integrar_cuadrado` en `codigo.py` | Ej. 8: descomposición, centro del intervalo, acumulación y contraste manual |
| `script.sh`, `demo.py` y bloque inicial de Git | Ej. 9: entorno, Bash, archivos, área de preparación, commits y remoto |

La presencia de ejemplos en la carpeta es evidencia de contenido trabajado, no de dominio individual. El taller muestrea cada bloque; no requiere reproducir todas las variantes (Fibonacci y Hanoi quedan representados por los conceptos recursivos de factorial y Euclides). Los tipos, operadores, funciones y contratos reaparecen en varios ejercicios. No introduce pruebas automatizadas ni error/convergencia formal antes de su sesión; reconocer el algoritmo de puntos medios ya visto no equivale a adelantar ese contenido nuevo. Tampoco añade recursividad como requisito de los laboratorios.
