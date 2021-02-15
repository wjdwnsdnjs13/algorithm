# 이코테 339p and 백준 18352 특정 거리의 도시 찾기.

import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
route = [-1] * (n + 1)
route[x] = 0

queue = deque([x])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if route[i] == -1:
            route[i] = route[v] + 1
            queue.append(i)
result = False
for i in range(1, n + 1):
    if route[i] == k:
        print(i)
        result = True
if result == False:
    print(-1)
