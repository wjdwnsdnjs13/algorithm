def solution(s):
#     ({)} 이런 경우 해결해야 됨
    answer = 0
    for i in range(len(s) - 1):
        text = s[i:] + s[:i]
        one, two, three = 0, 0, 0
        after = ""
        for j in range(len(text)):
            t = text[j]
            after = text[j + 1] if j < (len(text) - 1) else ""
            if t == "[":
                one += 1
                if after == ")" or after == "}": break
            elif t == "]":
                one -= 1
            elif t == "(":
                two += 1
                if after == "]" or after == "}": break
            elif t == ")":
                two -= 1
            elif t == "{":
                three += 1
                if after == ")" or after == "]": break
            elif t == "}":
                three -= 1
            if one < 0 or two < 0 or three < 0:
                break
        else:
            if one == 0 and two == 0 and three == 0:
                answer += 1
    return answer