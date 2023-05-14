import heapq

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    heap = []
    for i in range(len(prices)):
        heapq.heappush(heap, [-prices[i], i])
        while(len(heap) > 0 and heap[0][0] < -prices[i]):
            target = heapq.heappop(heap)
            answer[target[1]] = i - target[1]
        
    while(len(heap)):
        target = heapq.heappop(heap)
        answer[target[1]] = len(prices) - target[1] - 1
    return answer