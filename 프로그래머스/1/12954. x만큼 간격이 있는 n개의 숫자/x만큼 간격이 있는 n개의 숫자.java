import java.util.*;

class Solution {
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