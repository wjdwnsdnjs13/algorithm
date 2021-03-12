import sys
input = sys.stdin.readline
n, m = map(int, input().split())
jack = list(map(int, input().split()))
result = []
for i in range(n):
    if i >= n - 2:
        break
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            a = jack[i] + jack[j] + jack[l]
            if a <= m:
                result.append(a)
print(max(result))
