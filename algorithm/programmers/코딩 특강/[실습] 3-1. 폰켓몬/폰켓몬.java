import java.util.*;

class Solution {
    public int solution(int[] nums) {
        // 같은 종류의 포켓몬은 같은 번호
        // N/2마리 포켓몬을 선택함.
        // 가장 많은 종류의 포켓몬을 선택하는 경우를 찾아, 이 때 종류수를 리턴
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            if(map.get(num) != null) map.put(num, map.get(num) + 1);
            else map.put(num, 1);
        }
        int answer = (map.size() > nums.length/2)?nums.length/2:map.size();
        return answer;
    }
}