# 이코테 351p 백준 18428 감시 피하기
from itertools import combinations

n = int(input())
zido = []
teacher = []
blank = []
for i in range(n):
    zido.append(list(input().split()))
    for j in range(n):
        if zido[i][j] == 'T':
            teacher.append((i,j))
        elif zido[i][j] == 'X':
            blank.append((i,j))

def dfs(x, y, d):
    if d == 0:
        while y < n:
            if zido[x][y] == "S":
                return True
            if zido[x][y] == "O":
                return False
            y += 1
    elif d == 1:
        while x < n:
            if zido[x][y] == "S":
                return True
            if zido[x][y] == "O":
                return False
            x += 1
    elif d == 2:
        while y >= 0:
            if zido[x][y] == "S":
                return True
            if zido[x][y] == "O":
                return False
            y -= 1
    elif d == 3:
        while x >= 0:
            if zido[x][y] == "S":
                return True
            if zido[x][y] == "O":
                return False
            x -= 1
    return False

def process():
    for x,y in teacher:
        for i in range(4):
            if dfs(x, y, i):
                return True
    return False
    
find = False
for w in combinations(blank, 3):
    for a, b in w:
        zido[a][b] = 'O'
    if not process():
        find = True
        break
    for a, b in w:
        zido[a][b] = 'X'
if find:
    print("YES")
else:
    print("NO")