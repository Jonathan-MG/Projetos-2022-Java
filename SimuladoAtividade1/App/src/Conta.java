// Nome: Jonathan Martins Gomes
// RA: 20.00862-7

public class Conta {
    private String idConta;
    private double saldo;
    private Usuario usuario;

    public Conta (String idConta, Usuario usuario){
        this.usuario = usuario;
        this.idConta = idConta;
        saldo = 0;
    }

    public Usuario getUsuario(){
        return usuario;
    }
    
    public double getSaldo (){
        return this.saldo;
    }

    public String getId (){
        return this.idConta;
    }

    public String visualizarSaldo() {
        return String.format("R$ %.2f", saldo);
    }
    
    public String toString(){
        return "\n" + " Conta Numero: " + idConta + "\n Cliente: " + usuario.getNome() + "\n e-mail: " + usuario.getEmail() + "\n Saldo: " + visualizarSaldo() + "\n";
    }
}