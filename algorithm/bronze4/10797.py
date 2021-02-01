#0131
import sys
a = int(sys.stdin.readline())
x = 0
b = (list(map(int, (sys.stdin.readline().split()))))
for i in b:
    if i == a:
        x += 1

print(x)
