class Solution {
    public String solution(int q, int r, String code) {
        // code의 각 인덱스를 q로 나눈 나머지가 r인 위치의 문자
        // 앞에서부터 순서대로 이어붙인 문자.
        
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < code.length(); i++){
            if(i%q == r) answer.append(code.charAt(i));
        }
        
        return answer.toString();
    }
}