class Solution {
    public int solution(int a, int b) {
        String result = Integer.toString(a) + Integer.toString(b);
        String result2 = Integer.toString(b) + Integer.toString(a);
        int answer = Math.max(Integer.parseInt(result), Integer.parseInt(result2));
        return answer;
    }
}