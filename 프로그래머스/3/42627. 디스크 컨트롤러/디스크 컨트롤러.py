import heapq

def solution(jobs):
    # 한 번에 하나만 수행.
    # 가장 빠른 속도로 처리해서 요청부터 걸린 시간의 평균을 가장 작게
    # jobs : [요청 시간, 소요 시간]
    # return : 가장 짧은 평균 처리 시간
    
    # job은 우선순위 큐인데, 작업 소요 시간 기준으로함
    job = []
    n = len(jobs)
    jobs.sort(reverse=True)
    time = jobs[-1][0]
    answer = 0
    while(jobs or job):
        if(not job):
            process = jobs.pop()
        else:
            process = heapq.heappop(job)[::-1]
        time += process[1]
        answer += time - process[0]
        while(jobs and time > jobs[-1][0]):
            heapq.heappush(job, jobs.pop()[::-1])
    return answer//n