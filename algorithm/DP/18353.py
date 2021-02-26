# 이코테 380p 18353 병사 배치하기
n = int(input())
List = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if List[j] > List[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
