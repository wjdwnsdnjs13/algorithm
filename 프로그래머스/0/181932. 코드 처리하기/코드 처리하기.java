class Solution {
    public String solution1(String code) {
        // "1"이 있으면 mode 변경.
        // mode에 따라 ret 문자열을 만듦.
        // mode = 0 : 인덱스 짝수일 경우에만 ret에 추가
        // mode = 1 : 인덱스 홀수일 경우에만 ret에 추가
        
        int mode = 0;
        String answer = "";
        for(int i = 0; i < code.length(); i++){
            char c = code.charAt(i);
            if(c == '1') mode = (mode == 0)?1:0;
            else if(i%2 == mode) answer += c; 
        }
        return answer.isEmpty()?"EMPTY":answer;
    }
    
    public String solution(String code) {
        // "1"이 있으면 mode 변경.
        // mode에 따라 ret 문자열을 만듦.
        // mode = 0 : 인덱스 짝수일 경우에만 ret에 추가
        // mode = 1 : 인덱스 홀수일 경우에만 ret에 추가
        
        int mode = 0;
        String answer = "";
        String[] codes = code.split("");
        for(int i = 0; i < codes.length; i++){
            String c = codes[i];
            if(c.equals("1")) mode = (mode == 0)?1:0;
            else if(i%2 == mode) answer += c; 
        }
        return answer.isEmpty()?"EMPTY":answer;
    }
}