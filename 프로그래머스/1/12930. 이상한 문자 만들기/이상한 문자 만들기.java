class Solution {
    public String solution(String s) {
        // 삼항 연산자로 많이 줄일 수 있음.
        StringBuilder answer = new StringBuilder();
        int count = 0;
        String[] sArray = s.split("");
        for(String ss: sArray){
            count = ss.equals(" ")?0:count + 1;
            answer.append((count%2 == 1)?(ss.toUpperCase()):(ss.toLowerCase()));
            
        }
        return answer.toString();
    }
}