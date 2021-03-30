# 아직 오류 발생함. combinations 사용하는 방법 익히기
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
        while y >= 0:
            if zido[x][y] == 'S':
                return True
            if zido[x][y] == 'O':
                return False
            y -= 1
    if d == 1:
        while y < n:
            if zido[x][y] == 'S':
                return True
            if zido[x][y] == 'O':
                return False
            y += 1
    if d == 2:
        while x >= 0:
            if zido[x][y] == 'S':
                return True
            if zido[x][y] == 'O':
                return False
            x -= 1
    if d == 3:
        while x < n:
            if zido[x][y] == 'S':
                return True
            if zido[x][y] == 'O':
                return False
            x += 1
    return False

def process():
    for x, y in teacher:
        for i in range(4):
            if dfs(x, y, i):
                return True
    return False

find = False
for data in combinations(blank, 3):
    for x,y in data:
        zido[x][y] = '0'
    if not process():
        find = True
        break
    for x, y in data:
        zido[x][y] = 'X'


if find:
    print('yes')
else:
    print('no')
