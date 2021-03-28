# 이코테 367p 정렬된 배열에서 특정 수의 개수 구하기

n, target = map(int, input().split())
box = list(map(int, input().split()))

start = 0
end = n - 1
left, right = 0, 0
while start <= end:
    mid = (start + end)//2
    if mid == 0 or (box[mid] == target and box[mid] - 1 < target):
        left = mid
    elif box[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

start = 0
end = n - 1
while start <= end:
    mid = (start + end)//2
    if mid == (n - 1) or (box[mid] == target and box[mid] + 1 > target):
        right = mid
    elif box[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
print(left, right)