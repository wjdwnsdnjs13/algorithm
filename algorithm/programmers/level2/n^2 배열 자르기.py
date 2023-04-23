def solution(n, left, right):
    alpha = left//n + 1
    answer = (([alpha] * (alpha)) + list(range(alpha + 1, n + 1)))[left%n:]
    while(len(answer) < (right - left + 1)):
        x = left + len(answer)
        alpha = x//n + 1
        answer += ([alpha] * (alpha)) + list(range(alpha + 1, n + 1))
    return answer[:right - left + 1]