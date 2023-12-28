import java.util.Arrays;

class Solution {
    public boolean solution(int[] arr) {
        // 1부터 n까지 숫자가 중복이 안되는 지 확인.
        // 중복이 없으면 true, 중복이 있으면 fals 리턴
        // 배열 길이 10만
        // 배열의 원소는 0 이상 10만 이하
        
        // 배열을 정렬하고 for문 돌면서 맞는 지 확인하면 될 듯.
        boolean answer = true;
        
        Arrays.sort(arr);
        for(int i = 1; i <= arr.length; i++) if(arr[i - 1] != i) answer = false;
        return answer;
    }
}