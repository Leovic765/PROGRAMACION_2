from punto import Punto
from linea import Linea
from circulo import Circulo
import turtle

p1 = Punto(0, 0)
p2 = Punto(100, 100)

print(p1.coord_cartesianas())
print(p1.coord_polares())

t = turtle.Turtle()
screen = turtle.Screen()

linea = Linea(p1, p2)
print(linea)
linea.dibujaLinea(t)

circulo = Circulo(p1, 141)
print(circulo)
circulo.dibujaCirculo(t)

screen.exitonclick()