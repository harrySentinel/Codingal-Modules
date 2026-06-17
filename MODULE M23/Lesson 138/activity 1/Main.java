class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }

    String add(String a, String b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Method Overloading in Java");
        System.out.println();
        System.out.println("add(5, 3)          = " + calc.add(5, 3));
        System.out.println("add(5.5, 2.3)      = " + calc.add(5.5, 2.3));
        System.out.println("add(1, 2, 3)       = " + calc.add(1, 2, 3));
        System.out.println("add(\"Aditya\", \" Srivastava\") = " + calc.add("Aditya", " Srivastava"));
    }
}
