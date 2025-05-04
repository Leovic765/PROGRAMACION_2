class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregar_empleado(self, nombre, edad, sueldo):
        self.empleados.append(nombre)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def eliminar_empleado_por_edad(self, edad_objetivo):
        nuevos_empleados = []
        nuevas_edades = []
        nuevos_sueldos = []
        for i in range(self.nroEmpleados):
            if self.edades[i] != edad_objetivo:
                nuevos_empleados.append(self.empleados[i])
                nuevas_edades.append(self.edades[i])
                nuevos_sueldos.append(self.sueldos[i])
        self.empleados = nuevos_empleados
        self.edades = nuevas_edades
        self.sueldos = nuevos_sueldos
        self.nroEmpleados = len(self.empleados)

    def mostrar_menor_edad(self):
        min_edad = min(self.edades)
        for i in range(self.nroEmpleados):
            if self.edades[i] == min_edad:
                print(f"Empleado con menor edad: {self.empleados[i]}, Edad: {min_edad}")

    def mostrar_menor_sueldo(self):
        min_sueldo = min(self.sueldos)
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == min_sueldo:
                print(f"Empleado con menor sueldo: {self.empleados[i]}, Sueldo: {min_sueldo}")

    def __add__(self, otro):
        if otro.nroEmpleados > 0:
            self.agregar_empleado(otro.empleados[-1], otro.edades[-1], otro.sueldos[-1])
            otro.empleados.pop()
            otro.edades.pop()
            otro.sueldos.pop()
            otro.nroEmpleados -= 1


# ---- Prueba del Ejercicio ----
m1 = Ministerio("Educación", "La Paz")
m1.agregar_empleado("Pedro Rojas Luna", 35, 2500)
m1.agregar_empleado("Lucy Sosa Rios", 43, 3250)
m1.agregar_empleado("Ana Perez Rojas", 26, 2700)
m1.agregar_empleado("Saul Arce Calle", 29, 2500)

m2 = Ministerio("Salud", "Cochabamba")
m2.agregar_empleado("Carlos Mendoza", 26, 3000)

m1.eliminar_empleado_por_edad(43)
m1 + m2  # Transferir empleado de m2 a m1

m1.mostrar_menor_edad()
m1.mostrar_menor_sueldo()
