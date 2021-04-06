# 이코테 376p 백준 1932 정수 삼각형
n = int(input())
pyramid = []
pyramid.append([int(input())])
for _ in range(n-1):
    pyramid.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(len(pyramid[i])):
        if j == 0:
            pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j]
        elif j == len(pyramid[i]) - 1:
            pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j-1]
        else:
            pyramid[i][j] = pyramid[i][j] + max(pyramid[i-1][j], pyramid[i-1][j-1])
print(max(pyramid[-1]))