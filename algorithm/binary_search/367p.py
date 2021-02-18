# 이코테 367p 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
List = list(map(int, input().split()))

# 더 작은 숫자 구하기
def LEFT(List, x, n):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if (List[mid-1] < x or mid == 0) and List[mid] == x:
            return mid
        elif List[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return

# 더 큰 숫자 구하기
def RIGHT(List, x, n):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if (List[mid+1] > x or mid == n - 1) and List[mid] == x:
            return mid
        elif List[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return
left = LEFT(List, x, n)
# 왼쪽거에 없으면 그냥 숫자가 없다는 말임.
if left == None:
    print(-1)
else:
    right = RIGHT(List, x, n)
    print(right - left + 1)
