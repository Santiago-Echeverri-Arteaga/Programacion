def copiar_matriz(matriz):
    copia = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            nueva_fila.append(valor)
        copia.append(nueva_fila)
    return copia


def imprimir_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(f"{valor:6.2f}", end=" ")
        print()
    print()


# Tamaño de la placa
n = 7

# Crear matriz llena de ceros
placa = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(0.0)
    placa.append(fila)

# Punto caliente en el centro
placa[n // 2][n // 2] = 100.0

# Parámetros del proceso
tolerancia = 0.01
cambio_maximo = float("inf")
iteracion = 0

print("Matriz inicial:")
imprimir_matriz(placa)

# Repetir hasta llegar casi al equilibrio
while cambio_maximo > tolerancia:
    nueva_placa = copiar_matriz(placa)
    cambio_maximo = 0.0

    # Recorrer solo el interior (sin tocar bordes)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            nueva_temperatura = (
                placa[i - 1][j] +
                placa[i + 1][j] +
                placa[i][j - 1] +
                placa[i][j + 1]
            ) / 4

            cambio = abs(nueva_temperatura - placa[i][j])

            if cambio > cambio_maximo:
                cambio_maximo = cambio

            nueva_placa[i][j] = nueva_temperatura

    placa = nueva_placa
    iteracion += 1

    print(f"Iteración {iteracion} - cambio máximo: {cambio_maximo:.4f}")
    imprimir_matriz(placa)

print("La placa llegó aproximadamente al equilibrio.")
print(f"Iteraciones totales: {iteracion}")
