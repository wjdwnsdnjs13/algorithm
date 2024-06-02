import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // query = [s, e, k]
        // i에 대해 i가 k의 배수이면, arr[i]++
        // i가 s와 k 사이일 경우, 모든 i에 대해 k의 배수면 1더함.
        
        for(int[] query: queries){
            for(int i = 0; i < arr.length; i++){
                if(query[0] <= i && query[1] >= i && i%query[2] == 0) arr[i]++;
            }
        }
        return arr;
    }
}