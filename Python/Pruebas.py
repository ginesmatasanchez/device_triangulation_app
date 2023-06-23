import tkinter as tk

class Pruebas(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mapa del Jugador")
        self.geometry("400x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        mostrar_button = tk.Button(self, text="Mostrar punto en el plano", command=self.mostrar_punto)
        self.info_text_field = tk.Entry(self, width=20)
        self.mapa = Mapa()

        mostrar_button.pack(side=tk.TOP)
        self.mapa.pack()
        self.info_text_field.pack(side=tk.BOTTOM)

    def mostrar_punto(self):
        # Simulación de la posición y la planta del jugador
        posicion = 5  # Ejemplo de posición
        planta = 2  # Ejemplo de planta

        # Mostrar la información en el Entry
        self.info_text_field.delete(0, tk.END)
        self.info_text_field.insert(tk.END, "Posición: " + str(posicion) + ", Planta: " + str(planta))

        # Actualizar el mapa con la posición del jugador
        self.mapa.actualizar_posicion(posicion, planta)

    def on_close(self):
        self.destroy()

class Mapa(tk.Canvas):
    def __init__(self):
        super().__init__(width=300, height=300, bg="white")

        self.posicion_jugador = 0
        self.planta_jugador = 0
        self.posicion_en_planta = 0

    def actualizar_posicion(self, posicion, planta):
        self.posicion_jugador = posicion
        self.planta_jugador = planta
        self.delete("all")
        self.dibujar_mapa()
        self.dibujar_posicion_jugador()

    def dibujar_mapa(self):
        self.create_rectangle(50, 50, 350, 350, outline="black")

    def dibujar_posicion_jugador(self):
        x = 200  # Ejemplo de coordenada x del jugador
        y = 200  # Ejemplo de coordenada y del jugador

        escala = 50  # Ejemplo de escala para ajustar las coordenadas
        offset_x = 100  # Ejemplo de desplazamiento horizontal para centrar el punto
        offset_y = 100  # Ejemplo de desplazamiento vertical para centrar el punto

        self.posicion_en_planta = self.posicion_jugador * escala  # Ejemplo de cálculo de la posición en la planta
        coordenada_x = x * escala + offset_x  # Ejemplo de cálculo de la coordenada x real
        coordenada_y = y * escala + offset_y - (self.planta_jugador * escala)  # Ejemplo de cálculo de la coordenada y real

        radio = 5  # Ejemplo de tamaño del punto del jugador

        self.create_oval(coordenada_x - radio, coordenada_y - radio, coordenada_x + radio, coordenada_y + radio, fill="red")

def main():
    pruebas = Pruebas()
    pruebas.mainloop()

if __name__ == "__main__":
    main()
