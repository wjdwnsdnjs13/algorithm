def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    while(len(A)):
        a = A[0]
        del A[0]
        b = B.pop()
        
        answer += (a * b)
    return answer