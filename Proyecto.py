import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pandas as pd

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.contadores = {}
        self.tablas_valores = {}
        self.num_columnas = 1
        self.current_id = 1

        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(padx=20, pady=20)

        self.frame_superior = ttk.Frame(self.frame_principal)
        self.frame_superior.pack()

        self.botones_agregar_eliminar = ttk.Frame(self.frame_superior)
        self.botones_agregar_eliminar.pack(side="left", padx=(0, 10))

        self.boton_agregar = ttk.Button(self.botones_agregar_eliminar, text="+", width=3, command=self.agregar_columna)
        self.boton_agregar.pack(side="left")

        self.boton_eliminar = ttk.Button(self.botones_agregar_eliminar, text="-", width=3, command=self.eliminar_columna)
        self.boton_eliminar.pack(side="left")

        self.cuadros_texto = []

        for i in range(self.num_columnas):
            self.contadores[i] = {}

            frame_columna = ttk.Frame(self.frame_superior)
            frame_columna.pack(side="left", padx=(10, 20))

            cuadro_texto = ttk.Entry(frame_columna, width=15)
            cuadro_texto.pack(pady=(10, 5))
            self.cuadros_texto.append(cuadro_texto)

            for j, boton in enumerate(["Peatón", "Bici", "Auto", "Moto", "Bus Mio", "Buc Mio", "Buc", "Bus", "C2P", "C2G", "C3-C4", "C5", "Campero"]):
                boton_incrementar = ttk.Button(frame_columna, text=boton, width=10, command=lambda col=i, btn=boton: self.incrementar_contador(col, btn))
                boton_incrementar.pack(pady=2)

                self.contadores[i][boton] = 0

            boton_tabla_valores = ttk.Button(frame_columna, text="Tabla de Valores", width=10, command=lambda col=i: self.mostrar_tabla_valores(col))
            boton_tabla_valores.pack(pady=(10, 0))

        self.frame_inferior = ttk.Frame(self.frame_principal)
        self.frame_inferior.pack(pady=(20, 0))

        self.boton_guardar = ttk.Button(self.frame_inferior, text="Guardar +15min", width=15, command=self.guardar_datos)
        self.boton_guardar.pack(side="left", padx=(0, 20))

        self.boton_borrar = ttk.Button(self.frame_inferior, text="Borrar Registros", width=15, command=self.borrar_registros)
        self.boton_borrar.pack(side="left")

        # Mantener la ventana principal siempre al frente
        self.root.attributes("-topmost", True)

    def incrementar_contador(self, columna, boton):
        self.contadores[columna][boton] += 1

    def agregar_columna(self):
        if self.num_columnas < 7:
            self.num_columnas += 1

            frame_columna = ttk.Frame(self.frame_superior)
            frame_columna.pack(side="left", padx=(10, 20))

            cuadro_texto = ttk.Entry(frame_columna, width=15)
            cuadro_texto.pack(pady=(10, 5))
            self.cuadros_texto.append(cuadro_texto)

            self.contadores[self.num_columnas - 1] = {}

            for j, boton in enumerate(["Peatón", "Bici", "Auto", "Moto", "Bus Mio", "Buc Mio", "Buc", "Bus", "C2P", "C2G", "C3-C4", "C5", "Campero"]):
                boton_incrementar = ttk.Button(frame_columna, text=boton, width=10, command=lambda col=self.num_columnas - 1, btn=boton: self.incrementar_contador(col, btn))
                boton_incrementar.pack(pady=2)

                self.contadores[self.num_columnas - 1][boton] = 0

            boton_tabla_valores = ttk.Button(frame_columna, text="Tabla de Valores", width=10, command=lambda col=self.num_columnas - 1: self.mostrar_tabla_valores(col))
            boton_tabla_valores.pack(pady=(10, 0))

    def eliminar_columna(self):
        if self.num_columnas > 1:
            self.num_columnas -= 1

            frame_columna = self.frame_superior.winfo_children()[-1]
            frame_columna.destroy()

            self.cuadros_texto.pop()

            self.contadores.pop(self.num_columnas)

    def mostrar_tabla_valores(self, columna):
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Tabla de Valores")

        tabla = self.obtener_tabla_valores(columna)

        tabla_frame = ttk.Frame(ventana_tabla)
        tabla_frame.pack(padx=20, pady=20)

        for i, columna_tabla in enumerate(tabla.columns):
            etiqueta_columna = ttk.Label(tabla_frame, text=columna_tabla)
            etiqueta_columna.grid(row=0, column=i+1, padx=5, pady=5)

        for i, row in enumerate(tabla.itertuples(index=False), start=1):
            etiqueta_id = ttk.Label(tabla_frame, text=row[0])
            etiqueta_id.grid(row=i, column=0, padx=5, pady=5)

            for j, valor in enumerate(row[1:], start=1):
                etiqueta_valor = ttk.Label(tabla_frame, text=valor)
                etiqueta_valor.grid(row=i, column=j, padx=5, pady=5)

        boton_copiar = ttk.Button(tabla_frame, text="Copiar", width=10, command=lambda: self.copiar_tabla_valores(columna))
        boton_copiar.grid(row=i+1, column=0, padx=5, pady=5)

    def obtener_tabla_valores(self, columna):
        if columna not in self.tablas_valores:
            self.tablas_valores[columna] = pd.DataFrame(columns=["ID"] + ["Auto", "Campero", "Bus Mio", "Buc Mio", "Buc", "Bus", "C2P", "C2G", "C3-C4", "C5", "Moto", "Bici", "Peatón"])

        tabla = self.tablas_valores[columna]

        for i, cuadro_texto in enumerate(self.cuadros_texto):
            valor = cuadro_texto.get()
            tabla.loc[self.current_id, tabla.columns[i+1]] = valor

        return tabla

    def guardar_datos(self):
        tabla_actual = self.obtener_tabla_valores(0)
        tabla_actual.fillna(0, inplace=True)

        messagebox.showinfo("Guardar +15min", f"Datos guardados en la fila con ID {self.current_id}")

        self.current_id += 1

    def borrar_registros(self):
        respuesta = messagebox.askquestion("Borrar Registros", "ESTA A PUNTO DE BORRAR TODO EL REGISTRO DE DATOS EXISTENTE. ¿DESEA CONTINUAR?")

        if respuesta == "yes":
            respuesta_confirmar = messagebox.askquestion("Borrar Registros", "CONFIRME NUEVAMENTE PARA BORRAR")

            if respuesta_confirmar == "yes":
                self.tablas_valores = {}
                self.current_id = 1

                messagebox.showinfo("Borrar Registros", "Registros borrados exitosamente")

    def copiar_al_portapapeles(self, columna):
        data = ''
        encabezados = "\t".join(self.contadores.keys())
        cantidades = "\t".join(str(self.contadores[clasificacion][columna]) for clasificacion in self.contadores.keys())

        data += encabezados + "\n" + cantidades + "\n"

        self.master.clipboard_clear()
        self.master.clipboard_append(data)
        messagebox.showinfo("Información", f"Datos columna {columna + 1} copiados al portapapeles.")

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()
