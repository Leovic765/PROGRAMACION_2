import turtle
from punto import Punto

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def dibujaLinea(self, t):
        t.penup()
        t.goto(self.p1.x, self.p1.y)
        t.pendown()
        t.goto(self.p2.x, self.p2.y)

    def __str__(self):
        return f"Linea({self.p1}, {self.p2})"