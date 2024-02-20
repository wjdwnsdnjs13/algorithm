def solution(n, k):
    # n을 k 진수로 바꿈.
    # 변환된 수 안에 아래 좋건이 맞는 소수가 몇 개인지 알고 싶음.
    # 0P0 : 소수 양 쪽에 0이 있는 경우
    # P0 : 소수 오른쪽에만 0이 있고 왼쪽에 아무 것도 없음
    # 0P : 소수 왼쪽에만 0이 있고 오른쪽에 아무것도 없는 경우
    # P : 소수 양 쪽에 아무 것도 없는 경우
    # P는 각 자릿수에 0을 포함하지 않는 소수임.
    # n <= 100만
    # 3 <= k <= 10
    answer = 0
    
    # 진수 변환
    change_n = ''
    n_c = n
    while(n_c >= k):
        change_n += str(n_c%k)
        n_c //= k
    if(change_n): change_n += str(n_c%k)
    change_n = change_n[::-1]
    
    # 숫자 쪼개기(0기준으로 split하면 됨.)
    change_n = change_n.split("0")
    
    # 소수 찾기
    for c in change_n:
        try:
            c = int(c)
            if(c < 2): continue
            for i in range(2, int(c ** 0.5) + 1):
                if(not c%i): 
                    print("i : ", i)
                    break
            else:
                answer += 1
        except:
            continue
    return answer