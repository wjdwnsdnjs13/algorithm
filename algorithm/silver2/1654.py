#ZeroDivisionError 주의하기
import sys

def calc(x):
    quantity = 0
    for i in range(len(lan)):
        quantity += lan[i]//x
    return quantity

input = sys.stdin.readline
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start = 1 #0으로 설정하면 mid가 0이될 수 있어서 런타임 에러 (ZeroDivisionError) 뜸.
end = max(lan)
while(start <= end):
    mid = (start + end)//2
    quantity = calc(mid)
    if quantity >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)