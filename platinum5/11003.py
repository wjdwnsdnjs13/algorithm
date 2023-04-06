import sys
input = sys.stdin.readline
print = sys.stdout.write
n, l = map(int, input().split())
A = list(map(int, input().split()))
answer = ""
for i in range(n):
    answer += str(min(A[i-l+1:i+1]) if i-l+1 > 0 else min(A[:i + 1])) + " "
print(answer)