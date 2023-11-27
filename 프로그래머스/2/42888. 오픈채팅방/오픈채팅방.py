def solution(record):
    result = []
    nameDic = {}
    # record가 빌 때까지 반복
    # Enter 시 [uid, "님이 들어왔습니다."]
    # change 시 딕셔너리 내의 정보 수정
    # Leave 시 [uid, "님이 나갔습니다."]
    # result에 삽입
    for r in record:
        if(r[0] == "L"):
            command, uid = r.split()
            result.append([uid, "님이 나갔습니다."])
        else:
            command, uid, name = r.split()
            if(command == "Enter"):
                result.append([uid, "님이 들어왔습니다."])
                nameDic[uid] = name
            else:
                nameDic[uid] = name
    # 반복문 종료 후 answer에 uid 비교하여 최종 값 삽입
    answer = [nameDic[r[0]] + r[1] for r in result]
    return answer