import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // What to enter:
        // Enter an integer n (example: 5)
        // Program will calculate: 1 + 2 + 3 + ... + n
        System.out.print("Enter a number (n): ");

        int n = scn.nextInt();
        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += i;
        }

        System.out.println("Sum till " + n + " is " + sum + ".");
    }
}
