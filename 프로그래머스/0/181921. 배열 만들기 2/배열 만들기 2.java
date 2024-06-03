import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
//         l과 r 사이 정수 중 0과 5로만 이루어진 모든 정수를 오름차순으로 정렬해 리턴.
//         없을 경우 [-1] 리턴
            
//         l을 10으로 나눠서 자릿수(10 * x)를 알아낸 후 5x의 값부터 시작
//         자릿수를 올라가며 해당 자릿수가 0이면 5 더하고 끝.
//         아닐 경우 끝까지 가서 * 10 한 다음 위의 알고리즘 반복.
        List<Integer> result = new ArrayList<>();
        
        int n = (int) Math.pow(10, (int) Math.log10(l)) * 5;
        if(n < l) n *= 10;
        for(int i = n; i <= r; i += 5){
            String strI = Integer.toString(i);
            boolean flag = false;
            for(int j = 0; j < strI.length(); j++) if(strI.charAt(j) != '0' && strI.charAt(j) != '5') flag = true;
            if(flag) continue;
            result.add(i);
        }
        return (result.isEmpty())?new int[] {-1}:result.stream().mapToInt(i -> i).toArray();
    }
}