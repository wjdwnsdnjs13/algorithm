import java.util.*;

class Solution {
    boolean solution(String s) {
        // 대소문자 구분하지 않음.
        s = s.toLowerCase();
        int[] count = new int[]{0, 0};
        for(char x: s.toCharArray()){
            int a = ((x == 'p')?count[0]++ : ((x == 'y')?count[1]++:0));
        }
        System.out.println(Arrays.toString(count));
        boolean answer = count[0] == count[1];
        return answer;
    }
}