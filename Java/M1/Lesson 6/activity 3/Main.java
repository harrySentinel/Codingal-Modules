import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // What to enter:
        // Enter two integers: low and high (example: 10 30)
        // Program prints all prime numbers between low and high (inclusive)
        System.out.print("Enter low: ");
        int low = sc.nextInt();

        System.out.print("Enter high: ");
        int high = sc.nextInt();

        for (int n = low; n <= high; n++) {
            if (n <= 1) continue; // 0 and 1 are not prime

            int count = 0;
            for (int div = 2; div * div <= n; div++) {
                if (n % div == 0) {
                    count++;
                    break;
                }
            }
            if (count == 0) {
                System.out.println(n);
            }
        }
    }
}
