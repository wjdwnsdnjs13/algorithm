class Solution {
    public String solution(int n) {
        String answer = "수박".repeat((int)n/2);
        answer += (n%2 == 1)?"수":"";
        return answer;
    }
}