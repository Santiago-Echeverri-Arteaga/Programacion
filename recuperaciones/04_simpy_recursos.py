"""Demo de SimPy: trabajos compiten por un instrumento."""

import simpy


def usar_instrumento(entorno, instrumento, nombre, llegada, duracion):
    yield entorno.timeout(llegada)
    instante_llegada = entorno.now
    with instrumento.request() as solicitud:
        yield solicitud
        espera = entorno.now - instante_llegada
        print(f"{nombre}: inicia={entorno.now}, espera={espera}")
        yield entorno.timeout(duracion)
        print(f"{nombre}: termina={entorno.now}")


entorno = simpy.Environment()
instrumento = simpy.Resource(entorno, capacity=1)
entorno.process(usar_instrumento(entorno, instrumento, "muestra_a", 0, 4))
entorno.process(usar_instrumento(entorno, instrumento, "muestra_b", 1, 2))
entorno.process(usar_instrumento(entorno, instrumento, "muestra_c", 2, 1))
entorno.run()
