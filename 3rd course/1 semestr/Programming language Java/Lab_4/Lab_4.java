import java.util. *;

public class Lab_4 {
    public static String solve(double a, double b, double c) {
        String result;
        if (a == 0) {
            result = "a=" + a + ". The coefficient a cannot be zero. There is no solution.";
        } else {
            double discriminant = b * b - 4 * c;
            if (discriminant < 0) {
                if (a < 0) {
                    result = "x = (-∞, +∞)";
                } else {
                    result = "d=" + discriminant + ". Discriminant less than zero. There are no valid solutions.";
                }
            } else {
                double sqrtDiscriminant = Math.sqrt(discriminant);
                double x1 = (-b - sqrtDiscriminant) / (2 * a);
                double x2 = (-b + sqrtDiscriminant) / (2 * a);
        
                if (a < 0) {
                    result = "x = (-∞, " + x1 + ") and (" + x2 + ", +∞)";
                } else {
                    result = "x = " + x1 + " or x = " + x2;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("a: ");
        double a = sc.nextDouble();
        System.out.print("b: ");
        double b = sc.nextDouble();
        System.out.print("c: ");
        double c = sc.nextDouble();
        System.out.println(solve(a, b, c));
        sc.close();
    }
}
