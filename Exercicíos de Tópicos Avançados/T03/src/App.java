import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(Func(n));
        System.out.println();

        Scanner in2 = new Scanner(System.in);
        int n2 = in2.nextInt();
        System.out.println(Func(n2));
        System.out.println();

        Scanner in3 = new Scanner(System.in);
        int n3 = in3.nextInt();
        System.out.println(Func(n3));
        System.out.println();

        Scanner in4 = new Scanner(System.in);
        int n4 = in4.nextInt();
        System.out.println(Func(n4));
        System.out.println();

        Scanner in5 = new Scanner(System.in);
        int n5 = in5.nextInt();
        System.out.println(Func(n5));
        System.out.println();

        Scanner in6 = new Scanner(System.in);
        int n6 = in6.nextInt();
        System.out.println(Func(n6));
        System.out.println();

        Scanner in7 = new Scanner(System.in);
        int n7 = in7.nextInt();
        System.out.println(Func(n7));
        System.out.println();

        Scanner in8 = new Scanner(System.in);
        int n8 = in8.nextInt();
        System.out.println(Func(n8));
        System.out.println();

        Scanner in9 = new Scanner(System.in);
        int n9 = in9.nextInt();
        System.out.println(Func(n9));
        System.out.println();

        Scanner in10 = new Scanner(System.in);
        int n10 = in10.nextInt();
        System.out.println(Func(n10));
        System.out.println();

        in.close();
        in2.close();
        in3.close();
        in4.close();
        in5.close();
        in6.close();
        in7.close();
        in8.close();
        in9.close();
        in10.close();

    }

    public static int Func(int n) {
        int i = 1;
        int m = 0;
        while (i <= n) {
            // for (i = 1; i <= n; i++)
            // for (int j = i; j <= n; j++){
            m = m + 1; // Linha 1
            i = i * 2;
        }
        return m;
    }
}
