# def contador(max: int):
#    print("Dentro del contador - Empezando")
#    n = 0
#    while n < max:
#        print(f"Dentro del contador - viene con yield n={n}")
#        yield (n)
#        print("Dentro del contador - retomando después del yield")
#        n += 1
#    print("Dentro del contador - Terminado")


# print("Instanciando contador")
# mycont = contador(3)
# print("Contador Instanciado")

# for i in mycont:
#    print(f"Valor leído del iterador={i}")
# print("Listo")


print(tuple(j+k for j, k in ((i, j) for i in range(4)
                             if not i % 2 for j in range(10) if not j % 3)))
