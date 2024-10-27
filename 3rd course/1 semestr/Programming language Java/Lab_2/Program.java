import java.io. *;
import java.util. *;

public class Program {
    public static void main(String[] s) {
        Scanner sc = new Scanner(System.in);
        System.out.print("a: ");
        double a = sc.nextDouble();
        System.out.print("b: ");
        double b = sc.nextDouble();
        System.out.print("x: ");
        double x = sc.nextDouble();

        double R = Math.pow(x, 2) * (x + 1) / (b - Math.pow(Math.sin(x + a), 2));
        System.out.println("R = " + R);

        sc.close();
    }

}