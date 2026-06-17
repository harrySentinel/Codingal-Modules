class Animal {
    String name;
    Animal(String name) { this.name = name; }
    void describe() { System.out.println(name + " is an animal."); }
}

class Mammal extends Animal {
    Mammal(String name) { super(name); }
    void describe() {
        super.describe();
        System.out.println(name + " is a mammal - warm-blooded and feeds young with milk.");
    }
}

class Dog extends Mammal {
    String breed;
    Dog(String name, String breed) {
        super(name);
        this.breed = breed;
    }
    void describe() {
        super.describe();
        System.out.println(name + " is a dog of breed: " + breed);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d1 = new Dog("Bruno", "Labrador");
        Dog d2 = new Dog("Max", "German Shepherd");

        d1.describe();
        d2.describe();
    }
}
