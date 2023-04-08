n, m = map(int, input().split())

number = [list(input()) for _ in range(n)]
answer = 1
for i in range(n):
    for j in range(m):
        for z in range(1, min(n - i, m - j)):
            if number[i][j] == number[i + z][j] and number[i][j] == number[i][j + z] and number[i][j] == number[i + z][j + z]:
                answer = max(z + 1, answer)

print(answer**2)