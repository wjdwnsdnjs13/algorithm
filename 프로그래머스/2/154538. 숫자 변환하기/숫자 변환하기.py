def solution(x, y, n):
    answer = [9999 for _ in range(y + 1)]
    if(y < x): return -1
    answer[x] = 0
    if(x + n <= y): answer[x + n] = 1
    if(x * 2 <= y): answer[x * 2] = 1
    if(x * 3 <= y): answer[x * 3] = 1
    
    for i in range(x, y + 1):
        if(i > x + n):
            answer[i] = min(answer[i], answer[i - n] + 1)
        if(i%2 == 0):
            answer[i] = min(answer[i], answer[i//2] + 1)
        if(i%3 == 0):
            answer[i] = min(answer[i], answer[i//3] + 1)
    if(answer[y] != 9999): return answer[y]
    else: return -1