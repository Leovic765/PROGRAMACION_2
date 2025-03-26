import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        media = self.promedio()
        suma_cuadrados = sum((x - media) ** 2 for x in self.numeros)
        return math.sqrt(suma_cuadrados / (len(self.numeros) - 1))

# Entrada de usuario
try:
    numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

    if len(numeros) != 10:
        print("Debe ingresar exactamente 10 números.")
    else:
        estadisticas = Estadisticas(numeros)
        print(f"El promedio es {estadisticas.promedio():.2f}")
        print(f"La desviación estándar es {estadisticas.desviacion():.5f}")
except ValueError:
    print("Entrada no válida. Asegúrese de ingresar números correctamente.")
