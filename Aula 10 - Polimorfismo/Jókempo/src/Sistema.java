import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        Jogada jogada1 = sortearJogada();
        Jogada jogada2 = sortearJogada();
        EnumJogadas resultado = avaliaJogadas(jogada1,jogada2);
        System.out.println();
        System.out.println("Entre " + jogada1.getTipo() + " e " + jogada2.getTipo() + " o resultado e: " +resultado);
        System.out.println();

        Jogada jogada3 = sortearJogada();
        Jogada jogada4 = sortearJogada();
        EnumJogadas resultado1 = avaliaJogadas(jogada3,jogada4);  
        System.out.println();
        System.out.println("Entre " + jogada3.getTipo() + " e " + jogada4.getTipo() + " o resultado e: " +resultado1);
        System.out.println();

        Jogada jogada5 = sortearJogada();
        Jogada jogada6 = sortearJogada();
        EnumJogadas resultado2 = avaliaJogadas(jogada5,jogada6);
        System.out.println();
        System.out.println("Entre " + jogada5.getTipo() + " e " + jogada6.getTipo() + " o resultado e: " +resultado2);
        System.out.println();
    }

    private static Jogada sortearJogada(){
        Jogada jogadas[] = new Jogada[5];
        jogadas[0] = new Pedra();
        jogadas[1] = new Papel();
        jogadas[2] = new Tesoura();
        jogadas[3] = new Spocky();
        jogadas[4] = new Lagarto();
        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static EnumJogadas avaliaJogadas(Jogada jogada1, Jogada jogada2){
        if(jogada1.verificarVenceu(jogada2))
            return jogada1.getTipo();
        if(jogada2.verificarVenceu(jogada1))
            return jogada2.getTipo();
        return EnumJogadas.EMPATE;
    }
}
