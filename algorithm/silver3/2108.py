import sys
import math
from collections import Counter
# 주의 사항 1 : 리스트가 하나인 경우 조심해야됨.
# 주의 사항 2 : 최빈값 구하기
# 주의 사항 3 : round 함수는 .5일때 홀수는 올림, 짝수는 내림
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]

most = Counter(numbers).most_common(2)
if counter

numbers.sort()
one = round(sum(numbers)/n) + 1 if (math.isclose((sum(numbers)/n)%1, 0.5) and (sum(numbers)/n)%2 == 0) else round(sum(numbers)/n)
print(one)
print(numbers[n//2])
print(three)
print(max(numbers) - min(numbers))