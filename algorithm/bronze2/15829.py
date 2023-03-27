n = int(input())
answer = 0
alphabet = input()
for i in range(n):
    answer += (ord(alphabet[i]) - 96) * (31 ** i)
print(answer%1234567891)