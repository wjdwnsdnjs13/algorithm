def solution(survey, choices):
    answer = ''
    mbti = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    score = {1 : 3, 2 : 2, 3 : 1, 5 : 1, 6 : 2, 7 : 3}
    for s, c in zip(survey, choices):
        if c == 4:
            continue
        if c < 4:
            mbti[s[0]] += score[c]
        else:
            mbti[s[1]] += score[c]
    answer += "T" if mbti["R"] < mbti["T"] else "R"
    answer += "F" if mbti["C"] < mbti["F"] else "C"
    answer += "M" if mbti["J"] < mbti["M"] else "J"
    answer += "N" if mbti["A"] < mbti["N"] else "A"
    return answer