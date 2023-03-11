import sys

input = sys.stdin.readline
n = int(input())
flag = False
stack = []
answer = []

p = 1
for i in range(n):
    order = int(input())
    while(p <= order):
        stack.append(p)
        answer.append('+')
        p += 1

    if stack[-1] == order:
        stack.pop()
        answer.append('-')
    else:
        flag = True
        break
if flag:
    print("NO")
else:
    for a in answer:
        print(a)