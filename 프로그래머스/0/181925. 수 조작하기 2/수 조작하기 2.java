class Solution {
    public String solution(int[] numLog) {
        int prev = numLog[0];
        String answer = "";
        for(int i = 1; i < numLog.length;i++){
            int dif = numLog[i] - prev;
            answer += (dif == 1)?"w":(dif == -1)?"s":(dif == 10)?"d":"a";
            prev = numLog[i];
        }
        
        return answer;
    }
}