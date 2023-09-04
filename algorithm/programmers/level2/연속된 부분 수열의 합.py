def solution(sequence, k):
    answer = [0, len(sequence)]
    hap = sequence[0]
    start = 0
    end = 0
    while(len(sequence) - 1 >= end):
        if(hap == k):
            if(end - start < answer[1] - answer[0]):
                answer = [start, end]
            end += 1
            if(end > len(sequence) - 1): break
            hap += sequence[end]
        elif(hap > k):
            hap -= sequence[start]
            start += 1
        else:
            end += 1
            if(end > len(sequence) - 1): break
            hap += sequence[end]
    return answer