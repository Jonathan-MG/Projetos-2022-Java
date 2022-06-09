public class BigBrothers extends Membro {

    public BigBrothers(String usuario, String email, String funcao) {
        super(usuario, email, "Big Brother");
    }
    
    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("...");
        else System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        return null;
    }
}
