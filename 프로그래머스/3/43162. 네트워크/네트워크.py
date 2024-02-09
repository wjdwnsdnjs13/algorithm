def solution(n, computers):
    # 컴퓨터가 서로서로 연결되어 있음. -> 같은 네트워크
    # n : 컴퓨터의 개수
    # computers : 연결 정보
    # return : 네트워크 개수
    
    answer = 0
    visited = [0 for _ in range(n)]

    for i in range(len(computers)):
        if(visited[i]): continue
        answer += dfs(computers, visited, i)
    return answer

def dfs(graph, visited, m):
    network = [m]
    while(network):
        com = network.pop()
        # if(not visited[com]): 
        for g in range(len(graph[com])):
            if(not visited[g] and graph[com][g]):
                network.append(g)
                visited[g] = 1
    return 1