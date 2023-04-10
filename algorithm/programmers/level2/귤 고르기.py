def solution(k, tangerine):
    answer, i = 0, 1
    orange = {}
    for t in tangerine:
        orange[t] = (orange[t] + 1) if t in orange else 1
    count = []
    for o in orange: count.append(orange[o])
    count.sort()
    
    while(0 < k):
        k -= count[-i]
        answer += 1
        i += 1
    return answer