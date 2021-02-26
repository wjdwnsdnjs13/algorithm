# 이코테 346p 프로그래머스 60058 괄호 변환
p = str(input())

def index_calc(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    index = index_calc(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution(p))
