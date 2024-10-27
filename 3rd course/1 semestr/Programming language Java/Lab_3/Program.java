import java.util. *;

public class Program {
    public static void main(String[] args) {
        int[] numbers = new int[3];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < numbers.length; i++) {
            System.out.print("Enter a number for array element " + (i + 1) + ": ");
            numbers[i] = sc.nextInt();
        }
        System.out.println("The array elements are:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + ", ");
        }
        System.out.println();
        int counter = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] >= 0) {
                counter += 1;
            }
        }
        System.out.println("The number of positive elements in the array is: " + counter);
        
        sc.close();
    }    
}