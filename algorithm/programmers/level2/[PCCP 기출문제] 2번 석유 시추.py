from collections import deque

def solution(land):
#     land : 석유가 묻혀있는 상황
#     return : 가장 많이 뽑을 수 있는 석유량

#     시추관이 지나가는 모든 석유 덩어리를 뽑을 수 있음.
#     dfs로 가능
    
    # 500 * 500인데, BFS로 전체 탐색하면 시간초과 나는 이유가 무엇인가?

    answer = [0 for _ in range(len(land[0]))]
    for n in range(len(land[0])):
        result = 0
        visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
        for m in range(len(land)):
            if(not visited[m][n]):
                result += bfs(land, visited, m, n)
        answer[n] = result
    return max(answer)

def bfs(land, visited, y, x):
    if(visited[y][x] == 1 or land[y][x] == 0): return 0
    visited[y][x] = 1
    q = deque([[y, x]])
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    count = 0
    while(q):
        b, a = q.popleft()
        count += 1
        for i in range(4):
            dy = direct[i][0] + b
            dx = direct[i][1] + a
            if(dy < 0 or dy >= len(land) or dx < 0 or dx >= len(land[0])):
                continue    
            if(land[dy][dx] == 1 and visited[dy][dx] == 0):
                visited[dy][dx] = 1
                q.append([dy, dx])
    return count