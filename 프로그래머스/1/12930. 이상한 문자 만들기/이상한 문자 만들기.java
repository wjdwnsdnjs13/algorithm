class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(String.valueOf(s.charAt(i)).equals(" ")) count = -1;
            if(count%2 == 0) answer.append(String.valueOf(s.charAt(i)).toUpperCase());
            else answer.append(String.valueOf(s.charAt(i)).toLowerCase());
            count++;
        }
        return answer.toString();
    }
}