"""Ingreso y producto de matrices"""


def solicitar_matriz(n: int):
    """_summary_

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    A = input("Ingrese letra con la que denota la primera matriz: ")
    matriz_A = []
    for _ in range(n):
        matriz_A.append([0]*n)
    # Ingreso valores de A
    for i in range(n):
        for j in range(n):
            texto = "Ingrese el valor de " + A + \
                "_{" + str(i) + "," + str(j) + "}: "
            matriz_A[i][j] = float(input(texto))
    return (matriz_A, A)


# Producto de matrices
def suma(matriz_A: list, matriz_B: list):
    """_summary_

    Args:
        matriz_A (_type_): _description_
        matriz_B (_type_): _description_

    Returns:
        _type_: _description_
    """
    resultado = []
    for _ in range(n):
        resultado.append([0]*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_A[i][k]*matriz_B[k][j]
    return (resultado)


if __name__ == "__main__":
    n = int(input("Ingrese la dimensión de las matrices: "))
    Matriz_A, nombre_A = solicitar_matriz(n)
    Matriz_B, nombre_B = solicitar_matriz(n)
    resultado = suma(Matriz_A, Matriz_B)
    print(resultado)
