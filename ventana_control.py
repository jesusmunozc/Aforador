import tkinter as tk
import xlsxwriter

class VentanaControl:
    def __init__(self, cantidad, nombres):
        self.cantidad = cantidad
        self.nombres = nombres
        self.ventana = None
        self.valores = [[0] * 13 for _ in range(self.cantidad)]
        self.libro_excel = None
        self.hoja_excel = None
        self.fila = 0

    def abrir_ventana(self):
        # Crear el archivo de Excel
        self.libro_excel = xlsxwriter.Workbook("datos.xlsx")
        self.hoja_excel = self.libro_excel.add_worksheet()

        # Crear la ventana de control
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de control")

        # Crear las columnas de botones con los encabezados
        for i in range(self.cantidad):
            marco = tk.Frame(self.ventana)
            marco.pack(side=tk.LEFT, padx=10)

            encabezado = tk.Label(marco, text=self.nombres[i])
            encabezado.pack()

            botones = []
            for j in range(13):
                boton = tk.Button(marco, text=f"Botón {j+1}", command=lambda col=i, row=j: self.incrementar_valor(col, row))
                boton.pack(pady=5)
                botones.append(boton)

        boton_siguiente = tk.Button(self.ventana, text="Siguiente", command=self.guardar_datos)
        boton_siguiente.pack(pady=10)

        # Centrar la ventana
        self.ventana.eval('tk::PlaceWindow . center')

        # Iniciar el bucle principal
        self.ventana.mainloop()

    def incrementar_valor(self, columna, fila):
        self.valores[columna][fila] += 1

    def guardar_datos(self):
        for col, columna in enumerate(self.valores):
            self.hoja_excel.write(self.fila, col * 14, f"Columna {col+1}")
            for fila, valor in enumerate(columna):
                self.hoja_excel.write(self.fila, col * 14 + fila + 1, valor)

        self.fila += 1

    def cerrar_archivo(self):
        if self.libro_excel:
            self.libro_excel.close()

if __name__ == "__main__":
    ventana = VentanaControl(2, ["Columna 1", "Columna 2"])
    ventana.abrir_ventana()
    ventana.cerrar_archivo()
