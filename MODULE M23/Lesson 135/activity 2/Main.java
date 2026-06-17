import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.println();
        System.out.println("Hello, " + name + "!");

        if (age < 13) {
            System.out.println("You are a child.");
        } else if (age < 18) {
            System.out.println("You are a teenager.");
        } else if (age < 60) {
            System.out.println("You are an adult.");
        } else {
            System.out.println("You are a senior citizen.");
        }

        sc.close();
    }
}
