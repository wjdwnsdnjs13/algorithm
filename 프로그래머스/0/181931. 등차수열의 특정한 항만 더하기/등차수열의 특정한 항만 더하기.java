import java.util.*;

class Solution {
    public int solution1(int a, int d, boolean[] included) {
        int answer = 0;
        for(int i = 1; i < included.length + 1; i++){
            answer += (included[i - 1]?a:0);
            a += d;
        }
        return answer;
    }
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        for(boolean flag: included){
            answer += flag?a:0;
            a += d;
        }
        return answer;
    }
}