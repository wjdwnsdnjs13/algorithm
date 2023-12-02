# 문자 a랑 b로만 이루어진 길이가 n인 문자열 s
# s를 원하는 대로 순서를 바꿔서 서로 다른 문자열중 팰린드롬이 아닌문자열 구하기
# 팰린드롬은 거꾸로 읽어도 같은 문자열임
# 팰린드롬이 아닌 문자 중 정렬해서 k번째인 거 출력
from itertools import product

n, k = map(int, input().split())
s = list(input())
cnt = 0
for i in s:
    cnt += 1 if(i =="b") else 0
result = []
answer = ""

# 0, 1으로 이루어진 모든 경우의 수
for i in product([0, 1], repeat=n):
    p = list(i[:])
    if(sum(p) == cnt and p != p[::-1]):
        result.append(p)
result.sort()

if(len(result) < k): answer = -1
else:
    for a in result[k - 1]:
        answer += "b" if(a) else "a"
print(answer)