from itertools import product

def solution(numbers, target):
    # numbers : 사용해야하는 숫자 목록
    # target : 목표 값
    # return : target을 만들 수 있는 방법
    # numbers에 있는 숫자를 더하거나 빼서 타켓 넘버를 만들어야 함.
    
    # product(l)은 l이라는 리스트 전체로 하나를 넘김.
    # *l은 리스트 요소 하나하나 넘김.
    # prouct()는 리스트 요소의 곱집합을 넘겨줌.
    l = [(n, -n) for n in numbers]
    result = list(map(sum, product(*l)))
    return result.count(target)

def solution2(numbers, target):
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

def solution3_use_zip(numbers, target):
    # numbers : 사용해야하는 숫자 목록
    # target : 목표 값
    # return : target을 만들 수 있는 방법
    # numbers에 있는 숫자를 더하거나 빼서 타켓 넘버를 만들어야 함.
    
    # 각 숫자에 (-1)을 곱하거나 (+1)을 곱한 값을 완전 탐색해서 합이 target인 경우 answer += 1
    symbol = list(product([-1, 1], repeat = len(numbers)))
    answer = 0
    for s in symbol:
        result = 0
        for x, y in zip(s, numbers):
            result += (x * y)
        answer += 1 if(result == target) else 0
    return answer