n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)

while(start <= end):
    mid = (start + end)//2
    take = 0
    for i in tree:
        take +=  (i - mid) if i > mid else 0
    if take >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)