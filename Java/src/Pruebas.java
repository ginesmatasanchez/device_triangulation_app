import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pruebas extends JFrame {
    private JTextField infoTextField;
    private Mapa mapa;

    public Pruebas() {
        setTitle("Mapa del Jugador");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JButton mostrarButton = new JButton("Mostrar punto en el plano");
        infoTextField = new JTextField(20);
        mapa = new Mapa();

        add(mostrarButton, BorderLayout.NORTH);
        add(mapa, BorderLayout.CENTER);
        add(infoTextField, BorderLayout.SOUTH);

        mostrarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Simulación de la posición y la planta del jugador
                int posicion = 5; // Ejemplo de posición
                int planta = 2; // Ejemplo de planta

                // Mostrar la información en el JTextField
                infoTextField.setText("Posición: " + posicion + ", Planta: " + planta);

                // Actualizar el mapa con la posición del jugador
                mapa.actualizarPosicion(posicion, planta);
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Pruebas mapa = new Pruebas();
                mapa.setVisible(true);
            }
        });
    }
}

class Mapa extends JPanel {
    private int posicionJugador;
    private int plantaJugador;
    int posicionEnPlanta;

    public Mapa() {
        setBackground(Color.WHITE);
    }

    public void actualizarPosicion(int posicion, int planta) {
        posicionJugador = posicion;
        plantaJugador = planta;
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Dibujar el mapa
        g.setColor(Color.BLACK);
        g.drawRect(50, 50, 300, 300); // Ejemplo de dibujo de un rectángulo que representa el mapa

        // Dibujar la posición del jugador
        int x = 200; // Ejemplo de coordenada x del jugador
        int y = 200; // Ejemplo de coordenada y del jugador

        // Calcular las coordenadas reales en función de la posición y la planta
        int escala = 50; // Ejemplo de escala para ajustar las coordenadas
        int offsetX = 100; // Ejemplo de desplazamiento horizontal para centrar el punto
        int offsetY = 100; // Ejemplo de desplazamiento vertical para centrar el punto

        posicionEnPlanta = posicionJugador * escala; // Ejemplo de cálculo de la posición en la planta
        int coordenadaX = x * escala + offsetX; // Ejemplo de cálculo de la coordenada x real
        int coordenadaY = y * escala + offsetY - (plantaJugador * escala); // Ejemplo de cálculo de la coordenada y real

        int radio = 5; // Ejemplo de tamaño del punto del jugador

        g.setColor(Color.RED);
        g.fillOval(coordenadaX - radio, coordenadaY - radio, 2 * radio, 2 * radio);
    }
}
