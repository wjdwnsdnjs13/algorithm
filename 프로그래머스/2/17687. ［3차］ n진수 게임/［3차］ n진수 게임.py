import string

def solution(n, t, m, p):
    # 한자리씩 떼서 순서대로 얘기함.
    # n : 진법
    # t : 구할 숫자의 수 
    # m : 게임에 참가하는 인원
    # p : 튜브의 순서
    answer = "0"
    
    # 숫자 진법 기준으로 나누기
    tmp = string.digits+string.ascii_uppercase
    for q in range(1, t * m):
        pp = ""
        while(q):
            q, r = divmod(q, n)
            pp = tmp[r] + pp
        answer += pp
        
#     011011100101110111100010011010
    
    return answer[p-1::m][:t]