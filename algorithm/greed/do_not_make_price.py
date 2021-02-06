n = input()
coin = list(map(int, input().split()))
target = 1
coin.sort()

for c in coin:
    if c <= target:
        target += c
    else:
        break

print(target)
