# Guía 15 — Docker y reproducibilidad desde cero

## Ficha

- Realización: segunda parte del miércoles 4 y práctica del jueves 5 de noviembre
  de 2026.
- Duración: 60 minutos de conceptos y hasta 120 minutos de práctica guiada.
- Nivel de IA: 1.
- Resultados: RA 1 y RA 10.
- Archivos: `infraestructura/compose.yaml` y `infraestructura/docker/`.

## Resultados

El estudiante podrá:

1. diferenciar imagen, contenedor, volumen, red y registro;
2. explicar qué comparte un contenedor con el sistema anfitrión;
3. ejecutar e inspeccionar un contenedor;
4. construir una imagen a partir de un Dockerfile;
5. usar Compose para conectar una aplicación con PostgreSQL;
6. reconocer qué problemas de reproducibilidad Docker resuelve y cuáles no.

## Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–15 | Comparar proceso, entorno virtual, máquina virtual y contenedor |
| 15–35 | Inspeccionar el contenedor PostgreSQL: `ps`, `logs`, `exec`, puertos |
| 35–50 | Observar capas e instrucciones del Dockerfile |
| 50–65 | Construir la imagen de análisis |
| 65–75 | Pausa y resolución de fallas de descarga |
| 75–95 | Ejecutar aplicación y base en la red de Compose |
| 95–108 | Volumen persistente, variables y reinicio |
| 108–120 | Salida individual y mapa de responsabilidades |

## Comandos

```bash
docker version
docker image ls
docker container ls --all
docker-compose up -d db
docker-compose logs db
docker-compose exec db sh
docker-compose build analisis
docker-compose --profile demo run --rm analisis
docker-compose down
```

## Lectura del Dockerfile

Cada instrucción debe responder una pregunta:

- `FROM`: ¿qué sistema y runtime se heredan?
- `WORKDIR`: ¿desde dónde se ejecuta el programa?
- `COPY`: ¿qué archivos entran en la imagen?
- `RUN`: ¿qué se calcula al construir?
- `ENV`: ¿qué comportamiento se configura?
- `CMD`: ¿qué ocurre al iniciar el contenedor?

## Conceptos que no deben confundirse

- Una imagen es una plantilla; un contenedor es una ejecución.
- Borrar un contenedor no equivale necesariamente a borrar un volumen.
- `localhost` dentro de un contenedor se refiere a ese contenedor.
- Publicar un puerto no es necesario para la comunicación interna entre servicios.
- Una contraseña en una variable sigue siendo un secreto que debe protegerse.
- Docker fija parte del entorno, pero no demuestra que el algoritmo sea correcto.

## Plan de contingencia

Si la sala no puede descargar imágenes, el docente usa imágenes precargadas y una
captura de los pasos de construcción. Los estudiantes aún deben interpretar el
Dockerfile, la red y el volumen. La clase no debe convertirse en dos horas de
diagnóstico de instalaciones.

## Salida individual

Dibujar el recorrido de una consulta desde `app.py` hasta PostgreSQL, indicando
qué elementos pertenecen a la imagen, al contenedor, a la red y al volumen.

## Referencias

- Dockerfile: <https://docs.docker.com/reference/dockerfile/>
- Compose: <https://docs.docker.com/compose/compose-file/>
- Imagen oficial de PostgreSQL: <https://hub.docker.com/_/postgres>
