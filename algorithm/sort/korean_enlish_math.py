# 이코테 359p 국영수
n = int(input())
List = [list(map(str, input().split())) for _ in range(n)]
# 1번 내림차순, 2번 오름차순, 3번 내림차순, x는 그냥
List.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 이름만 각 다른 줄에 출력
for i in range(n):
    print(List[i][0])
