# Laboratorio 1 — Puesta a punto con WSL2, Bash, Git y GitHub

## 1. Identificación y sincronización

| Campo | Especificación |
|---|---|
| Realización | Jueves 3 de septiembre de 2026 |
| Cierre de prerrequisitos | Martes 1 de septiembre: Git/GitHub; el miércoles 2 es práctica |
| Duración presencial | 120 min |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Windows con WSL2/Ubuntu, Bash, Git, GitHub y editor de texto |
| IA | Nivel 1: consultar documentación; no generar la entrega |
| Archivos iniciales | [`comandos_basicos.sh`](comandos_basicos.sh) y [`PLANTILLA_CONFIGURACION_WSL2.md`](PLANTILLA_CONFIGURACION_WSL2.md) |

Esta actividad usa solamente navegación, flujos de texto, un script secuencial y
el ciclo básico de Git. **No requiere** variables de Bash, condicionales, ciclos,
funciones, ramas, conflictos ni automatización avanzada.

## 2. Pregunta de trabajo

¿Puede otra persona instalar o verificar el mismo entorno, ejecutar un script
sencillo y reconocer en Git/GitHub qué quedó registrado, usando únicamente la
documentación del equipo?

## 3. Objetivos

- explicar en Markdown cómo instalar y verificar WSL2 con Ubuntu;
- navegar y crear directorios con comandos básicos de Linux;
- distinguir salida estándar y salida de error;
- usar `grep`, `>`, `>>`, `2>`, `2>>` y una tubería;
- ejecutar un archivo `.sh` con `bash` y como archivo ejecutable;
- registrar cambios con Git y publicar un repositorio básico en GitHub.

## 4. Preparación antes de la sesión

La instalación puede exigir permisos de administrador y reinicio. Debe hacerse
antes del laboratorio o en la sesión de preparación del miércoles 2 de septiembre.

En PowerShell con permisos de administrador:

```powershell
wsl --install -d Ubuntu
```

Después del reinicio y de crear el usuario de Ubuntu, comprobar en PowerShell:

```powershell
wsl --status
wsl --list --verbose
```

La distribución debe aparecer con versión `2`. Si una instalación existente está
en versión 1, el docente explicará el cambio con `wsl --set-version`; el estudiante
no debe desregistrar ni borrar distribuciones.

Ya dentro de Ubuntu, ejecutar cada orden por separado:

```bash
sudo apt update
sudo apt install git
git --version
```

Documentación de referencia:

- [Instalación oficial de WSL](https://learn.microsoft.com/windows/wsl/install)
- [Trabajo entre sistemas de archivos en WSL](https://learn.microsoft.com/windows/wsl/filesystems)
- [Primeros pasos de Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git)

No incluya contraseñas, tokens, claves privadas ni capturas que los revelen.

## 5. Comandos incluidos

### Navegación y archivos

```bash
pwd
ls
ls -lah
mkdir practica_linux
mkdir -p practica_linux/resultados
cd practica_linux
```

### Búsqueda, tuberías y redirecciones

```bash
grep -n "sensor" datos/mediciones.txt
grep -n "sensor" datos/mediciones.txt | wc -l
ls -lah > resultados/listado.txt
ls -lah >> resultados/listado.txt
grep -n "sensor" datos/mediciones.txt 2> resultados/errores.log
grep -n "temperatura" datos/mediciones.txt 2>> resultados/errores.log
```

`>` reemplaza la salida; `>>` la anexa. El descriptor `2` representa la salida de
error: `2>` la reemplaza y `2>>` la anexa. La forma `>>2` **no** redirige errores;
en Bash se interpreta como anexar la salida estándar a un archivo llamado `2`.

### Ejecución del script

```bash
bash comandos_basicos.sh
chmod u+x comandos_basicos.sh
./comandos_basicos.sh
```

El estudiante debe poder explicar el *shebang*, el permiso de ejecución y la
diferencia entre las dos formas de ejecutar. No se evalúan condicionales ni ciclos.

### Git y GitHub básico

Configure una identidad académica sin copiar credenciales en el repositorio:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@example.com"
git init
git status
git add README.md CONFIGURACION_WSL2.md comandos_basicos.sh
git diff --staged
git commit -m "Documenta la puesta a punto de WSL2"
git log --oneline
```

Después de crear en GitHub un repositorio remoto vacío y seguir el mecanismo de
autenticación autorizado por la Universidad:

```bash
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git remote -v
git push -u origin main
```

No se requieren ramas adicionales, `merge`, resolución de conflictos ni
reescritura de historial.

## 6. Procedimiento

1. Copie la plantilla como `CONFIGURACION_WSL2.md` y complétela con explicaciones
   propias, comandos y salidas breves de verificación.
2. Cree `datos` y `resultados` con `mkdir`. Use el archivo de muestra suministrado
   en [`datos/mediciones.txt`](datos/mediciones.txt).
3. Ejecute manualmente cada comando del bloque de búsqueda y prediga antes si la
   salida aparecerá en pantalla o en un archivo.
4. Abra `comandos_basicos.sh`, lea cada línea y complete solo las dos líneas `TODO`
   usando un `grep` y una tubería. No agregue condicionales ni ciclos.
5. Ejecute el script primero con `bash` y luego mediante permiso de ejecución.
6. Compare el efecto de ejecutar dos veces sobre los archivos creados con `>` y
   `>>`; explique la diferencia en el README.
7. Inicialice Git y cree dos commits coherentes: documentación del entorno y
   script/resultados. Revise `git status` antes de cada commit.
8. Publique el repositorio en GitHub y verifique que no contiene credenciales ni
   archivos ajenos a la actividad.
9. Una pareja diferente sigue el README y marca cualquier paso que dependa de una
   explicación oral.

## 7. Entrega

No se exige informe PDF en este primer laboratorio. Se entrega la URL del
repositorio con:

```text
lab01_apellido1_apellido2/
├── README.md
├── CONFIGURACION_WSL2.md
├── comandos_basicos.sh
├── datos/
│   └── mediciones.txt
└── resultados/
    ├── listado.txt
    ├── coincidencias.txt
    ├── conteo.txt
    └── errores.log
```

El README explica cómo ejecutar el script, qué produce y qué diferencia existe
entre Git y GitHub. `CONFIGURACION_WSL2.md` explica instalación, verificación,
ubicación recomendada del proyecto y un problema encontrado con su solución.

## 8. Criterios particulares

- documentación de WSL2 comprensible y verificable: 20 puntos;
- navegación, estructura y ejecución del `.sh`: 15 puntos;
- `grep`, tubería y redirecciones correctas: 25 puntos;
- flujo Git y publicación en GitHub sin secretos: 20 puntos;
- reproducción por otra pareja y explicación: 15 puntos;
- evidencia individual: 5 puntos.

## 9. Evidencia individual

Sin equipo ni IA, cada estudiante:

1. predice dónde termina la salida de una orden con tubería, `>` y `2>>`;
2. interpreta un `git status` sencillo;
3. explica cómo comprobaría que Ubuntu está usando WSL2;
4. indica qué comando usaría para ejecutar un `.sh` que todavía no tiene permiso
   de ejecución.
