import java.util.Scanner;

class AgeException extends Exception {
    AgeException(String msg) { super(msg); }
}

class GradeException extends Exception {
    GradeException(String msg) { super(msg); }
}

public class Main {
    static void hire(String name, int age, double cgpa) throws AgeException, GradeException {
        if (age < 18 || age > 26) throw new AgeException("Age must be between 18 and 26.");
        if (cgpa < 7.0) throw new GradeException("CGPA must be at least 7.0.");
        System.out.println(name + " is selected as an intern!");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter intern name: ");
        String name = sc.nextLine();

        System.out.print("Enter age: ");
        int age = sc.nextInt();

        System.out.print("Enter CGPA: ");
        double cgpa = sc.nextDouble();

        try {
            hire(name, age, cgpa);
        } catch (AgeException e) {
            System.out.println("Rejected - Age Issue: " + e.getMessage());
        } catch (GradeException e) {
            System.out.println("Rejected - Grade Issue: " + e.getMessage());
        } finally {
            System.out.println("Screening process done.");
            sc.close();
        }
    }
}
