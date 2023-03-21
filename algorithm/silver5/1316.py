n = int(input())
answer = 0
for _ in range(n):
    word = input()
    flag = False
    prev = 0
    for i in range(1, len(word)):
        if (word[i] != word[i-1] and word[i] in word[:i]):
            flag = True
    answer += 0 if (prev == 0 and flag == True) else 1
print(answer)