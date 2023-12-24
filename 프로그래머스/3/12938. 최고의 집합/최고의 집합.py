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
    
    # s를 n으로 나누면 될 거 같은데
    # number = s//n
    # count = s%n
    # result에 number를 나누어 떨어지면 n만큼 넣고 아니면 n -1 만큼 넣은 후 number + count 하나 넣고
    
    number = s//n
    count = s%n
    if(not s//n): return [-1]
    answer = [number for i in range(n)]
    if(count):
        for i in range(1, count + 1):
            answer[-i] += 1
    
    return answer