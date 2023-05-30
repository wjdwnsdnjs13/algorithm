from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque()
    for i in range(len(priorities)):
        que.append([priorities[i], False if i != location else True])
    while(True):
        one = max(que)[0]
        tmp = que.popleft()
        if tmp[0] < one:
            que.append(tmp)
        else:
            answer += 1
            if tmp[1] == True:
                return answer