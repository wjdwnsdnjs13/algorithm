def solution(players, callings):
#     추월 시 추월한 선수의 이름 부름.
#     LinkedList dictionary로 구현하기.
#     해당 선수 이름 key, 앞 뒤 선수 이름 value
#     추월 계산하려면 뒤 선수 이름도 필요함.
    answer = []
    playerRanking = {player : i for i, player in enumerate(players)}
    
    for calling in callings:
        rank = playerRanking[calling]
        if(rank == 0): countinue
        
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
        
        playerRanking[calling] -= 1
        playerRanking[players[rank]] += 1

        
    # for c in callings:
        # playerDic[players[i]] -= 1
    return players


def solution2(players, callings):
#     추월 시 추월한 선수의 이름 부름.
#     LinkedList dictionary로 구현하기.
#     해당 선수 이름 key, 앞 뒤 선수 이름 value
#     추월 계산하려면 뒤 선수 이름도 필요함.
    answer = []
    playersDic = {}
    for i in range(len(players)):
        if(i == 0):
            playersDic[players[i]] = ["first", players[i + 1]]
            playersDic["first"] = players[i]
        elif(i == len(players) - 1):
            playersDic[players[i]] = [players[i - 1], "last"]
            playersDic["last"] = players[i]
        else:
            playersDic[players[i]] = [players[i - 1], players[i + 1]]
            
#     callings를 for문 돌리고 이름 나오면 앞 이름과 스왑
    for c in callings:
#         a, b, c(불린 애), d 라고 하면
#         1. a, b, d를 저장
#         2. dic[c] = [a, b]
#         3. dic[a][1] = c
#         4. dic[b] = [c, d]
#         5. dic[d][0] = b
#         이름 불린 선수 뒤 선수 저장
        b = playersDic[c][0]
        a = playersDic[b][0]
        d = playersDic[c][1]
        
#         불린 선수가 맨 마지막일 경우 생각
#         앞 선수가 1등일 경우 생각
        if(d == "last"):
            playersDic["last"] = b
            playersDic[b] = [c, "last"]
            playersDic[c] = [a, b]
        elif(a == "first"):
            playersDic["first"] = c
            playersDic[c] = ["first", b]
            playersDic[b] = [c, d]
            playersDic[d][0] = b
        else:
            playersDic[c] = [a, b]
            playersDic[a][1] = c
            playersDic[b] = [c, d]
            playersDic[d][0] = b
    player = playersDic["first"]
    while(player != "last"):
        answer.append(player)
        player = playersDic[player][1]
    return answer