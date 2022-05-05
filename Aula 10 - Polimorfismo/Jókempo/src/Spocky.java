public class Spocky extends Jogada {

    public Spocky() {
        super(EnumJogadas.TESOURA,EnumJogadas.PEDRA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.SPOCKY;
    }
    
}
