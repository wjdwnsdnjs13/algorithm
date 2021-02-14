# 이코테 226p 효율적인 화폐 구성
n, m = map(int, input().split())
money = []
dp = [11111] * 10001
for i in range(n):
    money.append(int(input()))
    dp[money[i]] = 1
for i in range(m+1):
    for j in money:
        if i > j:
            dp[i] = min(dp[i], dp[i-j] + 1)
if dp[m] == 11111:
    dp[m] = -1
print(dp[m])
