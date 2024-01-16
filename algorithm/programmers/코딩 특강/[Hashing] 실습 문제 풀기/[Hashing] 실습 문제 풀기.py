def solution(id_list, report, k):
    # 한 번에 한 명만 신고 가능하고 횟수 제한 x, 서로 다른 유저 계속 신고 가능, 한 유저 여러번 신고해도 1회로 처리됨.
    # k번 이상 신고된 유저는 정지되면서 신고한 모든 유저에게 정지 사실 메일로 알려줌.
    #  -> 모든 신고 내용은 취합해서 마지막에 한번에 정지 메일 발송.
    
    # id_list : 이용자 id 목록
    # report : 신고한 이용자의 id 정보가 담긴 목록 ["신고자 피신고자"]
    # k : 정지되는 기준 횟수
    # return : 각 유저 별로 처리 결과 메일을 받은 횟수 배열

    userList = {i : [] for i in id_list}
    answer = {i : 0 for i in id_list}
    for r in report:
        complainant, accused = r.split(" ")
        if(complainant not in userList[accused]):
            userList[accused].append(complainant)
    for u in userList:
        if(len(userList[u]) >= k):
            for user in userList[u]:
                answer[user] += 1
    return [answer[a] for a in answer]