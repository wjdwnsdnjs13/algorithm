def solution(a, b):
    x = 0
    for i in range(min(a, b), max(a, b) + 1): x += i
    return x