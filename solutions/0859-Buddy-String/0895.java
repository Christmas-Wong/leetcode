import java.util.ArrayList;
import java.util.List;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {

    private static boolean buddyString(String a, String b){
        if (a==null || b==null
            || a.length() != b.length()
            || a.length()<2){
            return false;
        }
        if (a.equals(b)){
            List<String> uniqueList = new ArrayList<>();
            for (int i=0;i<a.length();i++){
                if (!uniqueList.contains(String.valueOf(a.charAt(i)))){
                    uniqueList.add(String.valueOf(a.charAt(i)));
                }
            }
            if (uniqueList.size()<a.length()){
                return true;
            }else{
                return false;
            }
        }else{
            List<Integer> different = new ArrayList<>();
            for(int i=0;i<a.length();i++){
                if (a.charAt(i) != b.charAt(i)){
                    different.add(i);
                    if (different.size()>2){
                        return false;
                    }
                }
            }
            if (different.size() != 2){
                return false;
            }
            if (a.charAt(different.get(0)) == b.charAt(different.get(1))
                && a.charAt(different.get(1)) == b.charAt(different.get(0))){
                return true;
            }else{
                return false;
            }

        }
    }

    public static void main(String[] args) {
        String a = "aa";
        String b = "aa";
        System.out.println(buddyString(a, b));
    }

}
