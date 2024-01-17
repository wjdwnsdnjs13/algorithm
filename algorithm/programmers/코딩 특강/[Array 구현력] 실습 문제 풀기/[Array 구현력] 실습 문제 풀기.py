from math import ceil

def solution(fees, records):
#     입차, 출차 기록이 주어졌을 때 주차 요금 계산
#     출차 내역이 없으면 23:59에 출차된 것으로 간주.
#     기본 요금 초과 시 기본요금 + 초과한 시간에 대해 단위 시간마다 단위 요금 청구함.
#      -> 초과 시간이 단위 시간으로 나누어 떨어지지 않으면 올림.
        
#     fees : 주차 요금을 나타내는 정수 배열
#     records : 입/출차 내역을 나타내는 배열 ["시각 차량번호 내역"], 시각을 기준으로 오름차순 정렬되어 있음.
#     return 차량 번호 오름차순으로 주차 요금을 담은 배열 리턴
    carList = {}
    for record in records:
        t, carNumber, flag = record.split(" ")
        hour, minute = map(int, t.split(":"))
        time = minute + hour * 60
        # carList : [입차시간, 사용한 시간, flag(출차여부)]
        # 출차 시 사용한 시간 최신화하고, 입차 시간 0으로 만듦.
        # 만약 0이 아닐 경우 사용한 시간을 입차시간부터 23:59에 나간거로 최신화
        # 1. 최초 입차 : 만들기만 하면 됨.
        # 2. 중복 입차 : 입차시간만 최신화.
        # 3. 출차 : 이전 시간 계산해서 넣고, falg 0으로 만듦.
        if(flag == "IN"):
            if(carNumber not in carList):
                carList[carNumber] = [time, 0, 1]
            else:
                carList[carNumber][0] = time
                carList[carNumber][2] = 1
        else:
            carList[carNumber][1] += time - carList[carNumber][0]
            carList[carNumber][2] = 0
    answer = []
    result = []
    for c in carList:
        if(carList[c][2] != 0):
            carList[c][1] += 59 + (23 * 60) - carList[c][0]
        carList[c][1] -= fees[0]
        result.append((c, fees[1] + (fees[3] * ceil(carList[c][1]/fees[2]) if(carList[c][1] > 0) else 0)))
    result.sort()
    for r in result:
        answer.append(r[1])
    return answer