# (이코테) 217p 1로 만들기
x = int(input())

dp = [0] * 30001
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])
    if i % 5 == 0:
        dp[i] = min(dp[i//5] + 1, dp[i])
print(dp[x])

# 백준 1463 1로 만들기
# 재귀로 풀면 예외 처리 할 게 너무 많아서 힘듬. 그냥 바텀 업방식으로 푸는 게 나을 듯.
n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])
