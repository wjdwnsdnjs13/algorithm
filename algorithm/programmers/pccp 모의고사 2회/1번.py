def solution(command):
    # 로봇은 x, y 좌표로 이동함
    # R : 90도 시계 방향 회전 -> d + 1
    # L : 90도 반시계 방향 회전 -> d - 1
    # G : 1칸 전진
    # B : 1칸 후진
    
    command = list(command)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    x, y = 0, 0
    for c in command:
        if(c == "R"): d += 1 if(d < 3) else - 3
        elif(c == "L"): d -= 1 if(d > 0) else - 3
        elif(c == "G"):
            x += direction[d][0]
            y += direction[d][1]
        else:
            x -= direction[d][0]
            y -= direction[d][1]
    return [x, y]