import heapq

def solution(scoville, K):
    # 음식 2가지를 섞으면 x = 젤 안 매운 거 + (두번째로 안 매운거 * 2)
    # 모든 음식이 K 이상이 될때까지 반복함.
    # return : 섞어야하는 최소 횟수
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    while(heap[0] < K):
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        if(len(heap) < 2 and heap[0] < K):
            return -1
    return answer

def solution2(scoville, K):
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