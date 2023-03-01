from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    elif command[0] == "back":
        try:
            print(queue[-1])
        except:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "pop":
        try:
            print(queue.popleft())
        except:
            print(-1)