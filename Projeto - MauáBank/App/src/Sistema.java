import java.time.LocalDate;

public class Sistema {
    public void run(){
        Cliente cliente = new Cliente("Jonathan", "435.242.434-36", "jonathanmgomes10@hotmail.com");
        Conta conta = new Conta(cliente, 445682);
        conta.depositar(300);
        System.out.println(conta);

        Titulo steam = new Titulo(250, LocalDate.of(2022,03,30), 5);
        
        System.out.println(conta);
    }

    boolean pagarTitulo(Titulo titulo, Conta conta){
        double valorPagar;
        LocalDate dataTitulo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        if (dataTitulo.compareTo(hoje) > 0 ){
            valorPagar = titulo.getValor();
        } else{
            // TERMINAR NA PRÓXIMA AULA
        }
        
        return true;
    }
}
