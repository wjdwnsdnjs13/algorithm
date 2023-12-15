def solution(park, routes):
    # "방향 거리" 꼴로 주어짐.
    # 벗어나거나 장애물을 만나면 해당 명령 무시함.
    # 마지막 위치를 [세로, 가로] 로 리턴.
    # S는 시작, O는 통로, X는 장애물
    for y in range(len(park)):
        for x in range(len(park[0])):
            if(park[y][x] == "S"):
                start = [x, y]
    for r in routes:
        print(move(start, park, r[0], int(r[2])))
        print(start)
    return start[::-1]

def move(start, park, direct, distance):
    x = {"N" : 0, "S" : 0, "E" : 1, "W" : -1}
    y = {"N" : -1, "S" : 1, "E" : 0, "W" : 0}
    go = [x[direct] * distance, y[direct] * distance]
    location = [x + y for x, y in zip(start, go)]
    print(start, go, location)
    if(0 <= location[0] and location[0] < len(park[0]) and 0 <= location[1] and location[1] < len(park)):
        for i in range(1, int(distance) + 1):
            if(park[start[1] + i * y[direct]][start[0] + i * x[direct]] == "X"): return False

        start[0] = location[0]
        start[1] = location[1]
        return True
    return False