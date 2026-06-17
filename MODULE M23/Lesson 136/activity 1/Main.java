class Employee {
    String name;
    int age;
    String department;
    double salary;

    Employee(String name, int age, String department, double salary) {
        this.name = name;
        this.age = age;
        this.department = department;
        this.salary = salary;
    }

    void display() {
        System.out.println("Name       : " + name);
        System.out.println("Age        : " + age);
        System.out.println("Department : " + department);
        System.out.println("Salary     : ₹" + salary);
        System.out.println();
    }

    void appraisal(double percent) {
        salary += salary * percent / 100;
        System.out.println(name + " got an appraisal! New Salary: ₹" + salary);
    }
}

public class Main {
    public static void main(String[] args) {
        Employee e1 = new Employee("Aditya Srivastava", 25, "Engineering", 95000);
        Employee e2 = new Employee("Riya Sharma", 22, "Marketing", 72000);

        e1.display();
        e2.display();

        e1.appraisal(10);
        e2.appraisal(8);
    }
}
