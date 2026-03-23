public class Javafile {

    // Method to greet a user
    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    // Method to calculate the sum of numbers 1 to n
    public static int sumUpto(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        greet("Jibishwaran");

        int n = 10;
        int result = sumUpto(n);
        System.out.println("Sum of numbers 1 to " + n + " is: " + result);
    }
}
