import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = []
people = {}
for _ in range(n + m):
    name = input()
    if (name not in people): people[name] = 1 
    else: answer.append(name)
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i], end="")