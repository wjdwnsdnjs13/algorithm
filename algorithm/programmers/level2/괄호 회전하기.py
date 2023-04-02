# 14번 케이스 해결 해야됨
# ({)} 등
def solution(s):
    answer = 0
    for i in range(len(s) - 1):
        text = s[i:] + s[:i]
        one, two, three = 0, 0, 0
        for t in text:
            one += 1 if t == "[" else -1 if t == "]" else 0
            two += 1 if t == "(" else -1 if t == ")" else 0
            three += 1 if t == "{" else -1 if t == "}" else 0
            if one < 0 or two < 0 or three < 0:
                break
        else:
            if one == 0 and two == 0 and three == 0:
                answer += 1
    return answer