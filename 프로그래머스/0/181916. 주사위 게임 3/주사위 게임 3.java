import java.util.*;
import java.lang.Math;

class Solution {
    Map<Integer, Integer> numbers;
    
    public int solution(int a, int b, int c, int d) {
        // 4개의 주사위를 굴림.
        // 모두 같은 숫자 p이면 (1111 * p)점 얻음
        // 3개가 같으면 (10 * p + q)^2
        // 2개 씩이면 (p + q) * abs(p - q)
        // 2개 같고, 나머지가 다르면 q * r점 얻음.
        // 다 다르면 가장 작은 숫자에 해당하는 점수.
        int answer = 0;
        
        // Map에 넣고 카운트 비교해서 점수 부여
        numbers = new HashMap();
        numbersAppend(a);
        numbersAppend(b);
        numbersAppend(c);
        numbersAppend(d);
        
        // 점수 부여 프로세스
        Set<Integer> key = numbers.keySet();
        if(numbers.size() == 1) return 1111 * a;
        else if(numbers.size() == 2){
            Iterator<Integer> iterator = key.iterator();
            int one = iterator.next();
            int two = iterator.next();
            if(numbers.get(one) == 2) return (one + two) * Math.abs(one - two);
            else{
                int result = (numbers.get(one) > numbers.get(two))?(10 * one + two):(10 * two + one);
                return (int) Math.pow(result, 2);
            }
        } else if(numbers.size() == 3){
            answer = 1;
            for(Integer i: key) answer *= (numbers.get(i) == 1)?i:1;
            return answer;
        } else{
            return Collections.min(numbers.keySet());
        }
        
    }
    public void numbersAppend(int x){
        if(numbers.containsKey(x)){
            numbers.put(x, numbers.get(x) + 1);
        }
        else{
            numbers.put(x, 1);
        }
    }
}