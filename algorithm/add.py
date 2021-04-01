n, m = map(int, input().split())
zido = []
copy = []
for i in range(n):
    zido.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x,y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx and nx < n and 0 <= ny and ny < m and copy[i][j] == 0:
            copy[i][j] = 2
            virus(i,j)

def score():
    count = 0
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                count += 1
    return count

def solution(count):
    global result
    if count == 3:
        copy = [i[:] for i in zido]
        for i in range(n):
            for j in range(m):
                if copy[i][j] == 2:
                    virus(i,j)
        result = max(result, score())

    else:
        for i in range(n):
            for j in range(m):
                if zido[i][j] == 0:
                    zido[i][j] = 1
                    count += 1
                    solution(count)
                    zido[i][j] = 0
                    count -= 1
result = 0
solution(0)
print(result)
