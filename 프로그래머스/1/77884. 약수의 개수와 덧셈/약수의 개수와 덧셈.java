class Solution {
    // left -> right까지의 수 중에서 약수가 짝수개면 더하고, 홀수 개면 빼고...
    public int solution(int left, int right) {
        int answer = 0;
        for(int i = left; i <= right; i++){
            answer += isMeasureEven(i)?i:-i;
        }
        return answer;
    }
    
    // 약수 계산
    public boolean isMeasureEven(int n){
        int count = 1;
        for(int i = 1; i <= (int) n/2; i++){
            if(n%i == 0) count++;
        }
        return (count%2 == 0);
    }
}