from collections import deque

def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x: x[1])
    que1 = deque()
    que2 = deque()
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2]) * 60 + int(plans[i][1][3:5])
        plans[i][2] = int(plans[i][2])
        que1.append([plans[i][0], plans[i][1], plans[i][2]])
    while(que1):
        playTask = que1.popleft()
        if(not que1):
            answer.append(playTask[0])
            if(que2):
                for q in que2: answer.append(q[0])
            break

        playTask[2] -= (que1[0][1] - playTask[1])
        if(playTask[2] == 0): answer.append(playTask[0])
        elif(playTask[2] < 0):
            answer.append(playTask[0])
            while((playTask[2] < 0) and que2):
                que2[0][2] += playTask[2]
                playTask[2] = 0
                if(que2[0][2] <= 0):
                    answer.append(que2[0][0])
                    playTask[2] += que2[0][2]
                    que2.popleft()
        else:
            que2.appendleft(playTask)
    return answer