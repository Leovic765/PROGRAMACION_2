import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# CLASE PADRE
class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Numero: {self.numero}, Precio: {self.precio:.1f}"

#SUBCLASES 
class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0

# INTERFAZ GRAFICA 
class VentanaTeatro:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")
        self.root.geometry("450x300")

        #Titulo
        lbl_titulo = tk.Label(root, text="Teatro Municipal", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=10)

        #Farme central
        frame = tk.LabelFrame(root, text="Datos del Boleto", padx=10, pady=10)
        frame.pack(padx=20, pady=5, fill="x")

        #Tipo de boleto
        self.tipo = tk.StringVar(value="Palco")
        tk.Radiobutton(frame, text="Palco", variable=self.tipo, value="Palco").grid(row=0, column=0)
        tk.Radiobutton(frame, text="Platea", variable=self.tipo, value="Platea").grid(row=0, column=1)
        tk.Radiobutton(frame, text="Galeria", variable=self.tipo, value="Galeria").grid(row=0, column=2)

        #Numero
        tk.Label(frame, text="Numero:").grid(row=1, column=0, sticky="e")
        self.txt_numero = tk.Entry(frame)
        self.txt_numero.grid(row=1, column=1)

        #Dias para el evento
        tk.Label(frame, text="Cant. Dias para el Evento:").grid(row=2, column=0, columnspan=2, sticky="e")
        self.txt_dias = tk.Entry(frame)
        self.txt_dias.grid(row=2, column=2)

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)
        tk.Button(frame_botones, text="Vende", width=10, command=self.vender).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Salir", width=10, command=root.quit).grid(row=0, column=1)

        #informacion
        self.lbl_resultado = tk.Label(root, text="Informacion:", font=("Lucida Sans", 10, "bold"), fg="blue")
        self.lbl_resultado.pack(pady=10)

    def vender(self):
        tipo = self.tipo.get()
        numero = self.txt_numero.get()
        dias = self.txt_dias.get()

        if not numero.isdigit():
            messagebox.showerror("Error", "El numero del boleto debe ser un numero entero.")
            return

        numero = int(numero)

        try:
            dias = int(dias) if dias else 0
        except:
            messagebox.showerror("Error", "Los dias deben ser un numero entero.")
            return

        boleto = None

        if tipo == "Palco":
            boleto = Palco(numero)
        elif tipo == "Platea":
            boleto = Platea(numero, dias)
        elif tipo == "Galeria":
            boleto = Galeria(numero, dias)

        self.lbl_resultado.config(text=str(boleto))

#EJECUCION 
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaTeatro(root)
    root.mainloop()
