public class Conta {
    // Atributos da classe
    int numero;
    String titular;
    double saldo;
    String cpf;

    // Métodos da classe
    void visualizarSaldo() {
        System.out.println("Saldo atual na conta " + numero + ": R$ " + saldo);
        System.out.println();
    }

    boolean depositar(double valor) {
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

    boolean sacar(double valor) {
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

    boolean transferirDinheiro(double valor, Conta destino) {
        if (!sacar(valor))
            return false;
        if (!destino.depositar(valor))
            return false;
        return true;
    }

}
