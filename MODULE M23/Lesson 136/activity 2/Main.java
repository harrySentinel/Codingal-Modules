class Counter {
    static int count = 0;
    String name;

    Counter(String name) {
        this.name = name;
        count++;
        System.out.println(name + " created. Total objects: " + count);
    }

    static void showCount() {
        System.out.println("Total Counter objects created: " + count);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Static Counter Example");
        System.out.println();

        Counter c1 = new Counter("Aditya");
        Counter c2 = new Counter("Riya");
        Counter c3 = new Counter("Aman");

        System.out.println();
        Counter.showCount();
    }
}
