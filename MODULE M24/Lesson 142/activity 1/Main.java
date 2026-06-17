import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter your age: ");
            int age = Integer.parseInt(sc.nextLine());

            if (age < 0) throw new IllegalArgumentException("Age cannot be negative!");
            if (age < 18) throw new ArithmeticException("You must be 18+ to apply.");

            System.out.println("Application submitted successfully!");
            System.out.println("Welcome to Codingal, applicant aged " + age + ".");

        } catch (NumberFormatException e) {
            System.out.println("Error: Please enter a valid number. " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Application process completed.");
            sc.close();
        }
    }
}
