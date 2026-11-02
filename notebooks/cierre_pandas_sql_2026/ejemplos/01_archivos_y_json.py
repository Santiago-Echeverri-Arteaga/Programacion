"""Ejemplo 1: archivos, JSON, ausencias, fechas y huellas.
Ejecuta: python ejemplos/01_archivos_y_json.py
No requiere PostgreSQL ni internet y no modifica archivos.
"""
from pathlib import Path
from datetime import date, timedelta
import hashlib
import json


def main():
    # Path representa una ruta. / une carpetas de forma portable.
    # __file__ apunta a ESTE programa, aunque la terminal esté en otra carpeta.
    carpeta_ejemplos = Path(__file__).resolve().parent
    modulo = carpeta_ejemplos.parent
    ruta = modulo / 'datos' / 'originales' / 'armenia_inicial.json'

    # Bytes son el contenido exacto guardado. No los alteramos para calcular la huella.
    contenido = ruta.read_bytes()
    huella = hashlib.sha256(contenido).hexdigest()
    print('SHA-256:', huella)
    # Una huella permite detectar cambios; no demuestra exactitud científica.
    # La ingesta compara esta huella con la del manifiesto antes de cargar offline.

    # JSON es el formato de la API: json.loads ya sabe interpretarlo.
    # No escribimos un parser: obtenemos diccionarios y listas conocidos del curso.
    respuesta = json.loads(contenido)
    diario = respuesta['daily']
    print('Tipo del resultado:', type(respuesta))  # dict
    print('Tipo de las fechas:', type(diario['time']))  # list
    print('Primer día:', diario['time'][0])  # 2024-01-01
    print('Primera máxima real:', diario['temperature_2m_max'][0])

    # Cada posición representa el mismo día en todas las columnas.
    # Esta es la razón de comprobar que las listas tienen igual longitud.
    for i in range(3):
        fecha = diario['time'][i]
        maxima = diario['temperature_2m_max'][i]
        print(fecha, maxima)

    # Demostración de formato, NO un registro meteorológico inventado:
    ejemplo_formato = json.loads('{"valor": null}')
    print(ejemplo_formato['valor'] is None)  # True: null JSON se convierte en None.
    # None significa ausencia; el número 0 significa un valor conocido.

    # Una fecha es un objeto, no un texto para sumar manualmente.
    dia = date.fromisoformat('2024-02-28')
    print(dia + timedelta(days=1))  # 2024-02-29 (año bisiesto)
    print(dia + timedelta(days=2))  # 2024-03-01
    # isoformat hace la conversión contraria: fecha -> texto AAAA-MM-DD.
    print(dia.isoformat())

    # Online usa el MISMO json.loads después de obtener bytes mediante HTTP:
    # from urllib.request import urlopen
    # with urlopen(url_documentada, timeout=45) as respuesta_http:
    #     contenido = respuesta_http.read()
    # El bloque with cierra el recurso incluso si ocurre una excepción.
    # timeout evita esperar indefinidamente. No se requiere ejecutar red aquí.


# Al ejecutar el archivo, Python usa el nombre especial __main__.
# Al importarlo, define main pero no realiza las lecturas hasta que la llamemos.
if __name__ == '__main__':
    main()
