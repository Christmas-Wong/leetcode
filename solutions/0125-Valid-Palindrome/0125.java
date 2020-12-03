import java.util.ArrayList;
import java.util.List;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {

    /**
     * use string function
     * @param s
     * @return
     */
    private static boolean isPalindromeFunction(String s){
        StringBuffer originString = new StringBuffer();
        for(int i=0;i<s.length();i++){
            char stringEle = s.charAt(i);
            if (Character.isLetterOrDigit(stringEle)){
                originString.append(Character.toLowerCase(stringEle));
            }
        }
        StringBuffer reverseString = new StringBuffer(originString).reverse();
        return originString.toString().equals(reverseString.toString());
    }

    /**
     * use double pointer
     * @param s
     * @return
     */
    private static boolean isPalindromeDoublePointer(String s){
        if (s.equals("")){
            return true;
        }
        int left = 0;
        int right = s.length()-1;
        while(left<right){
            if (!Character.isLetterOrDigit(s.charAt(left))){
                left ++;
                continue;
            }
            if (!Character.isLetterOrDigit(s.charAt(right))){
                right --;
                continue;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
                return false;
            }
            left ++;
            right --;
        }
        return true;

    }

    public static void main(String[] args) {
        String test_string = "A man, a plan, a canal: Panama";
        System.out.println(isPalindromeFunction(test_string));
    }

}
