"""Demo de SimPy: dos procesos comparten un reloj simulado."""

import simpy


def medir(entorno, nombre, intervalo, repeticiones):
    for numero in range(repeticiones):
        yield entorno.timeout(intervalo)
        print(f"t={entorno.now}: {nombre}, medición {numero + 1}")


entorno = simpy.Environment()
entorno.process(medir(entorno, "sensor_a", 2, 3))
entorno.process(medir(entorno, "sensor_b", 3, 2))
entorno.run()
