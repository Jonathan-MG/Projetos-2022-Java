import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static String status;

    public static void run() {
        status = "Atividade Regular";
        List<Membro> MAsK_S0c13ty = new ArrayList<Membro>();
        MAsK_S0c13ty.add(new MobileMembers("KR4ud10", "Claudinhodamamae@bol.br"));
        MAsK_S0c13ty.add(new HeavyLifter("P4m3L4", "Unicorniocolorido@gmail.com"));
        MAsK_S0c13ty.add(new ScriptGuys("M4rC0s", "MarcosSmith@hotmail.com"));
        MAsK_S0c13ty.add(new BigBrothers("Th14g0", "QueriaSerThiagoLeifert@yahoo.com.br"));

        MAsK_S0c13ty.add(new MobileMembers("P4ulu", "Paolinho@bol.br"));
        MAsK_S0c13ty.add(new HeavyLifter("K410", "Cainochao@gmail.com"));
        MAsK_S0c13ty.add(new ScriptGuys("T4b4t4", "Tabatinha@hotmail.com"));
        MAsK_S0c13ty.add(new BigBrothers("F4br1c10", "Fabri_Cio@yahoo.com.br"));

        MAsK_S0c13ty.add(new MobileMembers("T4m14", "TamiaRata@bol.br"));
        MAsK_S0c13ty.add(new HeavyLifter("G30rg1", "OTaldoGeorge@gmail.com"));
        MAsK_S0c13ty.add(new ScriptGuys("Gu1", "Guilherme_Mais_Bonito@hotmail.com"));
        MAsK_S0c13ty.add(new BigBrothers("K4r0l1n2", "Karolzinha@yahoo.com.br"));

        System.out.println();
        System.out.println("Status Atual: " + status);
        System.out.println();
        System.out.println("---------------------------------------------------------------------");
        ExibirMembros(MAsK_S0c13ty, status);
        
        mudarTurno();
        System.out.println("Status Atual: " + status);
        System.out.println();
        System.out.println("---------------------------------------------------------------------");
        ExibirMembros(MAsK_S0c13ty, status);

        mudarTurno();
        MAsK_S0c13ty.remove(1);
        MAsK_S0c13ty.remove(5);
        System.out.println("Status Atual: " + status);
        System.out.println();
        System.out.println("---------------------------------------------------------------------");
        ExibirMembros(MAsK_S0c13ty, status);
        System.out.println();
    }

    // public static String GerarTurno() {
    //     int turno = ThreadLocalRandom.current().nextInt(0, 2);
    //     if (turno == 0) {
    //         return "Atividade Regular";
    //     } else {
    //         return "Atividade Extra";
    //     }
    // }

    public static void mudarTurno() {
        if (status.equals("Atividade Regular")) {
            Sistema.status = "Atividade Extra";
        } else {
            Sistema.status = "Atividade Regular";
        }
    }

    public static void ExibirMembros(List<Membro> membros, String status) {
        for (Membro membro : membros) {
            System.out.println(membro);
            membro.PostarMensagem(status);
        }
    }
}
