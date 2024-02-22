def solution(n):
    answer = 0
    for i in range(1, 1000000):
        if n%i == 1:
            answer = i
            break
    return answer