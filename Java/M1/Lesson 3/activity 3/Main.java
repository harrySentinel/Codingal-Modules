import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = scn.nextInt();

        if (marks > 90) {
            System.out.println("O");
        } else if (marks > 80 && marks <= 90) {
            System.out.println("A+");
        } else if (marks > 70 && marks <= 80) {
            System.out.println("A");
        } else if (marks > 60 && marks <= 70) {
            System.out.println("B");
        } else {
            System.out.println("C");
        }
    }
}
