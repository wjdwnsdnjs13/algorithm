answer = []
def solution(k, dungeons):
    global answer
    count = 0
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            nextDungeons = dungeons.copy()
            nextDungeons.remove(dungeons[i])
            dfs(k - dungeons[i][1], nextDungeons, count + 1)
    return max(answer)

def dfs(k, dungeons, count):
    global answer
    if not dungeons or k < min(dungeons)[0]:
        return count
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            nextDungeons = dungeons.copy()
            nextDungeons.remove(dungeons[i])
            answer.append(dfs(k - dungeons[i][1], nextDungeons, count + 1))
    return count
            