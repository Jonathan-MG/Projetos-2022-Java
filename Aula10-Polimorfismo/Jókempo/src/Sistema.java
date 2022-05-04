import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        Jogada jogada1 = sortearJogada();
        Jogada jogada2 = sortearJogada();
        //Jogada jogada3 = new Tesoura();

        String resultado = avaliaJogadas(jogada1,jogada2);
        //String resultado2 = avaliaJogadas(jogada3,jogada1);
        
        System.out.println();
        System.out.println("Entre " + jogada1.getTipo() + " e " + jogada2.getTipo() + " o resultado e: " +resultado);
        System.out.println();
        // System.out.println("Vencedor:" +resultado2);
        // System.out.println();
    }

    private static Jogada sortearJogada(){
        Jogada jogadas[] = new Jogada[3];
        jogadas[0] = new Pedra();
        jogadas[1] = new Papel();
        jogadas[2] = new Tesoura();
        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2){
        if(jogada1.verificarVenceu(jogada2))
            return jogada1.getTipo();
        if(jogada2.verificarVenceu(jogada1))
            return jogada2.getTipo();
        return "Empate";
    }
}
