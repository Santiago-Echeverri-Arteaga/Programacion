Estudiantes = ["Diana", "Juan David", "Andrés", "Sebastián", "Viviana"]
Notas = [4.5, 3.3, 5.0, 1.5, 4.2]
Horas_Estudio = [8, 2, 2, 12, 0]
for estudiante, nota, cantidad in zip(Estudiantes, Notas, Horas_Estudio):
    if nota < 3:
        continue
    elif cantidad == 0:
        print("Error!")
        break
    print(f"{estudiante} sacó en Termodinámica con la profesora Angélica {nota} y estudio durante {cantidad} horas")
else:
    print("Se llegó al fin de los estudiantes")
