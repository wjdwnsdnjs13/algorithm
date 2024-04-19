import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        for(int i = 0; i < num_list.length; i++) answer[i] = num_list[i];
        int result = answer[num_list.length - 1] - answer[num_list.length - 2];
        answer[num_list.length] = (result > 0)?result:answer[num_list.length - 1] * 2;
        return answer;
    }
}