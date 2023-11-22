def solution(arr):
#     2^n * 2^n 크기의 배열 arr
# 쿼드 트리와 같은 방식으로 압축
# 1. 압축하려는 영역을 S
# 2. S 내부의 모든 수가 같으면 하나로 압축
# 3. 다른 수가 있으면 4개의 정 사각형 영역으로 쪼개 1번부터 반복
# arr을 압축했을 때 최종적으로 남은 [0의 개수, 1의 개수] return
    answer = cube(arr)
# sum(범위) = 0 -> 0
# sum(범위) = 범위넓이 -> 1
# 재귀 함수로 ㄱㄱ
    return answer

def cube(arr):
    area = len(arr) * len(arr)
    hap = 0
    for a in arr: hap += sum(a)
    if(area == hap): return [0, 1]
    if(hap == 0): return [1, 0]
    if(len(arr) == 2):
        return [area - hap, hap]
    cubeData = [[],[],[],[]]
    for i in range(4):
        arrCopy = []
        for j in range(len(arr)//2):
            if(i == 0): arrCopy.append(arr[j][:len(arr)//2])
            elif(i == 1): arrCopy.append(arr[j][len(arr)//2:])
            elif(i == 2): arrCopy.append(arr[len(arr)//2 + j][:len(arr)//2])
            else: arrCopy.append(arr[len(arr)//2 + j][len(arr)//2:])
        cubeData[i] = cube(arrCopy)
    x = cubeData[0][0] + cubeData[1][0] + cubeData[2][0] + cubeData[3][0]
    y = cubeData[0][1] + cubeData[1][1] + cubeData[2][1] + cubeData[3][1]
    return [x, y]
