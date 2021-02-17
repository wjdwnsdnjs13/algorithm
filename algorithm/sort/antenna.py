# 이코테 360p 안테나
n = int(input())
List = list(map(int, input().split()))
List.sort()
print(List[(n-1)//2])
