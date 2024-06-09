import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr) {
        // i를 0으로 설정 후 i가 arr 길이보다 작을 때
        //     1. stk가 빈 배열이면 arr[i]를 stk에 추가하고, i + 1
        //     2. stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk 뒤에 추가하고 i를 더함
        //     3. stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소 제거
        
        List<Integer> stk = new ArrayList<>();
        int i = 0;
        while(i < arr.length){
            if(stk.size() == 0){
                stk.add(arr[i]);
                i++;
            }
            else if(stk.get(stk.size() - 1) < arr[i]){
                stk.add(arr[i]);
                i++;
            }
            else{
                stk.remove(stk.size() - 1);
            }
        }
        return stk.stream()
            .mapToInt(j -> j)
            .toArray();
    }
}