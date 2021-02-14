# 이코테 223p 바닥 공사
n = int(input())
dp = [0] * 1001
dp[1], dp[2], dp[3] = 1, 3, 5
for i in range(3, n+1):
    dp[i] = (dp[i-1] + (2 * dp[i-2])) % 796796
print(dp[n])
