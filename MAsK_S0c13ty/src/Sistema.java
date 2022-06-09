import java.util.ArrayList;
import java.util.List;

public class Sistema {
    public static void run(){
        String status = "Atividade Regular";
        List<Membro> MAsK_S0c13ty = new ArrayList<Membro>();
        MAsK_S0c13ty.add(new MobileMembers("KR4ud10", "Claudinhodamamae@bol.br"));
        MAsK_S0c13ty.add(new HeavyLifter("P4m3L4", "Unicorniocolorido@gmail.com"));
        MAsK_S0c13ty.add(new ScriptGuys("M4rC0s", "MarcosSmith@hotmail.com"));
        MAsK_S0c13ty.add(new BigBrothers("Th14g0", "QueriaSerThiagoLeifert@yahoo.com.br"));    
        
        System.out.println();
        ExibirMembros(MAsK_S0c13ty, status);
        mudarTurno(status);
        System.out.println();
        ExibirMembros(MAsK_S0c13ty, status);

    }

    public static void mudarTurno(String status){
        if (status == "Atividade Regular")
            status = "Atividade Extra";
        else status = "Atividade Regular";
    }

    public static void ExibirMembros(List<Membro> membros, String status){
        for (Membro membro : membros) {
            System.out.println(membro);
            membro.PostarMensagem(status);
        }
    }
}
