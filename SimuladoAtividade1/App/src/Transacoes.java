// Nome: Jonathan Martins Gomes
// RA: 20.00862-7

public class Transacoes {
    private Conta conta;
    private double valor;

    public static void gerarQRCode(double valor, Conta conta) {
        System.out.println(conta.getId() + ";" + conta.getUsuario().getNome() + ";" + valor);
        System.out.println();
    }

}
