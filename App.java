public class App {
    public static void main(String[] args) {
        //Declara e Instancia um objeto Caneta
        Caneta c1 = new Caneta();
        c1.modelo = "BIC";
        c1.cor = "AZUL";
        c1.carga = 100;
        c1.ponta = 1.0;
        System.out.println("Minha caneta:"+c1.modelo);
        System.out.println("Minha caneta:"+c1.cor);
        System.out.println("Minha caneta:"+c1.carga);
        System.out.println("Minha caneta:"+c1.ponta);
    }
}