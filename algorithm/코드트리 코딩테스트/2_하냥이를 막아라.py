# 하냥이가 먹는 함수
def ha(n, h, box):
    count = 0
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    go = 1
    location = [n//2, n//2]
    dr = -1
    eat = 0
    while(count < n * n):
        for i in range(2):
            dr += (1 if(dr != 3) else - 3)
            for j in range(go):
                location[0] += direction[dr][0]
                location[1] += direction[dr][1]
                if(location[0] < 0 or location[0] == n or location[1] < 0 or location[1] == n): return 0
                count += 1
                eat += box[location[0]][location[1]]
                if(eat >= h):
                    return count
        go += 1
    return 0

# 2배로 만드는 함수
def double(x, y, box):
    box[x][y] *= 2
    if(x != 0): box[x - 1][y] *= 2 
    if(x != n - 1): box[x + 1][y] *= 2
    if(y != 0): box[x][y - 1] *= 2
    if(y != n - 1): box[x][y + 1] *= 2

# n^2 크기의 박스. n은 홀수 3<= n <= 49
# 위 쪽을 먼저 가고 시계 방향의 소용돌이 형태로 돌아다님.
# 방문하는 모든 부스의 간식을 먹음
# 최소 h 개 먹어야함. 1 <= h <= 10,000

# 리온이는 한 부스 선택하고 선택 시 해당 부스랑 상하좌우 2배로 늘려줌
# 단, 범위 밖은 무시됨.
# 하냥이가 방문할 부스 수를 최소화하려면 어떤 부스를 선택해야하는 지 구하시오.
# 준비된 간식 수는 0 ~ 50

# 규칙 : [위, 오, 밑, 왼] [x, x, x + 1, x + 1] 위 1, 오 1, 밑 2, 왼 2, 위 3, 오 3, 밑 4, 왼 4
n, h = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
answer = []
for x in range(n):
    for y in range(n):
        boxCopy = []
        for b in box:
            boxCopy.append(b[:])
        double(x, y, boxCopy)
        result = ha(n, h, boxCopy)
        if(result):
            answer.append(result)
print(min(answer) if(len(answer)) else "HUNGRY")
