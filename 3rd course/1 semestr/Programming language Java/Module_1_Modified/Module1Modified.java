import java.util. *;

public class Module1Modified {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1
        System.out.println("1:");
        System.out.print("Enter a string you want to print: ");
        String string = sc.nextLine();
        System.out.println("Printed string: " + string);
        System.out.println();

        // 2
        System.out.println("2:");
        System.out.print("Enter a quantity of numbers you want to print backwards: ");
        int quantity = sc.nextInt();
        int[] numbers = new int[quantity];
        System.out.print("Created array of " + quantity + " numbers: ");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = i + 1;
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        System.out.println();
        System.out.print("Reversed array of " + quantity + " numbers: ");
        for (int i = numbers.length - 1; i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        System.out.println();

        // 3
        System.out.println("3:");
        System.out.print("Enter a sentence you want to change or 'Lorem' to use the default one: ");
        sc.nextLine();
        String sentence = sc.nextLine();
        if (sentence.equals("Lorem") || sentence.equals("")) {
            sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent bland";
            }
        String[] words = sentence.split(" ");
        String lastName = "BOIKO";
        for (int i = 2; i < words.length; i += 3) {
            words[i] = lastName;
        }
        String newSentence = String.join(" ", words);
        System.out.println();
        System.out.println("Initial sentence: ");
        System.out.println(sentence);
        System.out.println();
        System.out.println("Changed sentence: ");
        System.out.println(newSentence);
        System.out.println();

        // 4
        System.out.println("4-5:");
        abstract class Shape {
            protected String color;
            protected double area;

            public abstract double calculateArea();

            public void setColor(String color) {
                this.color = color;
            }

            public String getColor() {
                return color;
            }
        }

        // 5
        class Circle extends Shape {
            private double radius;

            public Circle(double radius) {
                this.radius = radius;
                this.area = calculateArea();
            }

            @Override
            public double calculateArea() {
                return Math.PI * radius * radius;
            }
        }

        class Rectangle extends Shape {
            private double width;
            private double height;

            public Rectangle(double width, double height) {
                this.width = width;
                this.height = height;
                this.area = calculateArea();
            }

            @Override
            public double calculateArea() {
                return width * height;
            }
        }

        
        System.out.println("To create a circle - enter: ");
        System.out.print("radius: ");
        double inputRadius = sc.nextDouble();
        System.out.print("color: ");
        sc.nextLine();
        String inputColor = sc.nextLine();
        Circle circle = new Circle(inputRadius);
        circle.setColor(inputColor);        
        System.out.println();       
        System.out.println();        
        System.out.println("Information about the circle:");
        System.out.println("Circle area: " + circle.area);
        System.out.println("Circle color: " + circle.getColor());
        
        System.out.println();       
        System.out.println();  
        System.out.println("To create a rectangle - enter: ");
        System.out.print("width: ");
        double inputWidth = sc.nextDouble();
        System.out.print("height: ");
        double inputHeight = sc.nextDouble();
        System.out.print("color: ");
        sc.nextLine();
        inputColor = sc.nextLine();
        Rectangle rectangle = new Rectangle(inputWidth, inputHeight);
        rectangle.setColor(inputColor);
        System.out.println();       
        System.out.println();        
        System.out.println("Information about the rectangle:");
        System.out.println("Rectangle area: " + rectangle.area);
        System.out.println("Rectangle color: " + rectangle.getColor());

        sc.close();
    }
}