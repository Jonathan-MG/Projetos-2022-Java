public class Aplicacao {
    public static void run(){
        Usuario usuario1 = new Usuario("Jonathan");
        System.out.println(usuario1.getVeiculo().testar());
        
        usuario1.emprestarVeiculo(new Carro("carro"));
        System.out.println(usuario1.getVeiculo().testar());
        
        usuario1.emprestarVeiculo(new Moto("moto"));
        System.out.println(usuario1.getVeiculo().testar());
    }
}
