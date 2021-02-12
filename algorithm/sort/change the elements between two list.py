n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

for i in range(k):
    p = 0
    while True:
        if min(a) == a[p]:
            if a[p] < b[p]:
                a[p], b[p] = b[p], a[p]
                break
            else:
                break
        p += 1
print(sum(a))
