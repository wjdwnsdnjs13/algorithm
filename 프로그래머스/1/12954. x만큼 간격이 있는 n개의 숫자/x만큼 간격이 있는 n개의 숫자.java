import java.util.*;

class Solution {
    public long[] solution(long x, int n) {
        long[] answer = new long[n];
        answer[0] = x;
        for(int i = 1; i < n; i++){
            answer[i] = answer[i - 1] + x;
        }
        return answer;
    }
}

class Solution2 {
    public long[] solution(long x, int n) {
        long result = 0;
        List<Long> list = new ArrayList<>();
        for(int i = 0; i < n; i++){
            result += x;
            list.add(result);
        }
        long[] answer = list.stream().mapToLong(Long :: longValue).toArray();
        return answer;
    }
}