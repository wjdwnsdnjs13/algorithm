def solution(k, score):
    # 매일 1명이 노래 부름
    # 문자 투표로 점수 부여함
    # 매일 출연한 가수 점수가 출연 가수들 점수 중 k 이내면 해당 가수 점수를 전당에 올림.
    # 즉, k 명의 명예 전당이 유지됨.
    # 매일 명예 전당 최하위 점수를 발표함.
    
    answer = []
    star = []
    for s in score:
        if(len(star) == k):
            if(star[0] < s):
                star[0] = s
                star.sort()
        else:
            star.append(s)
            star.sort()
        answer.append(star[0])
    return answer