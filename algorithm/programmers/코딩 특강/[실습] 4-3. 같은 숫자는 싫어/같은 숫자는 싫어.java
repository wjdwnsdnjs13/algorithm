import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        for(int a: arr){
            if(list.size() != 0 && list.get(list.size() - 1) == a) continue;
            list.add(a);
        }
        
        int[] answer = list.stream().mapToInt(v -> v).toArray();

        return answer;
    }
}