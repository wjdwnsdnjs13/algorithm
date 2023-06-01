answer = []
def solution(k, dungeons):
    global answer
    count = 0
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            dfs(k - dungeons[i][1], dungeons[:i] + dungeons[i+1:], count + 1)
    return max(answer)

def dfs(k, dungeons, count):
    global answer
    if not dungeons or k < min(dungeons)[0]:
        return count
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            answer.append(dfs(k - dungeons[i][1], dungeons[:i] + dungeons[i+1:], count + 1))
    return count
            