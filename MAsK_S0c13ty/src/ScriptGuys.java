public class ScriptGuys extends Membro{

    public ScriptGuys(String usuario, String email) {
        super(usuario, email, "Script Guy");
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        else System.out.println("Prazer em ajudar novos amigos de código!");
        return null;
    }
}
