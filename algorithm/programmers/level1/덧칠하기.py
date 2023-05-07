def solution(n, m, section):
    answer = 1
    point = section[0] + m
    while(point <= section[-1]):
        for s in section:
            if s < point:
                continue
            else:
                answer += 1
                point = s + m
    return answer