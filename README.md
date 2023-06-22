# device_triangulation_app
Aplicación Java para triangular la posición de un aparato, dentro de un plano 2D (importado previamente).

Esquema gráfico de estrutura de datos:

-https://www.goconqr.com/es-ES/flowchart/13318321/sin-titulo

Repos interesantes:

-https://github.com/ajnas/WiFiPS

-https://github.com/themadcreator/delaunay/tree/master

(posible uso del algoritmo Delauny(?))



-https://github.com/aubruz/ips

(\app\src\main\java\com\mse\ips\lib\Tools.java interesante linea 71-83, conversion de pixeles a metros)

-https://github.com/Makerfabs/Makerfabs-ESP32-UWB

(repo ESP32 UWB Indoor Positioning)


Links interesantes:

-https://www.makerfabs.cc/article/esp32-uwb-indoor-positioning-test.html

-https://www.youtube.com/watch?v=rd5qukiDjys

-https://www.youtube.com/watch?v=-GNkobAxao0




# Pasos generales:

1. Diseño del plano y la interfaz de usuario:
   - Define cómo se representará el plano de la sala y las plantas en la interfaz de usuario. Puedes utilizar una biblioteca gráfica como Swing o JavaFX para crear los elementos visuales necesarios.

2. Obtención de datos:
   - Implementa la lógica para obtener los datos necesarios. Puedes utilizar una fuente de datos, como un archivo o una base de datos, que contenga la información de las salas y las plantas.

3. Triangulación de la posición:
   - Implementa el algoritmo de triangulación para determinar la posición dentro del plano de la sala. Hay diferentes enfoques para realizar esto, como trilateración o multilateración. La elección del algoritmo dependerá de la disponibilidad de puntos de referencia o balizas dentro de la sala.

4. Cálculo de la posición:
   - Utiliza los datos obtenidos y el algoritmo de triangulación para calcular la posición dentro del plano de la sala. Considera las coordenadas x, y y z si hay múltiples plantas.

5. Visualización de los resultados:
   - Muestra los resultados de la triangulación en la interfaz de usuario. Puedes resaltar la posición en el plano de la sala o mostrar las coordenadas obtenidas.

Recuerda que estos son solo pasos generales y el proceso de desarrollo puede variar según tus requisitos específicos. También puedes considerar el uso de bibliotecas adicionales que faciliten la implementación de la triangulación, como Apache Commons Math o JTS Topology Suite.

------------------------------------------------

# Ejemplo:

1. Diseño del plano y la interfaz de usuario:
```java
import javax.swing.*;

public class PlanoSalaApp extends JFrame {
    // Aquí puedes definir los elementos visuales, como paneles, botones, etc.

    public PlanoSalaApp() {
        // Configuración de la interfaz de usuario

        // Agregar los elementos visuales al marco
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            PlanoSalaApp app = new PlanoSalaApp();
            app.setVisible(true);
        });
    }
}
```

2. Obtención de datos:
```java
import java.util.ArrayList;
import java.util.List;

public class SalaPlantaData {
    // Aquí puedes implementar la lógica para obtener los datos de las salas y las plantas

    public static List<Sala> obtenerSalas() {
        // Implementa la lógica para obtener la información de las salas
        // Puede ser desde un archivo, una base de datos, etc.

        List<Sala> salas = new ArrayList<>();
        // Agrega las salas a la lista
        return salas;
    }

    public static List<Planta> obtenerPlantas() {
        // Implementa la lógica para obtener la información de las plantas

        List<Planta> plantas = new ArrayList<>();
        // Agrega las plantas a la lista
        return plantas;
    }
}

public class Sala {
    private String nombre;
    private double x;
    private double y;

    // Getters y setters
}

public class Planta {
    private int numero;
    private String nombre;

    // Getters y setters
}
```

3. Triangulación de la posición:
```java
public class Triangulacion {
    public static Posicion triangularPosicion(List<Sala> salas, List<Planta> plantas, String salaSeleccionada, int plantaSeleccionada) {
        // Implementa aquí el algoritmo de triangulación
        // Utiliza la información de las salas y las plantas para determinar la posición

        double x = 0.0; // Coordenada x calculada
        double y = 0.0; // Coordenada y calculada
        double z = 0.0; // Coordenada z calculada si hay múltiples plantas

        return new Posicion(x, y, z);
    }
}

public class Posicion {
    private double x;
    private double y;
    private double z;

    // Constructor y getters
}
```

4. Cálculo de la posición:
```java
// En el controlador de la interfaz de usuario o donde sea apropiado
List<Sala> salas = SalaPlantaData.obtenerSalas();
List<Planta> plantas = SalaPlantaData.obtenerPlantas();
String salaSeleccionada = "Sala1";
int plantaSeleccionada = 1;

Posicion posicion = Triangulacion.triangularPosicion(salas, plantas, salaSeleccionada, plantaSeleccionada);

// Haz uso de la posición calculada como desees
System.out.println("La posición calculada es: " + posicion.getX() + ", " + posicion.getY() + ", " + posicion.getZ());
```

-----------------------------------------
# JavaFX
Representar visualmente la posición triangulada como un punto en un plano 2D importado previamente, puedes utilizar una biblioteca gráfica como JavaFX para mostrar el plano y el punto en la interfaz de usuario. 

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.stage.Stage;

import java.util.List;

public class PlanoSalaApp extends Application {
    private static final double WIDTH = 800; // Ancho de la ventana
    private static final double HEIGHT = 600; // Alto de la ventana

    private Pane root;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        root = new Pane();
        Scene scene = new Scene(root, WIDTH, HEIGHT);

        List<Sala> salas = SalaPlantaData.obtenerSalas();
        List<Planta> plantas = SalaPlantaData.obtenerPlantas();
        String salaSeleccionada = "Sala1";
        int plantaSeleccionada = 1;

        Posicion posicion = Triangulacion.triangularPosicion(salas, plantas, salaSeleccionada, plantaSeleccionada);

        importarPlano(); // Método para importar y mostrar el plano en el Pane

        dibujarPunto(posicion.getX(), posicion.getY()); // Dibuja el punto en las coordenadas calculadas

        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void importarPlano() {
        // Lógica para importar y mostrar el plano en el Pane
        // Puedes utilizar JavaFX para cargar la imagen del plano y agregarla al Pane
        // Por ejemplo:
        // Image planoImage = new Image("ruta_del_plano.png");
        // ImageView planoImageView = new ImageView(planoImage);
        // root.getChildren().add(planoImageView);
    }

    private void dibujarPunto(double x, double y) {
        // Dibuja un punto en las coordenadas especificadas en el Pane
        Circle punto = new Circle(x, y, 5, Color.RED);
        root.getChildren().add(punto);
    }
}
```

Recuerda reemplazar `"ruta_del_plano.png"` con la ruta y el nombre de tu archivo de imagen del plano.

En este ejemplo, se utiliza JavaFX para crear una ventana (`Stage`) y un contenedor (`Pane`) donde se mostrará el plano y el punto. El método `importarPlano()` es donde puedes implementar la lógica para cargar y mostrar la imagen del plano dentro del `Pane`. Luego, el método `dibujarPunto()` se utiliza para dibujar un punto rojo en las coordenadas calculadas dentro del `Pane`.




# Algoritmo Delaunay para triangular la posicion

Para utilizar el algoritmo de triangulación de Delaunay y triangular la posición en el plano, necesitarás una biblioteca que implemente dicho algoritmo. Existen varias opciones disponibles, pero una popular es la biblioteca JDT (Java Delaunay Triangulation).

Aquí tienes un ejemplo básico de cómo usar la biblioteca JDT en tu aplicación Java:

1. Agregar la dependencia de JDT a tu proyecto. Puedes agregarlo a tu archivo de configuración de Maven o Gradle, dependiendo de tu sistema de construcción. Aquí está un ejemplo para Maven:

```xml
<dependencies>
    <dependency>
        <groupId>org.saintandreas</groupId>
        <artifactId>jdt-core</artifactId>
        <version>1.0.1</version>
    </dependency>
</dependencies>
```

2. Importar las clases necesarias:

```java
import org.saintandreas.math.Vector2f;
import org.saintandreas.math.triangulation.Delaunay;
```

3. Triangular la posición utilizando el algoritmo de Delaunay:

```java
// Supongamos que tienes una lista de objetos Sala con coordenadas x e y
List<Sala> salas = SalaPlantaData.obtenerSalas();
String salaSeleccionada = "Sala1";

// Obtén las salas relevantes para la triangulación
List<Sala> salasTriangulacion = salas.stream()
        .filter(sala -> sala.getNombre().equals(salaSeleccionada))
        .collect(Collectors.toList());

// Crea una lista de puntos en formato Vector2f para la triangulación de Delaunay
List<Vector2f> puntos = new ArrayList<>();
for (Sala sala : salasTriangulacion) {
    puntos.add(new Vector2f((float) sala.getX(), (float) sala.getY()));
}

// Ejecuta la triangulación de Delaunay
Delaunay triangulacion = new Delaunay();
triangulacion.triangulate(puntos);

// Obtén los triángulos resultantes
List<Vector2f[]> triangulos = triangulacion.getTriangles();

// Aquí puedes realizar acciones con los triángulos resultantes, como dibujarlos en el plano
for (Vector2f[] triangulo : triangulos) {
    // Cada Vector2f representa un punto en el plano
    Vector2f punto1 = triangulo[0];
    Vector2f punto2 = triangulo[1];
    Vector2f punto3 = triangulo[2];

    // Realiza acciones con los puntos del triángulo, como dibujar líneas
    // por ejemplo, utilizando una biblioteca gráfica como JavaFX
}
```

Recuerda adaptar este código según tu estructura de datos y requisitos específicos. La biblioteca JDT proporciona más funcionalidades, como la posibilidad de agregar restricciones o bordes para la triangulación. Consulta la documentación de la biblioteca JDT para obtener más información sobre sus características y opciones avanzadas.
