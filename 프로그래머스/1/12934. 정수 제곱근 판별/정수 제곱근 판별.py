# def solution(n):
#     if (n ** (1/2))%1 == 0:
#         return (n ** (1/2) + 1) ** 2
#     else:
#         return -1
    
import math
def solution(n):
    x = math.sqrt(n)
    # if (n ** (1/2))%1 == 0: #혹은 x == int(x) 를 사용해서 정수를 확인할 수 있습니다.
    if x == int(x):
        return math.pow(x+1, 2)
    return -1