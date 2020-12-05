import java.util.HashMap;
import java.util.Map;

public class main {

    private static boolean transformString(String a, String b){
        if (a == null
            || b == null
            || a.length() != b.length()){
            return false;
        }
        int[] stringMap = new int[256];
        for (int i=0;i<a.length();i++){
            stringMap[a.charAt(i)] ++;
        }
        for (int j=0;j<b.length();j++){
            if (stringMap[b.charAt(j)]-- == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        String a = "Hell0";
        String b = "Hello";
        System.out.println(transformString(a, b));
    }
}
