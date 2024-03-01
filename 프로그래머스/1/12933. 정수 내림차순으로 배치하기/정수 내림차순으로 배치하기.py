def solution(n):
    answer = ""
    tmp = []
    for i in str(n):
        tmp.append(i)
    tmp.sort(reverse = True)
    for t in tmp:
        answer += t
    return int(answer)