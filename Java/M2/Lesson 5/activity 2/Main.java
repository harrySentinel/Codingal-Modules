// this program is created to teach the concept of abstraction
abstract class Objects {
    // abstract method declaration
    abstract void showShape();

    public void shape() {
        System.out.println("I'm from abstract class");
    }
}

class Sphere extends Objects {
    void showShape() {
        System.out.println("Object type is Sphere.");
    }
}

class Cuboid extends Objects {
    void showShape() {
        System.out.println("Object type is Cuboid.");
    }
}

class Prism extends Objects {
    void showShape() {
        System.out.println("Object type is Prism.");
    }
}

public class Main {
    public static void main(String[] args) {
        Objects obj = new Sphere();  // object of sphere
        obj.shape();
        obj.showShape();

        obj = new Cuboid();          // cuboid
        obj.shape();
        obj.showShape();

        obj = new Prism();           // prism
        obj.shape();
        obj.showShape();
    }
}
