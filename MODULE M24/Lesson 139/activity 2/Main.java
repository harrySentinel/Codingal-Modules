class Shape {
    private double length;
    private double width;
    private double radius;

    public void setLength(double length) { this.length = length; }
    public void setWidth(double width) { this.width = width; }
    public void setRadius(double radius) { this.radius = radius; }

    public double getRectangleArea() { return length * width; }
    public double getCircleArea() { return Math.PI * radius * radius; }
    public double getTriangleArea() { return 0.5 * length * width; }
}

public class Main {
    public static void main(String[] args) {
        Shape s = new Shape();

        s.setLength(10);
        s.setWidth(5);
        System.out.println("Rectangle Area  : " + s.getRectangleArea());
        System.out.println("Triangle Area   : " + s.getTriangleArea());

        s.setRadius(7);
        System.out.printf("Circle Area     : %.2f%n", s.getCircleArea());
    }
}
