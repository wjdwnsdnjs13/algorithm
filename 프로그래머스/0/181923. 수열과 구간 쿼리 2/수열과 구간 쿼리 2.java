import java.util.*;

class Solution {
    List<Integer> list;
    
    public int[] solution(int[] arr, int[][] queries) {
        // query = [s, e, k]
        // s와 e 사이의 값 i에 대해 k보다 크면서 가장 작은 arr[i]
        // 결과값 배열 리턴.(없으면 -1)
        
        list = new ArrayList<>();
        for(int[] query:queries){
            int s = query[0], e = query[1], k = query[2];
            int result = 99999999;
            for(int i = s; i <= e; i++) if(arr[i] > k && arr[i] < result) result = arr[i];
            list.add((result != 99999999)?result:-1);
        }
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        
        return answer;
    }
}