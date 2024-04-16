class Solution {
    public int solution(int a, int b, int c) {
        int answer = a + b + c;
        if(a == b || a == c || b == c) answer *= (int) Math.pow(a, 2) + (int) Math.pow(b, 2) + (int) Math.pow(c, 2);
        if(a == b && b == c) answer *= (int) Math.pow(a, 3) + (int) Math.pow(b, 3) + (int) Math.pow(c, 3);
        return answer;
    }
}