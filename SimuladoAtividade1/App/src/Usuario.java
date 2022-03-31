// Nome: Jonathan Martins Gomes
// RA: 20.00862-7

public class Usuario {
    private String nome;
    private String senha;
    private String email;

    public Usuario(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }

    public void visualizarUsuario() {
        System.out.println("Dados do usuário:");
        System.out.println("Nome: " + nome);
        System.out.println("e-mail: " + email);
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }
}
