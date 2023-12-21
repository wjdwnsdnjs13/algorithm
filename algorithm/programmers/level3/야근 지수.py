def solution(n, works):
#     야근 피로도 = 야근 시작 시점 + (남은 작업량)^2
#     1시간동안 1만큼 처리
#     n = 퇴근까지 남은 시간
    
    # works의 총합 - n
    # 이 값이 0이하면 바로 리턴
    
    # (야근)/len(works) 에서
    # 1. 나머지에 해당하는 만큼의 평균 + 1 이 존재
    # 2. 1번의 갯수를 뺀만큼 평균이 존재
    # 이거는 기존 숫자에 + 하는 경우가 나오기 때문에 안됨.
    # 새로 추가한 4번 케이스 참고
    
    # 최댓값을 직접 1씩 제거하는 방법
    # 1. 최대힙 사용
    # 2. 최초 1회 정렬 후 while 안에서 정렬을 계속하는 거보다
    # for문으로 한 칸씩 앞으로 가면서 [-1] 이하의 값이 나올 때까지
    # -1 해주면 됨.
    
    minWorksTime = sum(works) - n
    if(minWorksTime <= 0): return 0
    count = len(works)
    avgWorksTime = minWorksTime//count
    upToAvgCount = minWorksTime%count
    answer = 0
    answer += (avgWorksTime + 1) ** 2 * upToAvgCount
    count -= upToAvgCount
    answer += (avgWorksTime) ** 2 * count
    return answer