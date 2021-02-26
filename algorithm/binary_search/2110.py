# 이코테 369p 2110 공유기 설치
import sys
input = sys.stdin.readline
n,c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
result = 0
start = 1
end = house[-1] - house[0]
while start <= end:
    mid = (start + end)//2
    val = house[0]
    count = 1
    for i in range(n):
        if house[i] >= val + mid:
            count += 1
            val = house[i]
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)