def solution(price, money, count):
    # 놀이기구 원가는 price
    # n번 이용 시 원가의 n배 받음
    # count번 탔을 때 갖고 있는 금액에서 얼마나 모자라는 지?
#     부족하지 않으면 0 리턴
    for i in range(1, count + 1):
        money -= price * i
    answer = -money if(money < 0) else 0
    return answer