import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 한 명 빼고 전원 완주
        // participant : 완주자 명단
        // completion : 완주한 선수
        // 완주 못 한 사람 이름 리턴
        // 1 <= 참여자 수 <= 100,000
        // 동명이인 있을 수도 있음.
        
        Arrays.sort(participant);
        Arrays.sort(completion);
        String answer = "";
        for(int i = 0; i < participant.length; i++){
            if(i + 1 == participant.length || !participant[i].equals(completion[i])){
                answer = participant[i];
                break;
            }
        }
        
        return answer;
    }
}