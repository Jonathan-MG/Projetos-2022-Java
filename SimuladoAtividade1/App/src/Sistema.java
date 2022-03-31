// Nome: Jonathan Martins Gomes
// RA: 20.00862-7

public class Sistema {
    public void run(){
        Usuario user1 = new Usuario("Jonas", "myamzpsw", "jonasotaldobilu@ig.com.br");
        Conta conta1 = new Conta("1", user1);
        System.out.println(conta1);
        Transacoes.gerarQRCode(500, conta1);
}
}