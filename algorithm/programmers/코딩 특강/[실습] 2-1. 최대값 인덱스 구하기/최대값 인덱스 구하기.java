import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr) {
        // Array를 사용해서 최댓값의 인덱스 목록을 리턴.
        
        List<Integer> indexList = new ArrayList<>();
        int maxValue = Arrays.stream(arr).max().getAsInt();
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == maxValue) indexList.add(i);
        }
        int[] answer = new int[indexList.size()];
        for(int i = 0; i < indexList.size(); i++) answer[i] = indexList.get(i);
        return answer;
    }
}