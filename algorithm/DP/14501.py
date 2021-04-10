# 이코테 377p 백준 14501 퇴사
# 계산 시 과정 계산
n = int(input())
dp = [0] * (n+1)
schedule = []
for i in range(n):
    schedule.append(list(map(int, input().split())))
print(schedule)
Max = 0
for i in range(n):
    if i+schedule[i][0] <= n:
        dp[i+schedule[i][0]] = max(dp[i] + schedule[i][1], Max)
        Max = dp[i+schedule[i][0]]
        for j in range(i+schedule[i][0], n+1):
            dp[j] = Max
print(dp)
