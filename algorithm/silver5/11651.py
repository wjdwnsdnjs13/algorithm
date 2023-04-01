import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
boxs = [list(map(int, input().split())) for _ in range(n)]
boxs.sort(key=lambda x: [x[1], x[0]])
for box in boxs:
    print(str(box[0]) + " " + str(box[1]) + "\n")