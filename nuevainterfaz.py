import tkinter as tk
from ventana_control import VentanaControl

class VentanaSeleccion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Selección de movimientos")
        self.geometry("350x250")
        self.configure(background="#F1F2A2")

        self.marco = tk.Frame(self, bg="#F1F2A2")
        self.marco.pack(expand=True, pady=20)

        self.texto = tk.Label(self.marco, text="Seleccionar número de movimientos", bg="#F1F2A2")
        self.texto.pack()

        self.var_cantidad = tk.StringVar(self)
        self.var_cantidad.set("1")  # Valor predeterminado
        self.opciones = ["1", "2", "3", "4", "5", "6"]
        self.dropdown = tk.OptionMenu(self.marco, self.var_cantidad, *self.opciones)
        self.dropdown.pack()

        self.instrucciones = ["Ingrese nombre 1", "Ingrese nombre 2", "Ingrese nombre 3", "Ingrese nombre 4", "Ingrese nombre 5", "Ingrese nombre 6"]

        self.entries_nombres = []
        for i in range(6):
            entry_nombre = tk.Entry(self.marco, width=20, foreground="gray")
            entry_nombre.insert(0, self.instrucciones[i])
            entry_nombre.bind("<FocusIn>", lambda event, index=i: self.gestionar_texto_sombra(event, index))
            entry_nombre.bind("<FocusOut>", lambda event, index=i: self.gestionar_texto_sombra(event, index))
            self.entries_nombres.append(entry_nombre)

        self.boton_aceptar = tk.Button(self, text="Aceptar", command=self.abrir_ventana_control, bg="green", fg="white", width=10)
        self.boton_aceptar.pack(pady=10)

        self.centrar_ventana()

        self.mostrar_cuadros_texto()

    def mostrar_cuadros_texto(self):
        cantidad = int(self.var_cantidad.get())
        for entry in self.entries_nombres:
            entry.pack_forget()
        for i in range(cantidad):
            self.entries_nombres[i].pack()

    def abrir_ventana_control(self):
        cantidad = int(self.var_cantidad.get())
        nombres = []
        for i in range(cantidad):
            nombres.append(self.entries_nombres[i].get())
        ventana_control = VentanaControl(cantidad, nombres)
        ventana_control.abrir_ventana()

    def gestionar_texto_sombra(self, event, index):
        if event.type == "9":  # FocusIn: El cuadro de texto ha sido seleccionado
            if self.entries_nombres[index].get() == self.instrucciones[index]:
                self.entries_nombres[index].delete(0, tk.END)
                self.entries_nombres[index].config(foreground="black")
        elif event.type == "10":  # FocusOut: El cuadro de texto ha perdido la selección
            if self.entries_nombres[index].get() == "":
                self.entries_nombres[index].insert(0, self.instrucciones[index])
                self.entries_nombres[index].config(foreground="gray")

    def centrar_ventana(self):
        self.eval('tk::PlaceWindow . center')

if __name__ == "__main__":
    ventana_seleccion = VentanaSeleccion()
    ventana_seleccion.mainloop()
