def solution(schedules, timelogs, startday):
#     일주일 간 출근 희망일을 지키면 상품
#     출근 희망 시각 + 10분까지 출근
#     *토, 일은 이벤트 영향 x
#     직원 n명 <= 1000
#     schedules : 출근 희망 시간
#     timelogs : 출근 시간 2차원 배열
#     startday : 이벤트 시작 요일
    
#     직원 1000명에 출근도 7개까지라 완탐 가능
    
#     시간에 00시는 없음
    
#     1(월) ~ 7(일)
#     6, 7은 그냥 건너 띄면 됨
    count = [0 for _ in range(len(schedules))]
    
    # 스케쥴 형식 변경
    for i in range(len(schedules)):
        schedules[i] = timeCalc(schedules[i])
    
    for i in range(7):
        if(startday == 6 or startday == 7): 
            startday += 1 if(startday != 7) else -6    
            continue
        for j in range(len(schedules)):
            if(schedules[j] + 10 >= timeCalc(timelogs[j][i])): count[j] += 1
        startday += 1 if(startday != 7) else -6

    answer = 0
    for c in count:
        if(c == 5): answer += 1
    return answer

# 시간 계산 함수
def timeCalc(t):
    t = str(t)
    h = int(t[:-2])
    m = int(t[-2:])
    return h * 60 + m