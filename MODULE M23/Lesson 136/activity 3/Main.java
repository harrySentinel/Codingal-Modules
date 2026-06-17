public class Main {
    public static void main(String[] args) {
        String shabd = "Aditya Srivastava";

        System.out.println("Original  : " + shabd);
        System.out.println("Length    : " + shabd.length());
        System.out.println("Uppercase : " + shabd.toUpperCase());
        System.out.println("Lowercase : " + shabd.toLowerCase());
        System.out.println("Reversed  : " + new StringBuilder(shabd).reverse());
        System.out.println("Contains 'Codingal' : " + shabd.contains("Codingal"));
        System.out.println("Replace 'Aditya' with 'Riya' : " + shabd.replace("Aditya", "Riya"));
        System.out.println("First char : " + shabd.charAt(0));
        System.out.println("Index of 'S' : " + shabd.indexOf('S'));

        String[] words = shabd.split(" ");
        System.out.println("Word count : " + words.length);
        for (String word : words) {
            System.out.println("  Word: " + word);
        }
    }
}
