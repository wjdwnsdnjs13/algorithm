import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
//         n개의 퍼즐을 순서대로 풀어야함.
//         diff : 퍼즐 난이도
//         time_cur : 푸는데 걸리는 시간
//         time_prev : 이전 퍼즐 소요 시간
//         level : 숙련도
            
//         숙련도가 부족하면 그 차이 * time_prev 시간 사용 후 다시 풀어야함.
        
//         제한시간 limit 안에 모든 퍼즐을 풀 수 있는 숙련도의 최소값.
//             -> 이진탐색
        int answer = 999999999;
        int s = 1;
        int e = max(diffs);
        while(s <= e){
            int mid = (s + e) / 2;
            long result = 0;
            for(int i = 0; i < diffs.length; i++){
                if(i == 0) result += puzzling(mid, diffs[i], times[i], 0);
                else result += puzzling(mid, diffs[i], times[i], times[i - 1]);
            }

            if(result <= limit) {
                answer = Math.min(answer, mid);
                e = mid - 1;
            }
            else s = mid + 1;
        }
        return answer;
    }
    
    public int puzzling(int level, int diff, int time, int prev){
        if(level >= diff) return time;
        return time + (diff - level) * (time + prev);
    }
    
    public int max(int[] array){
        int result = 0;
        for(int i: array) result = (result > i)?result:i;
        return result;
    }
}