public class Caneta {
    // Características da caneta - seus atributos
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_INICIAL = 100;

    void inciarCaneta(String cor, String modelo, double ponta) {
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_INICIAL;
    }

    String mostrarDados() {
        return " Modelo: " + this.modelo + " - Cor: " + this.cor + " - Ponta: " + this.ponta + " - Carga: "
                + this.carga;
    }

    // Comportamentos da caneta - seus métodos
    void escrever(String texto) {
        for (int i = 0; i < texto.length(); i++) {
            if (this.carga > 0) {
                System.out.print(texto.charAt(i));
                this.carga -= 1;
            } else {
                System.out.println("\nCANETA SEM CARGA");
                break;
            }
        }
        System.out.println();
    }
}