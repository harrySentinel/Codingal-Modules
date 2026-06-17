class Person {
    String name;
    int birthYear;

    Person(String name, int birthYear) {
        this.name = name;
        this.birthYear = birthYear;
    }

    int getAge() {
        return 2025 - birthYear;
    }
}

class Student extends Person {
    String school;

    Student(String name, int birthYear, String school) {
        super(name, birthYear);
        this.school = school;
    }

    void display() {
        System.out.println("Student : " + name);
        System.out.println("School  : " + school);
        System.out.println("Age     : " + getAge());
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student("Aditya Srivastava", 2000, "Codingal");
        Student s2 = new Student("Riya Sharma", 2003, "DPS Delhi");
        Student s3 = new Student("Aman Gupta", 1997, "IIT Mumbai");

        s1.display();
        s2.display();
        s3.display();
    }
}
