from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 정해진 순서로 건넘.
    # 최소 걸리는 시간 계산.
    # bridge_length : 다리 거리, 다리에 올라가는 최대 트럭(1초에 1만큼 움직임)
    # weight : 최대 무게(트럭이 완전 다리에 올랐을 때 기준)
    # truck_weights : 트럭 무게
    
    answer = 1
    truck_weights = deque(truck_weights)
    bridge = deque() # deque([무게, 위치])
    bridge.append([truck_weights.popleft(), 1])
    
    
    # 최대 무게가 된 순간 맨 앞 트럭이 벗어날 때까지의 시간을 모든 트력 위치에 +시키고, 새로운 트럭 넣기
    while(truck_weights):
        w = 0
        for a, b in bridge:
            w += a
        next_w = w + truck_weights[0]
        if(next_w > weight or len(bridge) >= bridge_length):
            t = bridge_length - bridge.popleft()[1]
            answer += t
            for i in range(len(bridge)):
                bridge[i][1] += t
        else:
            for i in range(len(bridge)):
                bridge[i][1] += 1
            while(bridge and bridge[0][1] >= bridge_length):
                bridge.popleft()
            bridge.append([truck_weights.popleft(), 1])
            answer += 1
            
    # 다리 위에 남은 트럭들 이동시키기
    while(bridge):
        t = bridge_length - bridge.popleft()[1]
        answer += t
        for i in range(len(bridge)):
            bridge[i][1] += t
        
    return answer + 1