import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @ClassName Solution
 * @Description TODO Brute Force
 * @Author Wang Fei
 * @EditorTime 2019/10/28 14:45
 * @Version 1.0
 **/
public class Solution {
    public String digui(String s){
        if(s.length()==2){
            if(s.charAt(0)==s.charAt(1)){return s;}
            else{return null;}
        }
        if(s.length()<=1){return s;}
        if(s.charAt(0)==s.charAt(s.length()-1)){
            String output = s.substring(1,s.length()-1);
            return digui(output);
        }else{
            return null;
        }
    }
    public String longestPalindrome(String s) {
        int length = s.length();
        int start = 0;
        String outPut = "";
        if(s.length()<=1){
            return s;
        }
        for(;length>0;length--){
            start=0;
            while(start+length<s.length()+1){
                outPut = s.substring(start,start+length);
                if(digui(outPut)==null){
                    start++;
                    continue;
                }else{
                    return outPut;
                }
            }
        }
        outPut = s.substring(0,1);
        return outPut;
    }
    public String centerExpansion(String s){
        int leftIndex = 0;
        int stepSize = 0;
        String midString = "";
        String returnString = "";

        StringBuilder newString = new StringBuilder();
        for(int i=0;i<s.length();i++){
            newString.append("#");
            newString.append(s.charAt(i));
        }
        newString.append("#");

        for (;leftIndex<newString.length();leftIndex++){
            stepSize=0;
            while(leftIndex-stepSize>=0 && leftIndex+stepSize<newString.length()){
                if(newString.charAt(leftIndex-stepSize)==newString.charAt(leftIndex+stepSize)){
                    midString = newString.substring(leftIndex-stepSize,leftIndex+stepSize+1);
                    if(midString.length()>returnString.length()){
                        returnString = midString;
                    }
                    stepSize++;
                }else{
                    break;
                }
            }
        }
        returnString = returnString.replace("#","");
        return returnString;
    }
    public static void main(String[] args){
        String s = "abacab";
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome(s));

    }
}
