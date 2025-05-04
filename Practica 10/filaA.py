class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregar_empleado(self, nombre, edad, sueldo):
        self.empleados.append(nombre)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def eliminar_empleado(self, apellido):
        nuevos_empleados = []
        nuevas_edades = []
        nuevos_sueldos = []
        for i in range(self.nroEmpleados):
            if apellido not in self.empleados[i]:
                nuevos_empleados.append(self.empleados[i])
                nuevas_edades.append(self.edades[i])
                nuevos_sueldos.append(self.sueldos[i])
        self.empleados = nuevos_empleados
        self.edades = nuevas_edades
        self.sueldos = nuevos_sueldos
        self.nroEmpleados = len(self.empleados)

    def mostrar_mayor_edad(self):
        max_edad = max(self.edades)
        for i in range(self.nroEmpleados):
            if self.edades[i] == max_edad:
                print(f"Empleado con mayor edad: {self.empleados[i]}, Edad: {max_edad}")

    def mostrar_mayor_sueldo(self):
        max_sueldo = max(self.sueldos)
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == max_sueldo:
                print(f"Empleado con mayor sueldo: {self.empleados[i]}, Sueldo: {max_sueldo}")

    def __add__(self, otro):
        ¿
        if otro.nroEmpleados > 0:
            self.agregar_empleado(otro.empleados[-1], otro.edades[-1], otro.sueldos[-1])
            otro.empleados.pop()
            otro.edades.pop()
            otro.sueldos.pop()
            otro.nroEmpleados -= 1


#Main
t1 = LineaTeleferico("Rojo", "Tramo A", 20)
t1.agregar_empleado("Pedro Rojas Luna", 35, 2500)
t1.agregar_empleado("Lucy Sosa Rios", 43, 3250)
t1.agregar_empleado("Ana Perez Rojas", 26, 2700)
t1.agregar_empleado("Saul Arce Calle", 29, 2500)

t2 = LineaTeleferico("Verde", "Tramo B", 15)
t2.agregar_empleado("Carlos X Mendoza", 40, 3000)

t1.eliminar_empleado("Rojas")
t1 + t2 

t1.mostrar_mayor_edad()
t1.mostrar_mayor_sueldo()
