# 이코테 220p 개미 전사
n = int(input())
food = list(map(int, input().split()))

dp = [0] * 101
dp[1] = food[0]
dp[2] = food[1]
dp[3] = food[0] + food[2]
for i in range(4, n+1):
    dp[i] = max(dp[i-2], dp[i-3]) + food[i-1]

print(dp)
