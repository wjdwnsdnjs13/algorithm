class Solution {
    public long solution(long n) {
        long answer = 0;
        double srt = Math.pow(n, 0.5);
        boolean isNumber = srt%1 == 0.0;
        
        return isNumber?(long) Math.pow(srt + 1, 2):-1;
    }
}
