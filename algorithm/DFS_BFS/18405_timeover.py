# 이코테 345p 백준 18405 경쟁적 전염
n, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int, input().split())
prev = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def copy():
    for x in range(n):
        for y in range(n):
            prev[x][y] = Map[x][y]

def spread(virus, x, y):
    if prev[x][y] == virus:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx and nx < n and 0 <= ny and ny < n and Map[nx][ny] == 0:
                Map[nx][ny] = virus

for i in range(s):
    copy()
    for v in range(1, k+ 1):
        for x in range(n):
            for y in range(n):
                spread(v, x, y)

print(Map[target_x - 1][target_y - 1])