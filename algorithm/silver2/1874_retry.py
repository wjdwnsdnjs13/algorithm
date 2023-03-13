import sys
input = sys.stdin.readline

n = int(input())
answer = []
p = 0
flag = False
stack = []

for i in range(n):
    m = int(input())
    while(p < m):
        p += 1
        stack.append(p)
        answer.append('+')

    if stack[-1] == m:
        answer.append('-')
        stack.pop()
    else:
        flag = True
        break
if flag:
    print('NO')
else:
    for a in answer:
        print(a)