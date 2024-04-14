class Solution {
    public int solution(int a, int b) {
        String result1 = "" + a + b;
        int result2 = 2 * a * b;
        int answer = Math.max(Integer.parseInt(result1), result2);
        return answer;
    }
}