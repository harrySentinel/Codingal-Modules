class Shape {
    void draw() { System.out.println("Drawing a shape."); }
    double area() { return 0; }
}

class Circle extends Shape {
    double radius;
    Circle(double r) { this.radius = r; }

    void draw() { System.out.println("Drawing a Circle."); }
    double area() { return Math.PI * radius * radius; }
}

class Rectangle extends Shape {
    double l, w;
    Rectangle(double l, double w) { this.l = l; this.w = w; }

    void draw() { System.out.println("Drawing a Rectangle."); }
    double area() { return l * w; }
}

class Triangle extends Shape {
    double b, h;
    Triangle(double b, double h) { this.b = b; this.h = h; }

    void draw() { System.out.println("Drawing a Triangle."); }
    double area() { return 0.5 * b * h; }
}

public class Main {
    public static void main(String[] args) {
        Shape[] shapes = {
            new Circle(5),
            new Rectangle(8, 4),
            new Triangle(6, 3)
        };

        for (Shape s : shapes) {
            s.draw();
            System.out.printf("Area: %.2f%n%n", s.area());
        }
    }
}
