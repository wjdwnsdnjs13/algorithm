from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
command = []
q = deque()
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == "push_back":
        q.append(command[1])
    elif command[0] == "push_front":
        q.appendleft(command[1])
    elif command[0] == "pop_front":
        print(q.popleft()) if len(q) else print(-1)
    elif command[0] == "pop_back":
        print(q.pop()) if len(q) else print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(0) if len(q) else print(1)
    elif command[0] == "front":
        print(q[0]) if len(q) else print(-1)
    elif command[0] == "back":
        print(q[-1]) if len(q) else print(-1)