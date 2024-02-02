from itertools import product

def solution(numbers, target):
    # numbers : 사용해야하는 숫자 목록
    # target : 목표 값
    # return : target을 만들 수 있는 방법
    # numbers에 있는 숫자를 더하거나 빼서 타켓 넘버를 만들어야 함.
    
    # 각 숫자에 (-1)을 곱하거나 (+1)을 곱한 값을 완전 탐색해서 합이 target인 경우 answer += 1
    symbol = list(product([-1, 1], repeat = len(numbers)))
    answer = 0
    
    for s in symbol:
        result = 0
        for i in range(len(s)):
            result += numbers[i] * s[i]
        answer += 1 if(result == target) else 0
    
    return answer