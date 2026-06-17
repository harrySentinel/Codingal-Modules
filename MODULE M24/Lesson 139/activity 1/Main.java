class Student {
    private String name;
    private int age;
    private double marks;

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }
    public void setAge(int age) {
        if (age > 0) this.age = age;
        else System.out.println("Age cannot be negative!");
    }

    public double getMarks() { return marks; }
    public void setMarks(double marks) {
        if (marks >= 0 && marks <= 100) this.marks = marks;
        else System.out.println("Marks must be between 0 and 100!");
    }

    public void display() {
        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Marks : " + marks);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student();
        s.setName("Aditya Srivastava");
        s.setAge(20);
        s.setMarks(92.5);
        s.display();

        s.setAge(-5);
        s.setMarks(150);

        System.out.println("Name via getter: " + s.getName());
        System.out.println("Age via getter : " + s.getAge());
    }
}
