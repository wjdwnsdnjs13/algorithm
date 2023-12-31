class Solution {
    public String solution(String s) {
        // 삼항 연산자로 많이 줄일 수 있음.
        StringBuilder answer = new StringBuilder();
        int count = 0;
        String[] sArray = s.split("");
        for(String ss: sArray){
            count = ss.equals(" ")?0:count + 1;
            if(count%2 == 1) answer.append(ss.toUpperCase());
            else answer.append(ss.toLowerCase());
            
        }
        return answer.toString();
    }
}