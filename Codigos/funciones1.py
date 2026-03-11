"""Código para explicar el uso de funciones
    """


def suma(a: float, b: float) -> float:
    """Código para sumar dos números

    Args:
        a (float): primer valor a sumar
        b (float): segundo valor a sumar

    Returns:
        float: suma de a y b

    >>> suma(2,4)
    6
    """
    print("Hola Mundo, estoy sumando")
    resultado = a+b
    return (resultado)
    print("ya sumé")


valor = suma(3, 5)
print(valor)
help(suma)
