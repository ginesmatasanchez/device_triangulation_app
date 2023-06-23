"""import tkinter as tk

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
    main()"""

"""import svgwrite

# Clase para representar el plano y la visualización
class Plano:
    def __init__(self, edificio, planta, escala):
        self.edificio = edificio
        self.planta = planta
        self.escala = escala
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def dibujar_plano(self):
        dwg = svgwrite.Drawing(filename="plano.svg", debug=True)
        # Lógica para cargar y dibujar el plano SVG con la escala adecuada
        # Utiliza los atributos edificio, planta y escala para mostrar el plano correctamente
        # Dibuja los objetos almacenados en la lista de objetos
        dwg.save()

# Clase para representar un objeto en el plano
class Objeto:
    def __init__(self, nombre, coordenada_x, coordenada_y):
        self.nombre = nombre
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def mover(self, nueva_coordenada_x, nueva_coordenada_y):
        self.coordenada_x = nueva_coordenada_x
        self.coordenada_y = nueva_coordenada_y

# Clase para la base de datos
class BaseDeDatos:
    def __init__(self):
        self.datos = {}

    def agregar_dato(self, clave, valor):
        self.datos[clave] = valor

    def obtener_dato(self, clave):
        if clave in self.datos:
            return self.datos[clave]
        else:
            return None

# Clase para la gestión de alarmas
class Alarmas:
    def __init__(self):
        self.zonas_alarmadas = []
        self.objetos_en_colision = []

    def agregar_zona_alarmada(self, zona):
        self.zonas_alarmadas.append(zona)

    def agregar_objeto_en_colision(self, objeto):
        self.objetos_en_colision.append(objeto)

# Clase para representar una zona en el plano
class Zona:
    def __init__(self, nombre, coordenadas):
        self.nombre = nombre
        self.coordenadas = coordenadas

    def verificar_alarmas(self, objetos):
        for objeto in objetos:
            if self.objeto_en_zona(objeto):
                self.alarmas.agregar_objeto_en_colision(objeto)

    def objeto_en_zona(self, objeto):
        # Lógica para verificar si el objeto se encuentra dentro de las coordenadas de la zona
        return True  # Ejemplo: siempre devuelve True para simplificar

# Ejemplo de uso
def main():
    # Crear una instancia de la base de datos
    base_de_datos = BaseDeDatos()

    # Crear un objeto plano y agregar objetos a él
    plano = Plano("Edificio A", "Planta 1", 10)
    objeto1 = Objeto("Objeto 1", 50, 50)
    objeto2 = Objeto("Objeto 2", 100, 100)
    plano.agregar_objeto(objeto1)
    plano.agregar_objeto(objeto2)

    # Agregar los objetos a la base de datos
    base_de_datos.agregar_dato(objeto1.nombre, objeto1)
    base_de_datos.agregar_dato(objeto2.nombre, objeto2)

    # Realizar operaciones con los objetos
    objeto1.mover(60, 60)

    # Realizar una búsqueda de objeto por nombre
    nombre_objeto = "Objeto 2"
    objeto_encontrado = base_de_datos.obtener_dato(nombre_objeto)
    if objeto_encontrado:
        print("Objeto encontrado:", objeto_encontrado.nombre)

    # Crear una instancia de la gestión de alarmas
    alarmas = Alarmas()

    # Crear una zona y agregarla a la lista de zonas alarmadas
    coordenadas_zona = [(0, 0), (100, 0), (100, 100), (0, 100)]
    zona = Zona("Zona 1", coordenadas_zona)
    zona.alarmas = alarmas
    alarmas.agregar_zona_alarmada(zona)

    # Verificar alarmas en la zona
    objetos = [objeto1, objeto2]
    zona.verificar_alarmas(objetos)

    # Dibujar el plano
    plano.dibujar_plano()

if __name__ == "__main__":
    main()"""
    
    
    
from flask import Flask, redirect, url_for
from Pruebas2 import Pruebas2

app = Flask(__name__)
app.register_blueprint(Pruebas2, url_prefix='/admin')

@app.route('/')
def home():
        return "Hello! this is the home page <h1> HELLO!</h1>"
    
    
"""@app.route("/<name>")
def user(name):
    return f"Hello {name}!" """

"""@app.route('/admin')
def admin():
    return redirect(url_for("home"))"""
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
