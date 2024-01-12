def solution(s):
    # x : 첫 글자
    # x와 x가 아닌 글자를 카운트해서 카운트 같아지면 멈추고 문자열 분리
    # 분리 후 남은 문자열에서 계속 반복함
    # 문자열 끝일 경우 분리하고 종료
    # return : 분해한 문자열의 개수
    x = s[0]
    count = [0, 0]
    answer = 0
    for i in s:
        if(count == [0, 0]): x = i
        if(i == x): count[0] += 1
        else: count[1] += 1
        if(count[0] == count[1]):
            count = [0, 0]
            answer += 1
    
    return answer + (0 if(count == [0, 0]) else 1)