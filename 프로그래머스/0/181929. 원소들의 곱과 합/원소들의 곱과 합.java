import java.util.*;

class Solution {
    public int solution1(int[] num_list) {
        int multiple = 1;
        int square = 0;
        for(int n: num_list) multiple *= n;
        for(int n: num_list) square += n;
        square = (int) Math.pow(square, 2);
        int answer = (multiple < square)?1:0;
        System.out.println(multiple + ", " + square);
        return answer;
    }
    
    public int solution(int[] num_list) {
        int multiple = 1;
        for(int n: num_list) multiple *= n;
        int square = (int) Math.pow(Arrays.stream(num_list)
            .sum(), 2);
        int answer = (multiple < square)?1:0;
        System.out.println(multiple + ", " + square);
        return answer;
    }
}