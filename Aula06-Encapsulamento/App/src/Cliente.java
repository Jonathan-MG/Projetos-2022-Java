public class Cliente {
    private String cpf;
    private String nome;
    private String email;
    private Conta conta;

    public Cliente(String nome, String cpf, String email, Conta conta) {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        this.conta = conta;
    }

    public void visualizarCliente() {
        System.out.println("Dados do cliente:");
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println("e-mail: " + email);
        System.out.println("Conta: " + conta);

    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public String getEmail() {
        return email;
    }

    public Conta getConta() {
        return conta;
    }

}
