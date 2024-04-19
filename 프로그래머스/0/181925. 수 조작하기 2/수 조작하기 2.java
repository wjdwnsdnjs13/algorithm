import java.util.*;

class Solution {
    Map<Integer, String> map;
    List<String> list;
    
    public String solution1(int[] numLog) {
        int prev = numLog[0];
        String answer = "";
        for(int i = 1; i < numLog.length;i++){
            int dif = numLog[i] - prev;
            answer += (dif == 1)?"w":(dif == -1)?"s":(dif == 10)?"d":"a";
            prev = numLog[i];
        }
        
        return answer;
    }
    
    public String solution(int[] numLog) {
        map = new HashMap<>();
        map.put(1, "w");
        map.put(-1, "s");
        map.put(10, "d");
        map.put(-10, "a");
        
        int prev = numLog[0];
        String answer = "";
        for(int i = 1; i < numLog.length;i++){
            int dif = numLog[i] - prev;
            answer += map.get(dif);
            prev = numLog[i];
        }
        
        return answer;
    }
}