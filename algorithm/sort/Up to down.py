# (이코테) 위에서 아래로 178p
n = int(input())

n_list = []
for i in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)
for i in n_list:
    print(i, end=' ')
