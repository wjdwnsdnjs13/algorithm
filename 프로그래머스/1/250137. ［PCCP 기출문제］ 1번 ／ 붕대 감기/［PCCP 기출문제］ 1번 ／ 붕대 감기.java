class Solution {
    
    public int solution(int[] bandage, int health, int[][] attacks) {
//         붕대는 t초 동안 감으면서, 1초에 x만큼의 체력을 회복함.
//         끊기지 않으면 y 만큼 추가 회복함.
//         최대 체력 이상은 불가능.
//         공격 당하면 기술 취소되고, 그 순산에는 체력 회복 x
//         붕대감기는 무한 반복됨.
//         체력이 0 이하가 되면 사망.
        
//         모든 공격 직후 체력 or 죽으면 -1 리턴
        
        // 풀피일 때 연속 회복 성공 시간은 필요 없음 -> 어차피 공격당하면 회복 x, 초기화
        
        int answer = health;
        for(int i = 0; i < attacks.length; i++){
            answer -= attacks[i][1];
            
            // 피 0 이하면 사망
            if(answer <= 0) return -1;
            
            // 마지막이 아니면 힐
            if(i != attacks.length - 1){
                int time = attacks[i + 1][0] - attacks[i][0] - 1;

                // 피 계산
                answer += bandage[1] * time + time/bandage[0] * bandage[2];
                if(answer > health) answer = health;                
            }
        }
        return answer;
    }
}