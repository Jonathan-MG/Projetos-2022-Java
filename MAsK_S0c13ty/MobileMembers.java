public class MobileMembers extends Membro {

    public MobileMembers(String usuario, String email) {
        super(usuario, email, "Mobile Member");
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("Happy_C0d1ng. Maskers");
        else System.out.println("Happy Coding!");
        return null;
    }
}
