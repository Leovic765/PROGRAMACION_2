import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros):
    media = promedio(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (len(numeros) - 1))

# Entrada de usuario
try:
    numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
    
    if len(numeros) != 10:
        print("Debe ingresar exactamente 10 números.")
    else:
        media = promedio(numeros)
        desviacion_estandar = desviacion(numeros)
        print(f"El promedio es {media:.2f}")
        print(f"La desviación estándar es {desviacion_estandar:.5f}")
except ValueError:
    print("Entrada no válida. Asegúrese de ingresar números correctamente.")
