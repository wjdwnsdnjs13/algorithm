import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            result[i] = max(result[i], result[j]+1)
print(max(result))


#틀린 알고리즘임.
"""import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
y = []
result = 0
for i in range(n):
  x = []
  x.append(a[i])
  for j in range(i,n):
    if max(x) < a[j]:
      x.append(a[j])
  y.append(x)
for i in range(len(y)):
  if result < len(y[i]):
    result = len(y[i])
print(result)"""