def solution(a, b, flag):
    answer = a + (b if flag else (-b))
    return answer