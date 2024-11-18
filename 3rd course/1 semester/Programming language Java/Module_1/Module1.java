public class Module1 {
    public static void main(String[] args) {
        // 1
        System.out.println("1:");
        System.out.println("This is mdule 1");
        System.out.println();

        // 2
        System.out.println("2:");
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        for (int i = numbers.length - 1; i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        System.out.println();

        // 3
        System.out.println("3:");
        String sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
        String[] words = sentence.split(" ");
        String lastName = "BOIKO";
        for (int i = 0; i < words.length; i += 3) {
            words[i] = lastName;
        }
        String newSentence = String.join(" ", words);
        System.out.println(sentence);
        System.out.println(newSentence);
        System.out.println();

        // 4-5
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

        Circle circle = new Circle(5.0);
        circle.setColor("Red");
        System.out.println("Circle area: " + circle.area);
        System.out.println("Circle color: " + circle.getColor());

        Rectangle rectangle = new Rectangle(4.0, 3.0);
        rectangle.setColor("Blue");
        System.out.println("Rectangle area: " + rectangle.area);
        System.out.println("Rectangle color: " + rectangle.getColor());
    }
}