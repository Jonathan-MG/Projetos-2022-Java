import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    private int IdVeiculo = 0;
    private String Tipo;
    
    public Veiculo(String tipo) {
        this.Tipo = tipo;
        this.IdVeiculo = ThreadLocalRandom.current().nextInt(10000, 100000);
    }

    public String testar(){
        return String.format("IdVeiculo: %s - Tipo: %s", getIdVeiculo(), getTipo());
    }

    public int getIdVeiculo() {
        return IdVeiculo;
    }

    public String getTipo() {
        return Tipo;
    }

    public void setTipo(String tipo) {
        Tipo = tipo;
    }

    public void setIdVeiculo() {
        IdVeiculo = ThreadLocalRandom.current().nextInt(10000, 100000);
    }

}
