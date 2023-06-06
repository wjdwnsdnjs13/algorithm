from collections import deque

def solution(number, k):
    answer = ''
    que = deque(number)
    while(k and k < len(que)):
        print("que : ", que, "k : ", k, end=" ")
#         k=1 이면서 len(que) > 1면서, que[0] > que[1] 이면 삭제, 아니면 패스
        if k == 1 and que[0] > que[1]:
            k -= 1
            answer += que.popleft()
            break
        tmp = []
        for i in range(k):
            tmp.append(que[i])
        delete = que.index(max(tmp))
        if delete == 0:
            answer += que.popleft()
        else:
            for i in range(delete):
                que.popleft()
                k -= 1
        print(" answer : ", answer, "k : ", k)
    if k == 0:
        answer += "".join(que)
        
    return answer