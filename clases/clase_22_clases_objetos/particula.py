"""Objeto simple con una invariante física explícita."""


class Particula:
    def __init__(self, masa_kg: float, velocidad_m_s: float = 0.0) -> None:
        if masa_kg <= 0:
            raise ValueError("la masa debe ser positiva")
        self.masa_kg = masa_kg
        self.velocidad_m_s = velocidad_m_s

    def energia_cinetica(self) -> float:
        return 0.5 * self.masa_kg * self.velocidad_m_s**2

    def aplicar_impulso(self, impulso_n_s: float) -> None:
        self.velocidad_m_s += impulso_n_s / self.masa_kg
