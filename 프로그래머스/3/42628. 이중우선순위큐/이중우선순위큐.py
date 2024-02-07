import heapq

def solution(operations):
    # I 숫자 : 숫자를 큐에 삽입
    # D 1 : 최댓값 삭제
    # D -1 : 최솟값 삭제
    # 빈 큐에서 삭제 연산 -> 무시
    # return : 큐가 비어있으면 [0, 0] 값이 있으면 [최대값, 최소값]

    answer = []
    for o in operations:
        c, n = o.split(" ")
        n = int(n)
        if(c == "I"):
            heapq.heappush(answer, n)
        else:
            if(not answer): continue
            if(n == 1):
                answer.pop()
            else:
                heapq.heappop(answer)
    return [max(answer), min(answer)] if(answer) else [0,0]