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
        // mapToInt : mapToInt(ToIntFunction<? super T> mapper) function 처리된 IntStream을 리턴해줌.
        // IntStream에 넣기 위해서 Intger를 int로 변환해줘야해서 Integer#intValue() 사용
        int[] answer = indexList.stream().mapToInt(Integer :: intValue).toArray();
        return answer;
    }
}