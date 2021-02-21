# 이코테 376p 1932번 정수 삼각형
n = int(input())
List = []
for _ in range(n):
    List.append(list(map(int, input().split())))
dp = List
for i in range(1, n):
    for j in range(len(List[i])):
        if j == 0:
            left = 0
        else:
            left = List[i-1][j-1]
        if j == len(List[i]) - 1:
            right = 0
        else:
            right = List[i-1][j]
        dp[i][j] += max(left, right)
print(max(dp[-1]))
