import java.util.stream.IntStream;

class Solution {
    public int solution1(int n) {
        // n이 짝수면 짝수들만 -> even = true
        // 홀수면 홀수들만 -> even = false
        
        boolean even = (n%2 == 0);
        int answer = IntStream.range(1, n + 1)
            .filter(x -> (x%2 == 0) == even)
            .map(y -> even?(int) Math.pow(y, 2):y)
            .sum();
        System.out.println(answer);
        return answer;
    }
    
    public int solution2(int n) {
        // n이 짝수면 짝수들만 -> even = true
        // 홀수면 홀수들만 -> even = false
        
        int even = (n%2 == 0)?2:1;
        int answer = 0;
        for(int i = even; i < n + 1; i += 2){
            answer += (even == 2)?(int) Math.pow(i, 2):i;
        }
        return answer;
    }
    
    public int solution(int n) {
        // n이 짝수면 짝수들만 -> even = true
        // 홀수면 홀수들만 -> even = false
        
        int even = (n%2 == 0)?2:1;
        int answer = 0;
        for(int i = even; i < n + 1; i += 2){
            answer += (even == 2)?i * i:i;
        }
        return answer;
    }
}