# 이코테 341p 백준 14502 연구소
# 시간 초과 #pypy3로 제출하자ㅠㅠ
n, m = map(int, input().split())
graph = []
data_copy = [[0] * m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#virus 퍼트리는 함수
def virus(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if data_copy[nx][ny] == 0:
                data_copy[nx][ny] = 2
                virus(nx, ny)

#0카운팅 함수
def counting():
    score = 0
    for i in range(n):
        for j in range(m):
            if data_copy[i][j] == 0:
                score += 1
    return score

#벽 세우고 계산하는 함수
result = 0
def dfs(count):
    global result
    if count == 3:
        #맵 카피
        for i in range(n):
            for j in range(m):
                data_copy[i][j] = graph[i][j]
        #바이러스 퍼트리기
        for i in range(n):
            for j in range(m):
                if data_copy[i][j] == 2:
                    virus(i, j)
        #카운팅
        result = max(result, counting())
        #여기오면 중지 시켜 줘야지...;;
        return
    #3이 아닌 경우
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
                graph[i][j] = 1
                dfs(count)
                count -= 1
                graph[i][j] = 0
dfs(0)
print(result)