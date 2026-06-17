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

class Employee extends Person {
    String company;
    double salary;

    Employee(String name, int age, String company, double salary) {
        super(name, age);
        this.company = company;
        this.salary = salary;
    }

    void display() {
        super.display();
        System.out.println("Company : " + company);
        System.out.println("Salary  : ₹" + salary);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Using super keyword in Java");
        System.out.println();

        Employee e1 = new Employee("Aditya Srivastava", 25, "Codingal", 95000);
        Employee e2 = new Employee("Riya Sharma", 22, "Google", 120000);

        e1.display();
        e2.display();
    }
}
