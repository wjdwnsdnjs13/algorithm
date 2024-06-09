import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n) {
        // 1. 짝수면 2로 나누고
        // 2. 홀수면 3 * x + 1로 바꾸기
        // 1, 2를 1이 될 때까지 반복하고, 수열을 리턴
        List<Integer> answer = new ArrayList<>();
        answer.add(n);
        while(n != 1){
            if(n%2 == 0) n /= 2;
            else n = 3 * n + 1;
            answer.add(n);
        }
        
        return answer.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}