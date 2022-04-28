public class Usuario {
    private String nome;
    private Veiculo veiculo;
    
    public Usuario(String nome) {
        this.nome = nome;
        this.veiculo = new Veiculo(null);
    }

    public String getNome() {
        return nome;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public void emprestarVeiculo(Veiculo veiculoemprestado){
        veiculo.setTipo(veiculoemprestado.getTipo());
    }

    @Override
    public String toString() {
        return "Usuario [nome=" + nome + ", veiculo=" + veiculo + "]";
    }
}
