n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
request = int(input())
r_list = list(map(int, input().split()))

def one():
    for r in r_list:
        start = 0
        end = n - 1
        result = "no"
        while start <= end:
            target = (start + end)//2
            if n_list[target] == r:
                result = "yes"
                break
            elif n_list[target] > r:
                end = target - 1
            else:
                start = target + 1
        print(result, end=' ')

def two():
    n_set = set(n_list)

    for r in r_list:
        if r in n_set:
            print('yes', end=' ')
        else:
            print('no', end=' ')
