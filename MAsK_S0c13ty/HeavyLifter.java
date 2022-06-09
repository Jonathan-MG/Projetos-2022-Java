public class HeavyLifter extends Membro {

    public HeavyLifter(String usuario, String email, String funcao) {
        super(usuario, email, "Heavy Lifter");
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        else System.out.println("Podem contar conosco!");
        return null;
    }
}
