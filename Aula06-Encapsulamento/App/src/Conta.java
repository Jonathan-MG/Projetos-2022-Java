public class Conta {
    // Atributos da classe
    private int numero;
    private String titular;
    private double saldo;
    private String cpf;

    public Conta(int numero){
        this.numero = numero;
        saldo = 0;
    }

    // Métodos da classe
    public void visualizarSaldo() {
        System.out.println("Saldo atual na conta " + numero + ": R$ " + saldo);
        System.out.println();
    }

    public boolean depositar(double valor) {
        // if (valor > 0) {
        // saldo = saldo + valor;
        // return true;
        // } else {
        // return false;
        // }
        if (valor < 0)
            return false;
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor) {
        // if (valor <= saldo) {
        // saldo = saldo - valor;
        // } else {
        // System.out.println("Saldo insuficiente.\n");
        // }
        if (valor > saldo)
            return false;
        if (valor < 0)
            return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferirDinheiro(double valor, Conta destino) {
        if (!sacar(valor))
            return false;
        if (!destino.depositar(valor))
            return false;
        return true;
    }

}
