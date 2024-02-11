def solution(slice, n):
    # slice : 피자 조각 수
    # n : 피자를 먹는 사람 수
    # return : 최소 한 조각 이상 피자 먹으려면 몇 판의 피자를 시켜야 하는 지
    
    return n//slice + 1 if(n%slice != 0) else n//slice