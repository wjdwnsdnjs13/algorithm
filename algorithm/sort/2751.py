import sys
input = sys.stdin.readline
n = int(input())
List = [int(input()) for _ in range(n)]
List.sort()
for i in List:
    print(i)
