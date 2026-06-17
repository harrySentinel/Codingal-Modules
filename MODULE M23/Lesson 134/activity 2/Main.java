import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Mind Riddler - Guess the Output!");
        System.out.println();

        int x = 10;
        int y = 3;

        System.out.println("x = " + x + ", y = " + y);
        System.out.println();

        System.out.print("What is x + y?  Your answer: ");
        int ans1 = sc.nextInt();
        System.out.println("Correct answer : " + (x + y) + (ans1 == x + y ? " ✓ Correct!" : " ✗ Wrong!"));

        System.out.print("What is x % y?  Your answer: ");
        int ans2 = sc.nextInt();
        System.out.println("Correct answer : " + (x % y) + (ans2 == x % y ? " ✓ Correct!" : " ✗ Wrong!"));

        System.out.print("What is x / y?  Your answer: ");
        int ans3 = sc.nextInt();
        System.out.println("Correct answer : " + (x / y) + (ans3 == x / y ? " ✓ Correct!" : " ✗ Wrong!"));

        sc.close();
    }
}
