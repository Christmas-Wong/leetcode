import com.sun.deploy.util.StringUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {

    /**
     * one line solution
     * @param s
     * @return
     */
    private static String oneLine(String s){
        return Arrays.stream(s.split(" ")).map(word -> new StringBuilder(word).reverse().toString()).collect(Collectors.joining(" "));
    }

    /**
     * one pointer for loop
     * one pointer for words
     * @param s
     * @return
     */
    private static String reverseWord(String s){
        StringBuffer returnValue = new StringBuffer();
        if (s == null || s.length()<2){
            return s;
        }
        int index = 0;
        while(index < s.length()){
            int start = index;
            while (start<s.length() && !Character.isSpaceChar(s.charAt(start))){
                start ++;
            }
            for(int i=1;i+index<=start;i++){
                returnValue.append(s.charAt(start-i));
            }
            index = start;
            while(index<s.length() && Character.isSpaceChar(s.charAt(index))){
                returnValue.append(" ");
                index ++;
            }

        }
        return returnValue.toString();

    }

    public static void main(String[] args) {
        String a = "Let's take LeetCode contest";
        System.out.println(reverseWord(a));

    }

}
