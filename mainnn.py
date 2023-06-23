import tkinter as tk
from tkinter import messagebox

class ConteoVehicularApp:
    def __init__(self, master):
        self.master = master
        self.contadores = {'Clasificación 1': [0, 0], 'Clasificación 2': [0, 0], 'Clasificación 3': [0, 0], 'Clasificación 4': [0, 0], 'Clasificación 5': [0, 0], 'Clasificación 6': [0, 0], 'Clasificación 7': [0, 0], 'Clasificación 8': [0, 0], 'Clasificación 9': [0, 0], 'Clasificación 10': [0, 0], 'Clasificación 11': [0, 0], 'Clasificación 12': [0, 0], 'Clasificación 13': [0, 0]}

        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.LEFT, padx=10)

        self.buttons = []  # Inicializar lista de botones

        self.columna1 = self.crear_columna(0)
        self.columna2 = self.crear_columna(1)

        self.ver_boton1 = tk.Button(self.frame, text="Ver datos columna 1", command=lambda: self.ver_datos(0))
        self.ver_boton1.grid(row=len(self.contadores), column=0, columnspan=2, pady=10)

        self.ver_boton2 = tk.Button(self.frame, text="Ver datos columna 2", command=lambda: self.ver_datos(1))
        self.ver_boton2.grid(row=len(self.contadores) + 1, column=0, columnspan=2)

        self.copiar_boton1 = tk.Button(self.frame, text="Copiar columna 1", command=lambda: self.copiar_al_portapapeles(0))
        self.copiar_boton1.grid(row=len(self.contadores) + 2, column=0, columnspan=2, pady=10)

        self.copiar_boton2 = tk.Button(self.frame, text="Copiar columna 2", command=lambda: self.copiar_al_portapapeles(1))
        self.copiar_boton2.grid(row=len(self.contadores) + 3, column=0, columnspan=2)

    def crear_columna(self, columna):
        columna_frame = tk.Frame(self.frame)
        columna_frame.grid(row=0, column=columna)

        for i, clasificacion in enumerate(self.contadores.keys()):
            button = tk.Button(columna_frame, text=clasificacion, command=lambda c=clasificacion: self.incrementar_contador(c, columna))
            button.grid(row=i, column=0)
            self.buttons.append(button)

        return columna_frame

    def incrementar_contador(self, clasificacion, columna):
        self.contadores[clasificacion][columna] += 1

    def ver_datos(self, columna):
        datos_ventana = tk.Toplevel(self.master)
        datos_ventana.title(f"Datos Columna {columna + 1}")

        datos_frame = tk.Frame(datos_ventana)
        datos_frame.pack(side=tk.LEFT, padx=10)

        encabezados = list(self.contadores.keys())

        for i, clasificacion in enumerate(encabezados):
            encabezado_label = tk.Label(datos_frame, text=clasificacion)
            encabezado_label.grid(row=0, column=i, padx=5, pady=5)

            valor_label = tk.Label(datos_frame, text=str(self.contadores[clasificacion][columna]))
            valor_label.grid(row=1, column=i, padx=5, pady=5)

    def copiar_al_portapapeles(self, columna):
        data = ''
        encabezados = "\t".join(self.contadores.keys())
        cantidades = "\t".join(str(self.contadores[clasificacion][columna]) for clasificacion in self.contadores.keys())

        data += encabezados + "\n" + cantidades + "\n"

        self.master.clipboard_clear()
        self.master.clipboard_append(data)
        messagebox.showinfo("Información", f"Datos columna {columna + 1} copiados al portapapeles.")

if __name__ == '__main__':
    root = tk.Tk()
    app = ConteoVehicularApp(root)
    root.mainloop()
