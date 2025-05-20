
import java.util.ArrayList;
import java.util.Random;


public class PuzzleJava{
    // access modifier // return type // method with parameters
    public int[] getTenRolls(){
        int[] output = new int[10];
        Random rand= new Random();
        for(int i=0; i<10; i++){
            int result= rand.nextInt(20)+1;
            output[i]=result;
        }
        return output;
    }

    public char getRandomLetter(){
        char[] alphabet = new char[26];
        Random rand= new Random();
        for (int i=0; i<26;i++){
            alphabet[i] = (char) (i+'a');

        System.out.println(alphabet);
        
        }
        int rand_num = rand.nextInt(26);

        return alphabet[rand_num];
    }

    public String generatePassword() {
            StringBuilder password = new StringBuilder();
            for (int i = 0; i < 8; i++) {
                password.append(getRandomLetter());
            }
            return password.toString();
    }

    public ArrayList<String> getNewPasswordSet(int length) {
        ArrayList<String> passwordSet = new ArrayList<String>();
        for (int i = 0; i < length; i++) {
            passwordSet.add(generatePassword());
        }
        return passwordSet;
    }
    
}
