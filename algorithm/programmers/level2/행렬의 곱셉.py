def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum = 0
            for r in range(len(arr1[0])):
                sum += (arr1[i][r] * arr2[r][j])
            answer[i].append(sum)
        
    return answer