n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

count = 0
for c in coin:
    if c > k:
        continue
    if k//c == 0:
        count += k//c
        break
    count += k//c
    k %= c

print(count)