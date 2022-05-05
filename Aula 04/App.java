public class App {
    public static void main(String[] args) {
        // Declara e Instancia um objeto Caneta
        Caneta c1 = new Caneta();
        c1.inciarCaneta("Azul", "BIC", 1.0);

        Caneta c2 = new Caneta();
        c2.inciarCaneta("Vermelha", "Stabillo", 0.4);

        c1.escrever("\nOlha a véia atravessando a rua....");
        c2.escrever("\nIhhhhhh trouxa, troleiiii!");
        c2.escrever("\nIhhhhhh trouxa, troleiiii!");
        c2.escrever("\nIhhhhhh trouxa, troleiiii!");
        c2.escrever("\nIhhhhhh trouxa, troleiiii!");
        System.out.println();

    }
}
