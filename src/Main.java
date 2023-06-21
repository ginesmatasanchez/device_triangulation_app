import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
//import org.json.*;


public class Main extends JFrame{
    
    private BufferedImage planoImage;
    private JPanel panel;

    public Main() {


        // Carga el plano desde un archivo de imagen
        try {
            planoImage = ImageIO.read(new File("assets/plano-de-prueba-APPINTERIORISMO.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Agrega un panel para mostrar el plano y dibujar elementos adicionales
        panel = new JPanel() {
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



        // Crear un botón para dibujar el punto
        JButton dibujarPuntoButton = new JButton("Dibujar Punto");
        dibujarPuntoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Obtener las coordenadas desde alguna fuente, como un campo de texto o un servidor
                int x = obtenerCoordenadaX();
                int y = obtenerCoordenadaY();

                // Ajustar las coordenadas dentro de los límites del plano
                if (x < 0) x = 0;
                if (x >= planoImage.getWidth()) x = planoImage.getWidth() - 1;
                if (y < 0) y = 0;
                if (y >= planoImage.getHeight()) y = planoImage.getHeight() - 1;

                // Realizar acciones con las coordenadas ajustadas, por ejemplo, dibujar un punto
                dibujarPunto(x, y);
            }
        });

        // Agregar el botón al JFrame
        getContentPane().add(dibujarPuntoButton, BorderLayout.SOUTH);

        // Mostrar el JFrame
        pack();
        setVisible(true);
    }

    private int obtenerCoordenadaX() {
        // Implementar la lógica para obtener la coordenada X desde alguna fuente (campo de texto, servidor, etc.)
        // Por ejemplo, supongamos que se obtiene desde un campo de texto llamado "coordenadaXTextField"
        // return Integer.parseInt(coordenadaXTextField.getText());
        //return 0; // Valor de ejemplo
        return 100;
    }

    private int obtenerCoordenadaY() {
        // Implementar la lógica para obtener la coordenada Y desde alguna fuente (campo de texto, servidor, etc.)
        // Por ejemplo, supongamos que se obtiene desde un campo de texto llamado "coordenadaYTextField"
        // return Integer.parseInt(coordenadaYTextField.getText());
        //return 0; // Valor de ejemplo
        return 150;
    }

    /*private void dibujarPunto(int x, int y) {
        // Crear un objeto Graphics2D para dibujar en el JLabel
        Graphics2D g2d = (Graphics2D) planoImage.getGraphics();

        // Dibujar un punto en las coordenadas especificadas
        g2d.setColor(Color.RED);
        g2d.fillOval(x - 2, y - 2, 50, 50);

        // Liberar recursos del objeto Graphics2D
        g2d.dispose();
    }*/

    private void dibujarPunto(int x, int y) {
        // Obtener el objeto Graphics del panel
        Graphics g = panel.getGraphics();

        // Dibujar un punto en las coordenadas especificadas
        g.setColor(Color.RED);
        g.fillOval(x - 2, y - 2, 50, 50);
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
