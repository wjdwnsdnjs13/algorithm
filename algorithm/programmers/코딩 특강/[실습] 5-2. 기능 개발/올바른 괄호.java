import java.util.*;
import java.util.stream.*;

class Solution {
    boolean solution(String s) {
        // (와 )의 갯수 카운팅으로 음수가 되면 false
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(count < 0) return false;
            if(String.valueOf(s.charAt(i)).equals("(")) count++;
            else count--;
        }
        
        return count == 0;
    }
    
    boolean solutionUseStringArray(String s) {
        // (와 )의 갯수 카운팅으로 음수가 되면 false
        String[] str = s.split("");
        int count = 0;
        // Arrays.stream(str).forEach(v -> System.out.print(v));
        for(int i = 0; i < str.length; i++){
            if(count < 0) return false;
            if(str[i].equals("(")) count++;
            else count--;
        }
        
        return count == 0;
    }
    
    boolean solutionUseQueue(String s) {
        // (와 )의 갯수 카운팅으로 음수가 되면 false
        // Queue 사용하면 될 듯
        Queue queue = new LinkedList<>(Arrays.asList(s.split("")));
        int count = 0;
        while(queue.size() != 0){
            if(count < 0) return false;
            if(queue.poll().equals("(")) count++;
            else count--;
        }
        
        return count == 0;
    }
}