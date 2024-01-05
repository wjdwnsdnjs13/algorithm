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
}