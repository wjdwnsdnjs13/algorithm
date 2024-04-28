def solution(s, n):
    s = list(s)
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        a = ord(s[i])
        if a >= 97 and a <= 122 - n:
            s[i] = chr(a + n)
        elif a > 122 - n:
            s[i] = chr(96 + n - (122-a))
        elif a >= 65 and a <= 90 - n:
            s[i] = chr(a + n)
        elif a > 90 - n:
            s[i] = chr(64 + n - (90-a))
        answer += s[i]
    return answer