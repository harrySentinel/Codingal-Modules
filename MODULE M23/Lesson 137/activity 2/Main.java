class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void sound() {
        System.out.println(name + " makes a sound.");
    }

    void eat() {
        System.out.println(name + " is eating.");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    void sound() {
        System.out.println(name + " says: Woof!");
    }
}

class Cat extends Animal {
    Cat(String name) {
        super(name);
    }

    void sound() {
        System.out.println(name + " says: Meow!");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog("Bruno");
        Cat c = new Cat("Whiskers");
        Animal a = new Animal("Unknown Animal");

        d.sound();
        d.eat();
        System.out.println();

        c.sound();
        c.eat();
        System.out.println();

        a.sound();
        a.eat();
    }
}
