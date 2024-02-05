import heapq

def solution(ability, number):
    # 신입 중 2명 선발해서 같이 공부하게 하는 것.
    # 둘이 공부하면 둘의 능력치는 서로의 합이 됨.
    # 중복 선발 가능.
    # 교육 이후 모든 사원들의 능력치의 합을 최소화 하고 싶음.
    # ability : 신입 사원의 능력치, 길이는 100만, 능력치는 100이하
    # number : 교육 횟수, 1만 이하
    # 리턴 값은 10억 이하임.
    
    # 매번 작은 애들끼리 교육시키면 될 듯
    # 2중 for문은 시간 초과남. -> 우선순위 큐 사용.
    answer = 0
    heapq.heapify(ability)
    for n in range(number):
        one = heapq.heappop(ability)
        two = heapq.heappop(ability)
        tmp = one + two
        heapq.heappush(ability, tmp)
        heapq.heappush(ability, tmp)
    return sum(ability)