"""Ejemplo 2: configuración y transacción con Psycopg.
Ejecuta con una base propia preparada según la guía:
    export PGDATABASE=curso_datos
    python ejemplos/02_conexion_y_transaccion.py
No cambia datos meteorológicos. El ensayo artificial es temporal y se revierte.
"""
import os
import psycopg


def main():
    # export en Bash crea una variable que Python puede leer.
    # get devuelve el valor indicado o el valor por defecto si no existe.
    base = os.environ.get('PGDATABASE', 'curso_datos')
    print('Base elegida:', base)

    # Una conexión es el canal hacia PostgreSQL. El cursor envía SQL y recibe filas.
    # with cierra los recursos; con Psycopg, la conexión también controla la transacción.
    # Salida normal: COMMIT. Excepción que sale del bloque: ROLLBACK.
    with psycopg.connect(dbname=base) as conexion:
        with conexion.cursor() as cursor:
            consulta = '''SELECT fecha, tmax_c FROM silver.observaciones
                          WHERE ciudad_id=%s ORDER BY fecha LIMIT 3'''
            ciudad = 'armenia'
            cursor.execute(consulta, (ciudad,))
            # (ciudad,) es una tupla de UN elemento; la coma es necesaria.
            # %s no se sustituye con f-strings. Psycopg envía SQL y valores separados.
            # Así un valor sigue siendo un dato, no instrucciones SQL nuevas.
            filas = cursor.fetchall()
            for fila in filas:
                print(fila)
            # fetchone obtiene una fila; fetchall obtiene todas las del resultado.
            # Aquí hay como máximo tres. No usar fetchall sin pensar en la RAM.

            cursor.execute('CREATE TEMP TABLE ensayo_ejemplo (id INTEGER PRIMARY KEY)')
            cursor.execute('INSERT INTO ensayo_ejemplo VALUES (%s)', (1,))
            cursor.execute('SELECT COUNT(*) FROM ensayo_ejemplo')
            resultado = cursor.fetchone()  # Tupla (1,)
            print('Filas temporales antes del rollback:', resultado[0])
        conexion.rollback()  # Revierte también la creación de la tabla temporal.
    print('Ensayo revertido; las observaciones reales no cambiaron.')

    # En la ingesta, un for ejecuta INSERT para cada fila, dentro de un solo with.
    # Una falla en Silver revierte también los INSERT de Bronze de esa transacción.
    # Este control es del servidor: cerrar un archivo CSV no ofrece esa propiedad.


if __name__ == '__main__':
    main()
