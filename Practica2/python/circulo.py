import turtle
from punto import Punto

class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def dibujaCirculo(self, t):
        t.penup()
        t.goto(self.centro.x, self.centro.y - self.radio)  # Ajuste de posición
        t.pendown()
        t.circle(self.radio)

    def __str__(self):
        return f"Circulo(Centro={self.centro}, Radio={self.radio})"
