import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import filedialog

class ContadorInterfaz:
    def __init__(self, root):
        self.contador1 = 0
        self.contador2 = 0
        self.contador3 = 0
        self.contador4 = 0
        self.contador5 = 0
        self.contador6 = 0
        self.root = root
        self.datos = pd.DataFrame(columns=["Boton 1", "Boton 2", "Boton 3", "Boton 4", "Boton 5", "Boton 6"])

        # Crear los botones
        self.boton1 = tk.Button(self.root, text="Boton 1", command=self.sumar1)
        self.boton1.pack()

        self.boton2 = tk.Button(self.root, text="Boton 2", command=self.sumar2)
        self.boton2.pack()

        self.boton3 = tk.Button(self.root, text="Boton 3", command=self.sumar3)
        self.boton3.pack()

        self.boton_vista = tk.Button(self.root, text="Vista", command=self.mostrar_tabla)
        self.boton_vista.pack()

        # Crear los botones para la segunda columna
        self.boton4 = tk.Button(self.root, text="Boton 4", command=self.sumar4)
        self.boton4.pack()

        self.boton5 = tk.Button(self.root, text="Boton 5", command=self.sumar5)
        self.boton5.pack()

        self.boton6 = tk.Button(self.root, text="Boton 6", command=self.sumar6)
        self.boton6.pack()

        self.boton_vista2 = tk.Button(self.root, text="Vista 2", command=self.mostrar_tabla2)
        self.boton_vista2.pack()

        self.boton_guardar = tk.Button(self.root, text="Guardar", command=self.guardar)
        self.boton_guardar.pack()

        # Cargar los datos existentes desde el archivo Excel
        try:
            self.datos = pd.read_excel("datos.xlsx")
        except FileNotFoundError:
            pass

    def sumar1(self):
        self.contador1 += 1

    def sumar2(self):
        self.contador2 += 1

    def sumar3(self):
        self.contador3 += 1

    def sumar4(self):
        self.contador4 += 1

    def sumar5(self):
        self.contador5 += 1

    def sumar6(self):
        self.contador6 += 1

    def mostrar_tabla(self):
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Tabla")

        # Crear el widget Treeview para mostrar la tabla
        treeview = ttk.Treeview(ventana_tabla, columns=["Boton 1", "Boton 2", "Boton 3"], show="headings")
        treeview.heading("Boton 1", text="Boton 1")
        treeview.heading("Boton 2", text="Boton 2")
        treeview.heading("Boton 3", text="Boton 3")
        treeview.pack()

        # Mostrar los datos en el Treeview
        for index, row in self.datos.iterrows():
            treeview.insert("", "end", values=[row["Boton 1"], row["Boton 2"], row["Boton 3"]])

    def mostrar_tabla2(self):
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Tabla")

        # Crear el widget Treeview para mostrar la tabla
        treeview = ttk.Treeview(ventana_tabla, columns=["Boton 4", "Boton 5", "Boton 6"], show="headings")
        treeview.heading("Boton 4", text="Boton 4")
        treeview.heading("Boton 5", text="Boton 5")
        treeview.heading("Boton 6", text="Boton 6")
        treeview.pack()

        # Mostrar los datos en el Treeview
        for index, row in self.datos.iterrows():
            treeview.insert("", "end", values=[row["Boton 4"], row["Boton 5"], row["Boton 6"]])

    def guardar(self):
        new_data = {"Boton 1": self.contador1, "Boton 2": self.contador2, "Boton 3": self.contador3,
                    "Boton 4": self.contador4, "Boton 5": self.contador5, "Boton 6": self.contador6}
        self.datos = self.datos.append(new_data, ignore_index=True)
        self.datos.to_excel("datos.xlsx", index=False)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ventana de Botones")
    contador_interfaz = ContadorInterfaz(root)
    root.mainloop()
