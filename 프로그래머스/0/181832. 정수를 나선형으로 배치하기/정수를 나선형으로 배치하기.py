def solution(n):
    # n : n * n 배열에 1 ~ n^2 숫자가 나선형으로 들어감.
    # 다음 칸이 배열 범위를 벗어나거나, 값이 있는 경우 시계방향으로 90도 회전
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = [[0 for _ in range(n)] for _ in range(n)]
    d = 0
    go = [0, 0]
    for i in range(1, n ** 2 + 1):
        answer[go[0]][go[1]] = i
        nGo = [go[0] + direction[d][0], go[1] + direction[d][1]]
        if(nGo[0] < n and nGo[0] >= 0 and nGo[1] < n and nGo[1] >= 0 and answer[nGo[0]][nGo[1]] == 0):
            go = nGo
        # 다음 칸이 배열 범위 벗어나거나, 값이 있으면 시계 방향으로 90도 회전
        else:
            d = (d + 1 if(d < 3) else 0)
            go = [go[0] + direction[d][0], go[1] + direction[d][1]]
    return answer