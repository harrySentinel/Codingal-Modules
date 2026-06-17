interface Greetable {
    void greet();
}

interface Describable {
    void describe();
}

class Instructor implements Greetable, Describable {
    String name;
    String subject;

    Instructor(String name, String subject) {
        this.name = name;
        this.subject = subject;
    }

    public void greet() {
        System.out.println("Hello! I am " + name + ".");
    }

    public void describe() {
        System.out.println("I teach " + subject + " at Codingal.");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Interface in Java");
        System.out.println();

        Instructor i = new Instructor("Aditya Srivastava", "Python & AI");
        i.greet();
        i.describe();

        System.out.println();
        Greetable g = new Instructor("Riya Sharma", "Web Development");
        g.greet();
    }
}
