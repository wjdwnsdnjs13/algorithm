def solution(mats, park):
    # mats가 10개, 20까지
    # park 길이가 50, 빈 자리는 -1
    # 완탐
    answer = []
    
    mats.sort(reverse = True)
    for mat in mats:
        for x in range(len(park)):
            for y in range(len(park[x])):
                if(x + mat > len(park) or y + mat > len(park[x])): 
                    print("x, y : ", x, y)
                    continue
                if(checkSeat(mat, [p[y:y + mat] for p in park[x:x + mat]])): return mat
    return -1

# 자리 체크
# -1이 아닌 게 하나라도 있으면 안됨.
def checkSeat(k, seats):
    tmp = [s for seat in seats for s in seat]
    s = set(tmp)
    return True if(len(s) == 1 and '-1' in s) else False