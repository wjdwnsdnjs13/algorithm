from itertools import combinations

def solution(number):
    # 삼총사 : 3명 정수 번호의 합 0
    # return : 삼총사 만드는 경우의 수
    
    # 3중 for문 쓰면 바로 해결 가능
    answer = 0
    for x in range(len(number) - 2):
        for y in range(x + 1, len(number) - 1):
            for z in range(y + 1, len(number)):
                if(not (number[x] + number[y] + number[z])): answer += 1
    return answer

def solutionUseCombinations(number):
    # 삼총사 : 3명 정수 번호의 합 0
    # return : 삼총사 만드는 경우의 수
    
    # 3중 for문 쓰면 바로 해결 가능
    
    box = list(combinations(number, 3))
    answer = 0
    for b in box:
        if(not sum(b)): answer += 1
    
    return answer