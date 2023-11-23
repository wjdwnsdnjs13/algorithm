def solution(x):
#     x 자리 수들의 합으로 x가 나누어져야함.
    return True if(x % sum(int(i) for i in str(x)) == 0) else False