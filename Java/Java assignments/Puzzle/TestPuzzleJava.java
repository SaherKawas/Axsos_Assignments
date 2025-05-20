import java.util.ArrayList;
import java.util.Random;
public class TestPuzzleJava {
    
    public static void main(String[] args) {
        PuzzleJava rolls = new PuzzleJava();
        int[] result = rolls.getTenRolls();
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    
        char randomLetter = rolls.getRandomLetter();
        System.out.println("Random letter: " + randomLetter); 

        String password = rolls.generatePassword();
        System.out.println("Generated password: " + password);  

        ArrayList<String> passwordSet = rolls.getNewPasswordSet(5);
        System.out.println("Password set: " + passwordSet);

    }
}

