# ventana_tabla.py

import tkinter as tk
from tkinter import ttk
import pandas as pd

class VentanaTabla:
    def __init__(self, ventana_principal, nombre_encabezado, datos):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Tabla de datos - " + nombre_encabezado)

        self.ventana.geometry("800x300")  # Establecer el ancho deseado

        self.encabezados = [f"Botón {i+1}" for i in range(13)]
        self.datos = pd.DataFrame([datos], columns=self.encabezados)

        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear la tabla utilizando un widget Treeview de tkinter
        self.tabla = ttk.Treeview(self.ventana, columns=self.encabezados, show="headings")

        # Configurar los encabezados de las columnas
        for encabezado in self.encabezados:
            self.tabla.heading(encabezado, text=encabezado)

        # Ajustar el ancho de las columnas
        for encabezado in self.encabezados:
            self.tabla.column(encabezado, width=50)  # Puedes ajustar el ancho deseado

        # Agregar la tabla a un Scrollbar
        scrollbar = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Posicionar la tabla y el Scrollbar en la ventana
        self.tabla.pack(fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Mostrar los datos iniciales en la tabla
        self.actualizar_vista_tabla()

    def actualizar_vista_tabla(self):
        # Borrar los elementos actuales de la tabla
        self.tabla.delete(*self.tabla.get_children())

        # Agregar las filas a la tabla
        for _, row in self.datos.iterrows():
            self.tabla.insert("", tk.END, values=row.tolist())

    def mostrar_ventana(self):
        self.ventana.mainloop()