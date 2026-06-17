class Animal {
    void sound() {
        System.out.println("Animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog says: Woof!");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat says: Meow!");
    }
}

class Cow extends Animal {
    @Override
    void sound() {
        System.out.println("Cow says: Moo!");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Method Overriding in Java");
        System.out.println();

        Animal a = new Animal();
        Animal d = new Dog();
        Animal c = new Cat();
        Animal cow = new Cow();

        a.sound();
        d.sound();
        c.sound();
        cow.sound();
    }
}
