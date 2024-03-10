import math

def solution(fees, records):
#     fees : [기본 시간, 기본 요금, 단위 시간, 단위 요금]
#     records : "시각 차량번호 내역"
    
#     요금 관리할 dictionary 필요.
#     출차여부 관리할 dictionary 필요.
    # 23:59까지 출차 없으면 그때 강제 출차
    
    # car : {번호 : [누적 시간, 최종 입차 시간(출차 시 99999)]}
    answer = []
    car = dict()
    print(24 * 60)
    for r in records:
        t, n, p = r.split()
        t = int(t[:2]) * 60 + int(t[3:])
        if(p == "IN"):
            if(n in car):
                car[n][1] = t
            else:
                car[n] = [0, t]
        else:
            car[n][0] += t - car[n][1]
            car[n][1] = 99999
    print(car)
    tmp = [] # 정렬을 위해 잠시 데이터 담아둘 리스트
    for key in car:
        if(car[key][1] != 99999):
            car[key][0] += 23 * 60 + 59 - car[key][1]
        money = fees[1]
        car[key][0] -= fees[0]
        money += math.ceil(car[key][0]/fees[2]) * fees[3] if(car[key][0] > 0) else 0
        tmp.append([key, money])
    tmp.sort()
    for t in tmp:
        answer.append(t[1])

    return answer