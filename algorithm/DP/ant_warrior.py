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


# 재귀를 이용한 풀이
n = int(input())
food = list(map(int, input().split()))
memo = {
    0 : food[0],
    1 : food[1],
    2 : max(food[0]+food[2], food[1])
}

def thief(x):
    if x == 1:
        return memo[0]
    elif x == 2:
        return memo[1]
    if x in memo:
        return memo[x-1]
    output =  max(thief(x-1), food[x-1] + thief(x-2))
    memo[x-1] = output
    return output

print(thief(n))
print(memo)