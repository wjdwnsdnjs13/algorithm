import java.util.*;

class Solution {
    public static final Integer DP_MAX_VALUE = Integer.valueOf(9999999);
    
    List<Integer> dp;
    
    public int solution(int x, int y, int n) {
//         x를 y로 변환함.
        
//         a. x + n
//         b. x * 2
//         c. x * 3
        
//         3가지 연산을 사용해서 x를 y로 변환하기 위한 최소 연산 횟수를 return하기.
        dp = new ArrayList();
        for(int i = 0; i < y + 1; i++) dp.add(DP_MAX_VALUE);
        dp.set(x, 0);
        if(dp.size() > x + n) dp.set(x + n, 1);
        if(dp.size() > x * 2) dp.set(x * 2, 1);
        if(dp.size() > x * 3) dp.set(x * 3, 1);
        
        for(int i = x; i < y + 1; i++){
            int value = dp.get(i);
            int prev;
            if(i >= n){
                prev = dp.get(i - n);
                if(prev < value) dp.set(i, prev + 1);
            }
            // if(i%2 == 0){
            //     prev = dp.get(i/2);
            //     if(prev < value) dp.set(i, prev + 1);
            // }
            // if(i%3 == 0){
            //     prev = dp.get(i/3);
            //     if(prev < value) dp.set(i, prev + 1);
            // }
            if(i * 2 <= y) dp.set(i * 2, Math.min(dp.get(i * 2), dp.get(i) + 1));
            if(i * 3 <= y) dp.set(i * 3, Math.min(dp.get(i * 3), dp.get(i) + 1));
        }
        int answer = dp.get(y);
        // for(int i: dp) System.out.println(i);
        return (answer != DP_MAX_VALUE)?answer:-1;
    }
}