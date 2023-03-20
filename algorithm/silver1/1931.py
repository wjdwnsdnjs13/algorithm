import sys
input = sys.stdin.readline
n = int(input())
meeting = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
count = 0
time = 0
for x, y in meeting:
    if x >= time:
        count += 1
        time = y
print(count)