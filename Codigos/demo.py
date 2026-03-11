
n = int(input("Ingrese la dimensión de las matrices: "))

#############
#   Matriz A
#############

# Creo la matriz A como matriz vacía
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

#############
#   Matriz B
#############

# Creo la matriz B como matriz vacía
B = input("Ingrese letra con la que denota la segunda matriz: ")
matriz_B = []
for _ in range(n):
    matriz_B.append([0]*n)
# Ingreso valores de B
for i in range(n):
    for j in range(n):
        texto = "Ingrese el valor de " + B + \
            "_{" + str(i) + "," + str(j) + "}: "
        matriz_B[i][j] = float(input(texto))

# Producto de matrices
resultado = []
for _ in range(n):
    resultado.append([0]*n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            resultado[i][j] += matriz_A[i][k]*matriz_B[k][j]

print(resultado)
