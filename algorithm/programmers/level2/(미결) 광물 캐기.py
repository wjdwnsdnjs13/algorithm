def solution(picks, minerals):
# 각 곡괭이는 5개 까지만 캘 수 있음.
# 최소 피로도로 광물 캘 거임.
# picks는 곡괭이의 수
# [dia, iron, stone]
# 한번 사용한 곡괭이는 사용할 수 없을 때까지 사용함.
# 광물은 순서대로만 캘 수 있음.

    # 테이블 표 만들기
    table = [{'diamond' : 1, 'iron' : 1, 'stone' : 1},
             {'diamond' : 5, 'iron' : 1, 'stone' : 1},
             {'diamond' : 25, 'iron' : 5, 'stone' : 1}
            ]
    answer = [0 for _ in range(len(minerals) - sum(picks) * 5)]
    answer.append(0)
    print(answer)
    # minerals를 5등분해서 부분별로 각 곡괭이로 캤을 때 총 피로도 계산.
    calcTable = []
    count = 0
    score = [0, 0, 0]
#     곡괭이 수 * 5 이상의 광물은 제외 시켜야함.
    minerals = minerals[:sum(picks) * 5 + 1]
    for i in range(len(minerals)):
        count += 1
        for j in range(3):
            score[j] += table[j][minerals[i]]
        if(count == 5):
            count = 0
            calcTable.append(score[:])
            score = [0, 0, 0]
        
    else:
        if(count != 0):
                calcTable.append(score[:])
#     각 곡괭이 수 만큼, 곡괭이 종류에 따른 점수 차이가 큰 것부터 계산.
    calcTable.sort(key = (lambda x: x[2]))
    check = [False for _ in range(len(calcTable))]
#     calcTable 길이만큼 점수 합산하기
#     picks 돌면서 체크안된 나무 곡괭이 점수 젤 높은애부터 고르기
    for i in range(len(picks)):
        if(picks[i] == 0): continue
        if(not calcTable): break
        picks[i] -= 1
        # answer[0] += calcTable.pop()[i]
    
    return answer