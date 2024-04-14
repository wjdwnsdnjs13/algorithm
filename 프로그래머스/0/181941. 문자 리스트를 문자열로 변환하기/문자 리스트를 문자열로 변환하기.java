import java.util.*;

class Solution {
    public String solution1(String[] arr) {
        String answer = String.join("", arr);
        return answer;
    }
    public String solution2(String[] arr) {
        StringBuilder answer = new StringBuilder();
        for(String a: arr) answer.append(a);
        return answer.toString();
    }
    public String solution(String[] arr) {
        StringBuilder answer = new StringBuilder();
        Arrays.stream(arr).forEach(n -> answer.append(n));
        return answer.toString();
    }
}