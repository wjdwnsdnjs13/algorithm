from collections import deque

def solution(order):
    # 1부터 n까지 오름차순으로 정렬해서 전달됨.
    # 기사님한테 전달할 때는 선입선출
    # 상자 보관용 보조 컨테이너는 선입후출
    # return 실을 수 있는 상자의 수
    
    q = deque()
    extra_belt = []
    answer = 0
    c = 0
    for i in range(1, len(order) + 1):
        while(extra_belt):
            if(order[c] == extra_belt[-1]):
                extra_belt.pop()
                c += 1
                answer += 1
            else: break
        if(order[c] == i):
            answer += 1
            c += 1
        else:
            extra_belt.append(i)
    while(extra_belt):
            if(order[c] == extra_belt[-1]):
                extra_belt.pop()
                c += 1
                answer += 1
            else: break
    return answer