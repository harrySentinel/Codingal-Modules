import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        System.out.println("Magic 1 - ArrayList Spells!");
        System.out.println();

        ArrayList<String> spells = new ArrayList<>();
        spells.add("Lumos");
        spells.add("Expelliarmus");
        spells.add("Wingardium Leviosa");
        spells.add("Alohomora");
        spells.add("Accio");

        System.out.println("All Spells: " + spells);
        System.out.println("Total Spells: " + spells.size());
        System.out.println();

        spells.remove("Alohomora");
        System.out.println("After removing Alohomora: " + spells);

        Collections.sort(spells);
        System.out.println("Sorted Spells: " + spells);

        System.out.println("Contains Lumos: " + spells.contains("Lumos"));
        System.out.println("Spell at index 0: " + spells.get(0));

        System.out.println();
        System.out.println("Looping through spells:");
        for (String spell : spells) {
            System.out.println("  ✨ " + spell);
        }
    }
}
