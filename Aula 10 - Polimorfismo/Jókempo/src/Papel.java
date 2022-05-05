public class Papel extends Jogada {
    public Papel() {
        super(EnumJogadas.PEDRA, EnumJogadas.SPOCKY);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PAPEL;
    }
}
