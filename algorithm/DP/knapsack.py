# W : 배낭의 무게 한도, wt: 각 보석의 무게, val : 각 보석의 가격, n : 보석의 수
def knapsack(W, wt, val, n):
    # dp를 위한 2차원 리스트 초기화 무게 한도가 0이고 보석이 0인 경우가 있기에 0으로 초기화함.
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1): # 각 칸을 돌면서
        if i == 0 or w==0: # 0번째 행/열은 0으로 세팅하기. 위에 리스트 초기화 참고
            K[i][w] = 0
        elif wt[i-1] <= w: # 점화식을 그대로 프로그램으로
            #max함수 이용해서 큰 것 선택
            K[i][w] = max(val[i-1] + K[i=1][w-wt[i-1]], K[i-1][w])
        else:
            K[i][w] = k[i-1][w]
    return K[n][W]