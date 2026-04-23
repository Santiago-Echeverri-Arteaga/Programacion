"""
Ejemplo de uso de clases

Realizado el primer semestre de 2026
Santiago Echeverri Arteaga
"""


class uniquindiano:
    """Clase Uniquindiano
    """

    def __init__(self, nombre: str, apellido: str):
        self.name = nombre
        self.last = apellido
        self.full = self._unir_(1)

    def __str__(self):
        return (self.full)

    def add(self, **kwargs):
        for keys, values in kwargs.items():
            setattr(self, keys, values)
        self.year = 2026

    def _unir_(self, espacios: int):
        return (self.name + espacios*" " + self.last)


class vector:
    def __init__(self, x: float, y: float):
        self.value = [x, y]
        self.magnitud = (x**2+y**2)**0.5
        from math import atan2
        self.angulo = atan2(y, x)

    def __str__(self):
        cadena = "(" + str(self.value[0]) + ", " + str(self.value[1]) + ")"
        return (cadena)

    def __repr__(self):
        return (f"Lista flotante: {self.value}")

    def __add__(self, other):
        return (vector(self.value[0]+other.value[0], self.value[1]+other.value[1]))


v1 = vector(5, 3)
vector2 = vector(1, 4)

v3 = v1+vector2+v1+v1+vector2
print(v3.magnitud, v3.angulo)


def main_uniquindiano():
    Ana = uniquindiano("Ana", "Grajales")
    Ana.add(edad=32, profesion="Psicologa")

    Bob = uniquindiano("Bob", "Dylan")

    print(Ana.edad, Ana.year, Ana.profesion)
    try:
        print(Bob.year)
    except Exception as e:
        print(e)
