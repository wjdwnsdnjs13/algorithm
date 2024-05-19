import java.util.*;

public class Solution {
    public int solution1(int n) {
        // 어차피 자릿수 계산하거나 stream 쓰려면 String이나 char로 변환해야할 거 같음.
        int answer = 0;
        while(n > 0){
            answer += n%10;
            n /= 10;
        }
        return answer;
    }
    
    public int solution2(int n) {
        // 어차피 자릿수 계산하거나 stream 쓰려면 String이나 char로 변환해야할 거 같음.
        String[] number = Integer.toString(n).split("");
        // System.out.println(Arrays.toString(number));
        int answer = Arrays.stream(number).mapToInt(s -> Integer.parseInt(s)).sum();
        return answer;
    }
    
    public int solution(int n) {
        // 어차피 자릿수 계산하거나 stream 쓰려면 String이나 char로 변환해야할 거 같음.
        String[] number = Integer.toString(n).split("");
        int answer = 0;
        for(String s: number){
            answer += Integer.parseInt(s);
        }
        return answer;
    }
}