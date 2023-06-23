import tkinter as tk
from tkinter import filedialog

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Plano Arquitectónico")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.plano_image = None

        self.load_plano_image()

        self.info_label = tk.Label(self, text="Posición: ")
        self.info_label.pack()

        dibujar_punto_button = tk.Button(self, text="Dibujar Punto", command=self.dibujar_punto)
        dibujar_punto_button.pack(side=tk.BOTTOM)

    def load_plano_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.plano_image = tk.PhotoImage(file=file_path)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.plano_image)

    def dibujar_punto(self):
        x = self.obtener_coordenada_x()
        y = self.obtener_coordenada_y()

        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

    def obtener_coordenada_x(self):
        # Implementa la lógica para obtener la coordenada X desde alguna fuente
        # Por ejemplo, supongamos que se obtiene desde una entrada de texto llamada "coordenadaXEntry"
        # return int(coordenadaXEntry.get())
        return 100

    def obtener_coordenada_y(self):
        # Implementa la lógica para obtener la coordenada Y desde alguna fuente
        # Por ejemplo, supongamos que se obtiene desde una entrada de texto llamada "coordenadaYEntry"
        # return int(coordenadaYEntry.get())
        return 150

if __name__ == "__main__":
    app = Main()
    app.mainloop()
