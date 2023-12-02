# k번 째 생일을 맞은 나리.
# 곰돌이가 초 두개 구매할거임.
# n개의 초를 팔고 있음.
# 초 두개의 길이의 합은 나리의 나이 k와 같아야함.
# *초 조합은 무조건 한 가지임.

k, n = map(int, input().split())
box = list(map(int, input().split()))
box.sort()

# 투포인터로 하면 바로 해결될 듯.
start = 0
end = n - 1
while(True):
    target = box[start] + box[end]
    if(target == k): break
    elif(target > k):
        end -= 1
    else:
        start += 1
print(box[start], box[end])