def solution(X, Y):
    answer = ''
    x = {}
    y = {}
    for i in range(len(X)):
        t = int(X[i])
        x[t] = 1 if t not in x else (x[t] + 1)

    for i in range(len(Y)):
        t = int(Y[i])
        y[t] = 1 if t not in y else (y[t] + 1)
    for i in range(9, -1, -1):
        if (i not in x) or (i not in y): continue
        for j in range(min(x[i], y[i])):
            answer += str(i)
    if answer == '':
        return "-1"
    elif answer[0] == "0":
    # elif int(answer) == 0: #얘는 answer 길이가 길 때 시간 초과가 난다고 함.
        return "0"
    return answer