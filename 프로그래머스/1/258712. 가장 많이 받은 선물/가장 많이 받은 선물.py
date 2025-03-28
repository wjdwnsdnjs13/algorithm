def solution(friends, gifts):
#     friends 길이 <= 50
#     Uk 이고, 10글자 이하 소문자로 이루어짐
#     gifts 길이 <=10_000
#     "A B" 형태, "{선물_준_사람_이름} {선물_받은_사람_이름}"
    
    giftLog = {f: {a: 0 for a in friends if(f != a)} for f in friends}
    
    # gifts를 돌면서 A는 지수 +1, B는 지수 -1
    giftIndicator = {f: 0 for f in friends}
    
    # 선물 지수 : (이번 달까지 자신이 준 선물) - (받은 선물)
    for gift in gifts:
        a, b = gift.split()
        giftIndicator[a] += 1
        giftIndicator[b] -= 1
        giftLog[a][b] += 1
        
    answer = {f : 0 for f in friends}
    for col in giftLog:
        for row in giftLog[col]:
            # A : 서로 주고 받은 경우 이번 달에 더 많은 선물을 준 사람이 다음 달에 하나 더 받음.
            if(giftLog[col][row] > giftLog[row][col]):
                answer[col] += 1
            # B : 기록이 없거나, 서로 같은 양의 선물을 줬으면 '선물 지수'가 더 큰 사람이 선물 하나 받음
            elif(giftLog[col][row] == giftLog[row][col] and giftIndicator[col] > giftIndicator[row]):
                answer[col] += 1
            # C : 선물 지수도 동일하면 선물 주고 받지 않음.
            else:
                continue
            
    return max(answer.values())