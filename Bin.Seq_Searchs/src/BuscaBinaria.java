public class BuscaBinaria {
    public static int nComp = 0;
    public static int indice;
    public static int[] A = { 10, 12, 20, 22, 35, 37, 39, 40, 56, 70, 71, 75 };

    public static void main(String[] args) throws Exception {

        int n = 71;

        System.out.println();
        System.out.println("------ Busca Sequencial ------");

        seqSearch(n);

        if (indice != -1) {
            System.out.println("Valor encontrado na posição: " + indice);
            System.out.println("Total de comparações: " + nComp);
        } else {
            System.out.println("Valor NÃO encontrado... " + indice);
            System.out.println("Total de comparações: " + nComp);
        }

        nComp = 0;

        System.out.println();
        System.out.println("------ Busca Binária ------");

        binSearch(n, 0, A.length - 1);

        if (indice != -1) {
            System.out.println("Valor encontrado na posição: " + indice);
            System.out.println("Total de comparações: " + nComp);
        } else {
            System.out.println("Valor NÃO encontrado no array");
            System.out.println("Total de comparações: " + nComp);
        }

        System.out.println();
        
    }

    public static void seqSearch(int n) {
        for (int i = 0; i < A.length; i++) {
            if (A[i] == n) {
                nComp++;
                indice = i;
                break;
            } else {
                nComp++;
                indice = -1;
            }
        }
    }

    public static void binSearch(int item, int begin, int end) {

        int metade = (begin + end) / 2;

        if (begin > end) {
            indice = -1;
            nComp++;
            return;
        }

        if (A[metade] == item) {
            indice = metade;
            nComp++;
            return;
        }

        if (A[metade] < item) {
            nComp++;
            binSearch(item, metade + 1, end);
        }

        else {
            nComp++;
            binSearch(item, begin, metade);
        }

    }
}
