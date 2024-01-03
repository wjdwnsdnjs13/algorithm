import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
//         매일 다른 옷을 조합해야 함.
//         각 종류 별로 최대 1개만 가능.
//         일부가 겹쳐도 다른 게 겹치지 않거나 추가 착용 시 다른 방법임.
//         최소 한 개 이상의 의상은 입어야 함.
//         서로 다른 옷의 조합 수 return
        
//         clothes는 [의상이름, 종류]로 이루어짐.
//         1 <= 의상의 개수 <= 30
//         이름 같은 의상 x
//         clothes의 모든 원소는 문자열
//         1 <= 문자열 길이 <= 20, 알파벳 소문자 혹은 _로 이루어짐.
        
        // Map<옷종류, 종류_count + 1> 만들고, 곱 - 1 하면 될 듯.
        Map<String, Integer> map = new HashMap<>();
        for(String[] cloth: clothes){
            map.put(cloth[1], map.getOrDefault(cloth[1], 1) + 1);
        }
           
        int answer = 1;
        for(String key: map.keySet()) answer *= map.get(key);
        return answer - 1;
    }
}