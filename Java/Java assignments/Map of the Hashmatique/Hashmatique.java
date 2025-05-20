import java.util.HashMap;
import java.util.Set;
public class Hashmatique{
    public static void main( String[] args){
        HashMap<String, String> trackList = new HashMap<String, String>();
        trackList.put("Beautiful Things", "Please stay I want you, I need you, oh God Don't take These beautiful things that I've got");
        trackList.put("Mystical Magical", "Mystical, magical Oh baby, 'cause once you know, once you know My love is so mystical, magical Oh, baby, 'cause once you know, once you know");
        trackList.put("Sign of the times", "Just stop your crying, it's a sign of the times We gotta get away from here We gotta get away from here");
        trackList.put("Die with a smile", "If the world was ending, I'd wanna be next to you, If the party was over and our time on Earth was through");

        String track = trackList.get("Mystical Magical");

        Set<String> keys = trackList.keySet();
        for(String key: keys){
           System.out.println(key + ": " + trackList.get(key));
        }


    }

}
