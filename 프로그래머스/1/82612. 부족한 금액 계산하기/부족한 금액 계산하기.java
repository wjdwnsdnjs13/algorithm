class Solution {
    public long solution(int price, int money, int count) {        
//         놀이기구의 원래 이용료가 price원이다.
//         n번째 이용 시 n배 받음.
//         count번 탔을 때 모자란 금액은?
//         부족하지 않으면 0을 리턴
        long answer = money;
        for(var i = 1; i <= count; i++){
            answer -= price * i;
        }
        
        return (answer > 0)?0:-answer;
    }
}