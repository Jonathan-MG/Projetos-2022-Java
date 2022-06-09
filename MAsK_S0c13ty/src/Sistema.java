import java.util.ArrayList;
import java.util.List;

import javax.swing.event.MenuDragMouseEvent;

public class Sistema {
    public static void run(){
        String status = "Atividade Regular";
        List<Membro> MAsK_S0c13ty = new ArrayList<Membro>();
        //MAsK_S0c13ty.add(new )

        
        mudarTurno(status);

    }

    public static void mudarTurno(String status){
        if (status == "Atividade Regular")
            status = "Atividade Extra";
        else status = "Atividade Regular";
    }
}
