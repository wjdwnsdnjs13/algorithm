def solution(dartResult):
    answer = 0
    prev = 0
    i = -1
    bonus = { "S" : 1, "D" : 2, "T" : 3}
    while(i < len(dartResult) - 1):
        i += 1
        # for문에서는 다음 스텝이 시작될 때 i가 초기화되어서 +1 되고 시작됨.
        squre = 1
        option = 1
        if dartResult[i + 1] == '0':
            score = int(dartResult[i:i + 2])
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
        squre = bonus[dartResult[i]]
        if i < len(dartResult) - 1:
            if dartResult[i + 1] == "*":
                prev *= 2
                option = 2
            elif dartResult[i + 1] == "#": option = -1
        if option != 1: i += 1
        answer += prev
        prev = score ** squre * option
    answer += prev
    return answer