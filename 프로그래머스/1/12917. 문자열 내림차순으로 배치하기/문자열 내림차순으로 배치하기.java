import java.util.*;

class Solution {
    public String solution(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        s = new StringBuilder(String.valueOf(chars)).reverse().toString();
        return s;
    }
}