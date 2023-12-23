from itertools import combinations_with_replacement

def solution(n, s):
    # 최고 집합 : 중복 집합 중에서 밑 1, 2번 만족하는 집합
    # 1. 각 원소 합이 S
    # 2. 1번 만족하면서, 각 원소의 곱이 최대가 되는 집합
    # 1<= n <= 10,000
    # 1<= 원소의 합 s <= 100,000,000
    
    # 함수 생성하기
    # 1. (n, s) 받기
    # 2. 재귀 함수 : n이 10000이라서 안될 거 같음
    
    
    answer = [-1]
    max_value = 0
    pre_value = 0
    num = [i for i in range(1, s)]
    flag = False
    tmp = list(combinations_with_replacement(num, n))
    for t in tmp:
        if sum(t) == s:
            pre_value = multiply(t)
            if pre_value > max_value:
                answer = t
                
    return answer

def multiply(arr):
    result = 1
    for a in arr:
        if a != 0:
            result *= a
        else:
            return 0
    return result