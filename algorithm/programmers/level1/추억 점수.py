def solution(name, yearning, photo):
    answer = []
    for p in photo:
        score = 0
        for man in p:
            if man in name:
                score += yearning[name.index(man)]
        answer.append(score)
    return answer