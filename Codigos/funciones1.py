"""Código para explicar el uso de funciones
    """


def suma(a: list, b: list, a_celcius: int = 273.15) -> float:
    """Código para sumar dos números

    Args:
        a (float): primer valor a sumar
        b (float): segundo valor a sumar

    Returns:
        float: suma de a y b

    >>> suma(2,4)
    6
    """
    resultado = a+b+a_celcius
    return (resultado)


def funcion(**kwargs):
    print(kwargs)


def suma2(*a) -> float:
    """Código para sumar dos números

    Args:
        a (float): primer valor a sumar
        b (float): segundo valor a sumar

    Returns:
        float: suma de a y b

    >>> suma(2,4)
    6
    """
    resultado = 0
    for i in a:
        resultado += i
    return (resultado)


# print((lambda a, b, c, x: a*pow(x, 2)+b*x+c)(2, 3, 4, 5))
PI = 3.141519
if __name__ == "__main__":

    # valor = suma(3, 5, a_celcius=0)
    # print(valor)
    # valor = suma(3, 5, 0)
    # print(valor)
    # valor = suma(3, 5)
    # print(valor)
    # print("Hola soy funciones1.py")
    # print(suma2(3))
    # print(suma2(3, 4))
    # print(suma2(3, 4, 5))
    # print(suma2(3, 4, 5, 6, 7, 8, 9))
    funcion(valor=12, color="azul", linea="--", dato=[3, 4, 5, 6])
