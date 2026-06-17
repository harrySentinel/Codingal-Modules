import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        System.out.println("Magic 2 - HashMap & Collections!");
        System.out.println();

        HashMap<String, Integer> spellPower = new HashMap<>();
        spellPower.put("Lumos", 30);
        spellPower.put("Expelliarmus", 75);
        spellPower.put("Wingardium Leviosa", 50);
        spellPower.put("Avada Kedavra", 100);
        spellPower.put("Accio", 40);

        System.out.println("Spell Power Map:");
        for (String spell : spellPower.keySet()) {
            System.out.println("  " + spell + " -> Power: " + spellPower.get(spell));
        }

        System.out.println();
        System.out.println("Most powerful spell power: " + Collections.max(spellPower.values()));

        ArrayList<Integer> powers = new ArrayList<>(spellPower.values());
        Collections.sort(powers, Collections.reverseOrder());
        System.out.println("Powers ranked: " + powers);

        System.out.println();
        System.out.println("Spells with power > 50:");
        for (String spell : spellPower.keySet()) {
            if (spellPower.get(spell) > 50) {
                System.out.println("  " + spell);
            }
        }
    }
}
