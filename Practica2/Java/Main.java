import javax.swing.*;
public class Main {

    public static void main(String[] args) {
        
        Punto p1 = new Punto(50, 50);
        Punto p2 = new Punto(200, 200);
        Punto centro = new Punto(150, 100);

        
        Linea linea = new Linea(p1, p2);
        Circulo circulo = new Circulo(centro, 50);

        
        System.out.println(linea);
        System.out.println(circulo);

        
        JFrame frame = new JFrame("Dibujo con Java");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setContentPane(new Dibujo(linea, circulo));
        frame.setVisible(true);