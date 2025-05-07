class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
//         놀이기구의 원래 이용료가 price원이다.
//         n번째 이용 시 n배 받음.
//         count번 탔을 때 모자란 금액은?
//         부족하지 않으면 0을 리턴
        var answer = money.toLong()
        for(i in 1..count){
            answer -= price * i
        }
        return if (answer > 0) 0 else -answer
    }
}