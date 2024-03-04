def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer


def solution2(X, Y):
    # 짝궁 : 임의의 자리에서 공통으로 나타나는 정수를 이용해서 가장 큰 정수
    # return : 짝궁 있으면 짝궁, 없으면 -1, 0일 경우엔 0
    answer = ''
    x = {}
    y = {}
    tmp = []
    for p in X:
        if(p in x): x[p] += 1
        else: x[p] = 1
    for p in Y:
        if(p in y): y[p] += 1
        else: y[p] = 1
    for p in x:
        if(p in y and p in x):
            for i in range(min(x[p], y[p])):
                tmp.append(int(p))
    answer = "".join(tmp.sort(reverse=True))
#     for i in range(len(X)):
#         t = int(X[i])
#         x[t] = 1 if t not in x else (x[t] + 1)

#     for i in range(len(Y)):
#         t = int(Y[i])
#         y[t] = 1 if t not in y else (y[t] + 1)
#     for i in range(9, -1, -1):
#         if (i not in x) or (i not in y): continue
#         for j in range(min(x[i], y[i])):
#             answer += str(i)
            
            
    return "-1" if(answer == '') else str(int(answer))