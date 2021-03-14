# readline으로 한번에 받는 것도 찾아볼 것.
import sys
input = sys.stdin.readline
n = int(input())
List = [int(input()) for _ in range(n)]
List.sort()
for i in List:
    print(i)
