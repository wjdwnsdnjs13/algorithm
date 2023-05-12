import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    while(heap[0] < K):
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        heapq.heappush(heap, one + 2*two)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer