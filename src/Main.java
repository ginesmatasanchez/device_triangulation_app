import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Main extends JFrame {
    private BufferedImage planoImage;

    public Main() {


        // Carga el plano desde un archivo de imagen
        try {
            planoImage = ImageIO.read(new File("assets/plano-de-prueba-APPINTERIORISMO.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Agrega un panel para mostrar el plano y dibujar elementos adicionales
        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                // Dibuja el plano en el panel, escalándolo al tamaño del panel
                g.drawImage(planoImage, 0, 0, getWidth(), getHeight(), null);

                // Aquí puedes agregar código adicional para dibujar elementos en el plano

                /*
                // Ejemplo: Dibujar una línea horizontal en el plano
                g.setColor(Color.RED);
                g.drawLine(100, 100, 300, 100);

                // Ejemplo: Dibujar un rectángulo en el plano
                g.setColor(Color.BLUE);
                g.drawRect(150, 200, 200, 100);

                // Puedes agregar más código para dibujar elementos adicionales en el plano
                */
            }
        };
        getContentPane().setLayout(new BorderLayout()); // Utiliza un BorderLayout para que el panel se ajuste al tamaño del frame
        getContentPane().add(panel, BorderLayout.CENTER); // Agrega el panel al centro del BorderLayout

        pack(); // Ajusta automáticamente el tamaño del frame según el contenido
        
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Main main = new Main();
            main.setSize(800, 600);
            main.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            main.setLocationRelativeTo(null);
            main.setTitle("Plano Arquitectónico");
            main.setVisible(true);
        });
    }
}
