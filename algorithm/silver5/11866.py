n, k = map(int, input().split())
human = [i for i in range(1, n + 1)]
answer = "<"

# while(len(human)):
#     if i == len(human) - 1:
#         i = 0
#     else:
#         i += 1
#     count += 1
#     if count == k:
#         answer += str(human[i]) + ", "
#         del human[i]
#         count = 0
#         i -= 1

idx = -1
for i in range(n):
    for count in range(k):
        if idx == len(human) - 1:
            idx = 0
        else:
            idx += 1
    answer += str(human[idx]) + ", "
    del human[idx]
    idx -= 1

answer = answer[:-2]
answer += ">"
print(answer)