# 이코테 345p 백준 18405 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
t, target_x, target_y = map(int, input().split())
virus = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if Map[i][j] != 0:
            # 바이러스 종류, 시간, 좌표
            virus.append((Map[i][j], 0, i, j))
virus.sort()
q = deque(virus)
while q:
    v, s, x, y = q.popleft()
    if s == t:
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx and nx < n and 0 <= ny and ny < n and Map[nx][ny] == 0:
            Map[nx][ny] = v
            q.append((v, s+1, nx, ny))

print(Map[target_x - 1][target_y - 1])
