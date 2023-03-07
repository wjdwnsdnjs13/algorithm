import sys
print = sys.stdout.write

m, n = map(int, input().split())
for i in range(m, n + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i%j == 0: break
    else: print(str(i) + "\n")
# 이 방식 조금 더 공부해보기