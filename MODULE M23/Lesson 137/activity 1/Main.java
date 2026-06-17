class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void display() {
        System.out.println("Name : " + name);
        System.out.println("Age  : " + age);
    }
}

class Student extends Person {
    String school;
    double marks;

    Student(String name, int age, String school, double marks) {
        super(name, age);
        this.school = school;
        this.marks = marks;
    }

    void display() {
        super.display();
        System.out.println("School : " + school);
        System.out.println("Marks  : " + marks);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student("Aditya Srivastava", 20, "Codingal", 92.5);
        Student s2 = new Student("Riya Sharma", 19, "DPS Delhi", 88.0);

        s1.display();
        s2.display();
    }
}
