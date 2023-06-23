import tkinter as tk
import pandas as pd
from tkinter import ttk

class ContadorInterfaz:
    def __init__(self, root):
        self.contador1 = 0
        self.contador2 = 0
        self.root = root

        # Crear los botones
        self.boton1 = tk.Button(self.root, text="Boton 1", command=self.sumar1)
        self.boton1.pack()

        self.boton2 = tk.Button(self.root, text="Boton 2", command=self.sumar2)
        self.boton2.pack()

        self.boton_vista = tk.Button(self.root, text="Vista", command=self.mostrar_tabla)
        self.boton_vista.pack()

        self.boton_guardar = tk.Button(self.root, text="Guardar", command=self.guardar)
        self.boton_guardar.pack()

        # Cargar los datos existentes desde el archivo CSV
        self.datos = pd.DataFrame(columns=["Boton 1", "Boton 2"])
        try:
            self.datos = pd.read_csv("datos.csv")
        except FileNotFoundError:
            pass

    def sumar1(self):
        self.contador1 += 1

    def sumar2(self):
        self.contador2 += 1

    def mostrar_tabla(self):
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Tabla")

        # Crear el widget Treeview para mostrar la tabla
        treeview = ttk.Treeview(ventana_tabla, columns=["Boton 1", "Boton 2"], show="headings")
        treeview.heading("Boton 1", text="Boton 1")
        treeview.heading("Boton 2", text="Boton 2")
        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

        # Crear una barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(ventana_tabla, orient=tk.VERTICAL, command=treeview.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Asociar la barra de desplazamiento con el widget Treeview
        treeview.configure(yscrollcommand=scrollbar.set)

        # Insertar los datos en la tabla
        for _, row in self.datos.iterrows():
            treeview.insert("", "end", values=(row["Boton 1"], row["Boton 2"]))

    def guardar(self):
        nuevo_dato = pd.DataFrame({"Boton 1": [self.contador1], "Boton 2": [self.contador2]})
        self.datos = pd.concat([self.datos, nuevo_dato], ignore_index=True)
        self.contador1 = 0  # Reiniciar contador 1
        self.contador2 = 0  # Reiniciar contador 2

        # Guardar los datos en el archivo CSV
        self.datos.to_csv("datos.csv", index=False)

root = tk.Tk()
app = ContadorInterfaz(root)
root.mainloop()
