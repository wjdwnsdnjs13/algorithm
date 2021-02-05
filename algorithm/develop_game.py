n, m = map(int, input().split())
x, y, direction = map(int, input().split())
mapp = []
go = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북서남동
down = 0


for i in range(n):
    mapp.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
mapp[x][y] = 1

while True:
    turn_left()
    nx = go[direction][0] + x
    ny = go[direction][1] + y
    if mapp[nx][ny] == 0:
        x = nx
        y = ny
        mapp[x][y] = 1
        count += 1
        down = 0
        print(mapp)
        continue
    else:
        down += 1
        if down == 4:
            break
print(count)
