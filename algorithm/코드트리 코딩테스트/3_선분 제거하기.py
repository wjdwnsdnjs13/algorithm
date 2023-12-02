# 수직선상에 n개의 선분이 주어짐.
# 서로 안 겹치게 하기 위해 제거해야할 최소 선분의 수
# 끝 점 공유는 선분이 겹친거임.
# 회의실 문제랑 같음.
# n - (가장 많은 회의를 진행하는 경우의 수)
n = int(input())
box = []
for _ in range(n):
    a, b = map(int, input().split())
    box.append([a, b])
# 시작시간보다
# 빨리 끝나는 회의 먼저 진행해야 좋음.
box.sort(key=lambda x: (x[1], x[0]))

time = 0
count = 0
for b in box:
    if(b[0] > time):
        count += 1
        time = b[1]
print(n - count)