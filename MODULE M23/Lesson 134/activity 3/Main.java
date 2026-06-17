public class Main {
    public static void main(String[] args) {
        String name = "Maggie";
        int cookingTime = 2;
        double price = 14.5;
        boolean isSpicy = true;
        char size = 'M';

        System.out.println("Product   : " + name);
        System.out.println("Cook Time : " + cookingTime + " minutes");
        System.out.println("Price     : ₹" + price);
        System.out.println("Spicy     : " + isSpicy);
        System.out.println("Size      : " + size);
        System.out.println();

        int packets = 5;
        double totalCost = packets * price;
        System.out.println("Buying " + packets + " packets of " + name);
        System.out.println("Total Cost : ₹" + totalCost);
        System.out.println("Total Cook Time : " + (packets * cookingTime) + " minutes");
    }
}
