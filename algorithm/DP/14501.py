# 이코테 377p 백준 14501 퇴사
# 틀렸다고 나옴.
n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
dp = [0] * (n+1)

for i in range(n):
    if i + t[i] <= n:
        dp[i+t[i]] = max(dp[i+t[i]], p[i] + dp[i])
print(max(dp))
