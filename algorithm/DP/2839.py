order = int(input())
INF = int(1e9)
dp = [INF] * (order + 1)
for i in range(order+1):
    if i == 3 or i == 5:
        dp[i] = 1
    if i > 5:
        if dp[i-3] != INF or dp[i-5] != INF:
            dp[i] = min(dp[i-3], dp[i-5]) + 1
if dp[order] == INF:
    print("-1")
else:
    print(dp[order])
