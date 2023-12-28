class Solution {
    public int[] solution(long n) {
        // long으로 들어온 n
        // String으로 변환 후 그걸 List로 넣으면 될 거 같은데
        
        String str = Long.toString(n);
        int strLength = str.length();
        int[] answer = new int[strLength];
        for(int i = strLength - 1; i >= 0; i--){
            answer[strLength - i - 1] = str.charAt(i) - '0';
        } 
        return answer;
    }
}