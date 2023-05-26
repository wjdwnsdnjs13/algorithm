def solution(want, number, discount):
    answer = 0
    check = dict()
    for i in range(len(want)):
            check[want[i]] = number[i]
    for i in range(len(discount) - 10):        
        for j in range(i, i + 10):
            if discount[j] in check and check[discount[j]] != 0:
                check[discount[j]] -= 1
        flag = True
        for c in check:
            if check[c] != 0:
                flag = False
        answer += (1 if flag else 0)
    return answer