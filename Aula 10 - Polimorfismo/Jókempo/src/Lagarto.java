public class Lagarto extends Jogada {

    public Lagarto() {
        super(EnumJogadas.SPOCKY, EnumJogadas.PAPEL);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.LAGARTO;
    }
    
}
