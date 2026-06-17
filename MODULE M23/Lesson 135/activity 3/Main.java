public class Main {
    public static void main(String[] args) {
        String[] students = {"Aditya", "Riya", "Aman", "Neha", "Rohan"};
        int[] marks = {92, 78, 85, 60, 74};

        System.out.println("Student Report Card:");
        System.out.println("-----------------------------");

        for (int i = 0; i < students.length; i++) {
            String grade;
            if (marks[i] >= 90) {
                grade = "A+";
            } else if (marks[i] >= 80) {
                grade = "A";
            } else if (marks[i] >= 70) {
                grade = "B";
            } else if (marks[i] >= 60) {
                grade = "C";
            } else {
                grade = "F";
            }
            System.out.println(students[i] + " : " + marks[i] + " -> Grade: " + grade);
        }
    }
}
