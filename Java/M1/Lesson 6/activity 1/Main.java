import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // What to enter:
        // First enter t = number of test cases
        // Then enter t numbers (n), one per line
        System.out.print("Enter number of test cases (t): ");
        int t = scn.nextInt();

        for (int i = 1; i <= t; i++) {
            System.out.print("Enter number " + i + ": ");
            int n = scn.nextInt();

            int count = 0;
            for (int div = 2; div * div <= n; div++) {
                if (n % div == 0) {
                    count++;
                    break;
                }
            }

            if (n <= 1) {
                System.out.println("not prime");
            } else if (count == 0) {
                System.out.println("prime");
            } else {
                System.out.println("not prime");
            }
        }
    }
}
