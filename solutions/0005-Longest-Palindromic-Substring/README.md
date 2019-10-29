# 解题思路
- 注意：回文子串是奇数还是偶数
## 暴力法
两重循环+递归
- 第一重循环：假定回文子串的长度为s.length(),子串的长度逐渐减小
- 第二重循环：子串的起始点（leftIndex）从0开始，整个子串逐渐右移，右标签小于s的最右边的数
- 第三重：利用递归判断每一个子串是不是回文子串
```
    public boolean recursive(String s){
        if(s.length()==2){
            if(s.charAt(0)==s.charAt(1)){return true;}
            else{return false;}
        }
        if(s.length()<=1){return true;}
        if(s.charAt(0)==s.charAt(s.length()-1)){
            String output = s.substring(1,s.length()-1);
            return recursive(output);
        }else{
            return false;
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
                if(recursive(outPut)){
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
```
## 中心扩展法
两重循环
- 第一重循环：设定回文子串的中心点
- 第二重循环：设定步长，回文子串从中心点向两边扩展,如果左右两边相等，继续扩展，注意边界
- **解决奇数偶数问题**
    - 问题描述：奇数子串中心点是一个字符（例如：abcxcba）；偶数子串其实没有中心点（例如：abccba）
    - 解决办法：
        1. 在每个字符的前面加上一个字符，例如：#
        2. 在字符串的末尾加上一个字符，例如：#
        3. 这样原来字符串就变成了一个奇数字符串，2*（s.length()）+1
```
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
```
## 动态规划

## Manacher