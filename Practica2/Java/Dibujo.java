mport javax.swing.*;
import java.awt.*;

public class Dibujo extends JPanel {
    private Linea linea;
    private Circulo circulo;

    public Dibujo(Linea linea, Circulo circulo) {
        this.linea = linea;
        this.circulo = circulo;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        //Aqui dibujo la linea
        g2d.setColor(Color.BLUE);
        g2d.setStroke(new BasicStroke(2));
        g2d.drawLine(
            (int) linea.getP1().getX(), (int) linea.getP1().getY(),
            (int) linea.getP2().getX(), (int) linea.getP2().getY()
        );

        //Aqui dibujo el circulo
        g2d.setColor(Color.RED);
        int radio = (int) circulo.getRadio();
        int x = (int) circulo.getCentro().getX() - radio;
        int y = (int) circulo.getCentro().getY() - radio;
        g2d.drawOval(x, y, radio * 2, radio * 2);
    }
}