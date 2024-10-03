def solution(wallet, bill):
    # 지폐를 넣을거임.
    
    # 지폐는 항상 길이가 긴 쪽을 반으로 접음
    # 홀수 -> 소수점 이하 버림
    # 그대로 혹은 90도 회전해서 넣을 수 있으면 가능.
    # 지폐를 접는 최소 횟수
    answer = 0
    while(pushPoket(wallet, bill)):
        answer += 1
        if(bill[0] > bill[1]): bill[0] //= 2
        else: bill[1] //= 2
    return answer

def pushPoket(wallet, p):
    if(wallet[0] >= p[0] and wallet[1] >= p[1]): return False
    elif(wallet[0] >= p[1] and wallet[1] >= p[0]): return False
    return True