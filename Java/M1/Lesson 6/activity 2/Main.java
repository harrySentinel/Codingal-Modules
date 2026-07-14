import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // What to enter:
        // Enter a positive integer n (example: 60)
        // Output will print prime factors separated by spaces
        System.out.print("Enter a number (n): ");
        int n = scn.nextInt();

        for (int div = 2; div * div <= n; div++) {
            while (n % div == 0) {
                n = n / div;
                System.out.print(div + " ");
            }
        }
        if (n != 1) {
            System.out.print(n);
        }
    }
}
