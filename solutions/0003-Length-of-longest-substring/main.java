import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {

    public static int lengthOfLongestSubstring(String s) {
        int i = 0;
        int j = 0;
        int maxlength = 0;
        int limit = s.length();
        Set<Character> container = new HashSet<>();
        while(i<limit && j<limit){
            if(!container.contains(s.charAt(j))){
                container.add(s.charAt(j++));
                maxlength = Math.max(maxlength,j-i);
            }else{
                container.remove(s.charAt(i++));
            }
        }
        return maxlength;
    }

    public static void main(String[] args) {
        String originString = "pw";
        System.out.println(lengthOfLongestSubstring(originString));

    }
}
