def solution(land):
    answer = 0
    dp = [[0, 0, 0, 0] for _ in range(len(land))]
    dp[0] = land[0][:]

    for j in range(1, len(land)):
        for k in range(4):
            tmp = []
            for l in range(4):
                if l != k:
                    tmp.append(dp[j - 1][l])
            dp[j][k] = land[j][k] + max(tmp)
    answer = max(answer, max(dp[-1]))

    return answer