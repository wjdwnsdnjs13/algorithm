def solution(clothes):
    answer = 1
    closet = {}
    for item, kind in clothes:
        if kind not in closet: closet[kind] = 1
        closet[kind] += 1
    for key in closet:
        answer *= closet[key]
    return answer -1