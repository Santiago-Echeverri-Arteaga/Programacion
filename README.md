# Programación científica con Python para Física

Curso de Programación del programa de Física de la Universidad del Quindío.

Este repositorio reúne las guías, ejemplos, notebooks, datos y laboratorios que se
utilizan en clase. El curso prioriza la capacidad de leer, escribir, depurar,
probar y explicar código, además de aplicar la programación a modelos y datos
físicos de forma reproducible.

## Organización

- [`programa/`](programa/README.md): resultados de aprendizaje, cronograma,
  evaluación, política de IA y proyecto final.
- [`guias/`](guias/README.md): guías de clase y material de apoyo.
- [`ejemplos/`](ejemplos/README.md): programas breves usados en demostraciones.
- [`notebooks/`](notebooks/README.md): notebooks de trabajo guiado.
- [`datos/`](datos/README.md): conjuntos de datos pequeños con procedencia.
- [`laboratorios/`](laboratorios/README.md): enunciados y archivos iniciales.
- [`proyecto_final/`](proyecto_final/README.md): instrucciones y plantillas.
- [`infraestructura/`](infraestructura/README.md): PostgreSQL y Docker.
- [`recursos/`](recursos/README.md): referencias y enlaces de apoyo.

El directorio histórico `Codigos/` se conserva temporalmente mientras sus
materiales se revisan, migran o descartan. No hace parte de la ruta oficial del
curso nuevo.

## Preparación del entorno

Se requiere Python 3.12 o posterior, Git y una terminal Linux. Para los módulos
finales se requiere Docker.

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
