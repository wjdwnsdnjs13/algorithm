def solution(num):
    answer = 0
#     짝수면 2로 나누고
# 홀 수면 3을 곱하고 1을 더함
# 1이될때까지 반복
# 500번 반복해도 1이 안되면 -1 반환
    while(answer <= 500):
        if(num == 1): return answer
        answer += 1
        num = num//2 if(num % 2 == 0) else (num * 3 + 1)
    return -1