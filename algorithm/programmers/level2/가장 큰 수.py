import itertools

def solution(numbers):
    # 1. 첫번째자리 순 정렬
    # 2. 큰 수 순으로 정렬
    answer = ''
    numbers.sort(reverse = True, key=lambda x: (str(x)[0], x))
    for n in numbers:
        answer += str(n)
    
    return answer