n = list(input())
n.sort(reverse=True)

sum = 0
if not("0" in n):
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        for i in n:
            print(i, end='')
