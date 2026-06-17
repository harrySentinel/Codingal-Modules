interface Vehicle {
    void start();
    void stop();
    int getSpeed();
}

class Car implements Vehicle {
    String model;
    Car(String model) { this.model = model; }

    public void start() { System.out.println(model + " car started."); }
    public void stop()  { System.out.println(model + " car stopped."); }
    public int getSpeed() { return 120; }
}

class Bike implements Vehicle {
    String brand;
    Bike(String brand) { this.brand = brand; }

    public void start() { System.out.println(brand + " bike started."); }
    public void stop()  { System.out.println(brand + " bike stopped."); }
    public int getSpeed() { return 80; }
}

class Train implements Vehicle {
    public void start() { System.out.println("Train departed from the station."); }
    public void stop()  { System.out.println("Train arrived at the station."); }
    public int getSpeed() { return 200; }
}

public class Main {
    public static void main(String[] args) {
        Vehicle[] vehicles = {
            new Car("Toyota"),
            new Bike("Royal Enfield"),
            new Train()
        };

        for (Vehicle v : vehicles) {
            v.start();
            System.out.println("Max Speed: " + v.getSpeed() + " km/h");
            v.stop();
            System.out.println();
        }
    }
}
