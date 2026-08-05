# Programación científica con Python para Física

Curso de Programación del programa de Física de la Universidad del Quindío.

Este repositorio reúne las guías, ejemplos, notebooks, datos y laboratorios que se
utilizan en clase. El curso prioriza la capacidad de leer, escribir, depurar,
probar y explicar código, además de aplicar la programación a modelos y datos
físicos de forma reproducible.

## Organización

- [`programa/`](programa/README.md): resultados de aprendizaje, cronograma,
  evaluación, política de IA y proyecto final.
- [`clases/`](clases/README.md): 48 encuentros preparados, cada uno con guion y
  archivos de trabajo.
- [`guias/`](guias/README.md): guías de clase y material de apoyo.
- [`Codigos/`](Codigos/README.md): ejemplos desarrollados, organizados por tema.
- [`notebooks/`](notebooks/README.md): notebooks de trabajo guiado.
- [`datos/`](datos/README.md): conjuntos de datos pequeños con procedencia.
- [`laboratorios/`](laboratorios/README.md): enunciados y archivos iniciales.
- [`proyecto_final/`](proyecto_final/README.md): instrucciones y plantillas.
- [`infraestructura/`](infraestructura/README.md): PostgreSQL y Docker.
- [`recursos/`](recursos/README.md): referencias y enlaces de apoyo.

Cada carpeta importante contiene un `README.md` que explica su propósito, sus
archivos y la forma de uso. El material histórico que no pertenece a la nueva
ruta pública se conserva de forma recuperable en el archivo docente ignorado por
Git.

## Preparación del entorno

Python 3.12 es la versión de referencia del curso. Se requieren además Git y una
terminal Linux; para los módulos finales, Docker. Usar una versión posterior de
Python exige verificar previamente todas las dependencias.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En Windows PowerShell, la activación equivalente es:

```powershell
.venv\Scripts\Activate.ps1
```

Las instrucciones completas se desarrollarán en las guías de instalación y de
Linux/Bash.

## Uso de inteligencia artificial

La IA generativa no está permitida en parciales, pruebas escritas, ejercicios de
salida ni actividades que se identifiquen como evaluación individual protegida.
En actividades abiertas solo puede usarse cuando la guía lo autorice y siempre
debe declararse. Consulte [`programa/politica_ia.md`](programa/politica_ia.md).

## Material docente privado

Las soluciones, bancos de preguntas, claves de calificación y notas de clase se
mantienen en `_docente_privado/`, excluido de este repositorio público mediante
`.gitignore`.
