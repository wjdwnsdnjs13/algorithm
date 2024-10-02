class Solution {
    public int solution(String number) {
        if(number.equals("0")) return 0;
        int answer = 0;
        for(int i = 0; i < number.length(); i++){
            answer += number.charAt(i) - '0';
        }
        return answer%9;
    }
}