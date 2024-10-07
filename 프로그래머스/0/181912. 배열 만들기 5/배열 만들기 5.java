import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        // s번 인덱스에서 시작하는 l짜리 문자열
        // k보다 큰 값을 담은 배열 리턴
        List<Integer> answer = new ArrayList();
        for(String str: intStrs){
            Integer a = Integer.valueOf(str.substring(s, s + l));
            if(a > k) answer.add(a);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}