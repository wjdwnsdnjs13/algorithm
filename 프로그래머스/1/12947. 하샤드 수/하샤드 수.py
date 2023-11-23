def solution(x):
#     x 자리 수들의 합으로 x가 나누어져야함.
    y = 0
    for i in str(x):
        y += int(i)
    if(x%y == 0): return True
    return False