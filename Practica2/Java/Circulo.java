public class Circulo {
    private Punto centro;
    private float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public Punto getCentro() { return centro; }
    public float getRadio() { return radio; }

    @Override
    public String toString() {
        return "Círculo con centro " + centro + " y radio " + radio;
    }
}