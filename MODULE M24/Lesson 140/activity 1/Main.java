class HillStation {
    String name;

    HillStation(String name) { this.name = name; }

    void describe() {
        System.out.println(name + " is a hill station.");
    }
}

class Manali extends HillStation {
    Manali() { super("Manali"); }

    void describe() {
        System.out.println(name + " - Famous for snow, skiing and adventure sports in Himachal Pradesh.");
    }
}

class Ooty extends HillStation {
    Ooty() { super("Ooty"); }

    void describe() {
        System.out.println(name + " - Known as Queen of Hills, located in Tamil Nadu.");
    }
}

class Shimla extends HillStation {
    Shimla() { super("Shimla"); }

    void describe() {
        System.out.println(name + " - Capital of Himachal Pradesh, popular for its colonial charm.");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Polymorphism - Hill Stations of India");
        System.out.println();

        HillStation[] stations = { new Manali(), new Ooty(), new Shimla() };

        for (HillStation h : stations) {
            h.describe();
        }
    }
}
