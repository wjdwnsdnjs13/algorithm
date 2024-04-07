import java.util.*;

class Solution {
    public long[] solution(long x, int n) {
        long result = 0;
        List<Long> answer = new ArrayList<>();
        for(long i = 0; i < n; i++){
            result += x;
            answer.add(result);
        }
        return answer.stream().mapToLong(Long::longValue).toArray();
    }
}