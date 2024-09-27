import java.lang.Math;

class Solution {
    public int solution(int number, int limit, int power) {
//         기사는 1번부터 number까지 번호 지정
//         무기는 자신 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매
        
//         제한 수치가 있음.
//         이때는 협약 기관에서 정한 공격력의 무기를 구매해야함.
        
//         공격력 1당 철 1kg
//         필요한 철의 무게를 계산할거임.
       
        int count = 0;
        int answer = 0;
        // 약수 계산
        for(int i = 1; i <= number; i++){
            count = calc(i);
            answer += (count > limit)?power:count;
        }
        return answer;
    }
    
    public int calc(int number){
        if(number == 1) return 1;
        int result = 2; //1, 본인
        for(int i = 2; i < Math.pow(number, 0.5); i++){
            if(number%i == 0) {
                result += 2;
            }
        }
        if(number%Math.pow(number, 0.5) == 0) result++;
        return result;
    }
}