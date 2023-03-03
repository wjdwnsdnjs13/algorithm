import sys

input = sys.stdin.readline
n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]
number.sort(key=lambda x: (x[0], x[1]))
for a in number:
    print(a[0], a[1])