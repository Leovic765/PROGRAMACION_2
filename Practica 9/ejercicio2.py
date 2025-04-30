import tkinter as tk
from tkinter import messagebox
import random
import math

# --- a) Interfaz Coloreado ---
class Coloreado:
    def comoColorear(self):
        pass

# --- b) Clase abstracta Figura ---
class Figura(Coloreado):
    def __init__(self, color="negro"): 
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"Figura de color {self.color}"

    def area(self):
        pass

    def perimetro(self):
        pass

# --- c) Clase Cuadrado ---
class Cuadrado(Figura):
    def __init__(self, lado, color="rojo"):  
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

    def toString(self):
        return f"Cuadrado: lado={self.lado}, color={self.color}"

# --- d) Clase Circulo ---
class Circulo(Figura):
    def __init__(self, radio, color="azul"): 
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def toString(self):
        return f"Círculo: radio={self.radio}, color={self.color}"

# --- f) Programa de prueba con Tkinter ---
class Aplicacion:
    def __init__(self, ventana):  
        self.ventana = ventana
        self.ventana.title("Objetos Coloreados")
        self.ventana.geometry("400x300")

        # Botón para generar figuras
        self.boton = tk.Button(ventana, text="Generar Figuras", command=self.generar_figuras)
        self.boton.pack(pady=20)

        # Área de texto para mostrar resultados
        self.texto = tk.Text(ventana, height=10, width=50)
        self.texto.pack()

    def generar_figuras(self):
        self.texto.delete(1.0, tk.END)
        figuras = []

        # Generar 5 figuras aleatorias
        for _ in range(5):
            tipo = random.randint(1, 2)  
            if tipo == 1:
                lado = random.randint(1, 10)
                figuras.append(Cuadrado(lado))
            else:
                radio = random.randint(1, 10)
                figuras.append(Circulo(radio))

        # Mostrar información de cada figura
        for figura in figuras:
            self.texto.insert(tk.END, f"{figura.toString()}\n")
            self.texto.insert(tk.END, f"Área: {figura.area():.2f}\n")
            self.texto.insert(tk.END, f"Perímetro: {figura.perimetro():.2f}\n")
            
            # Verificar si tiene el método comoColorear
            if hasattr(figura, 'comoColorear'):
                self.texto.insert(tk.END, f"Método colorear: {figura.comoColorear()}\n")
            
            self.texto.insert(tk.END, "-" * 30 + "\n")

# --- Ejecutar la aplicación ---
if __name__ == "__main__": 
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()

