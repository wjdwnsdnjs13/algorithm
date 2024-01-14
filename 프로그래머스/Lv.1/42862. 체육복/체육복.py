def solution(n, lost, reserve):
#     n : 전체 학생 수
#     lost : 도난 당한 학생들의 번호
#     reserve : 여벌의 체육복을 가져온 학생들 번호
    
#     100101010110
#     양 쪽 다 여분이 있지만, 내가 가져가면 다른 친구들이 못 가져갈 경우가 생길 수 있음.

    answer = 0
    student = [1 for i in range(n)]
    for l in lost: student[l - 1] -= 1
    for r in reserve: student[r - 1] += 1
    for i in range(n):
        if(student[i] == 0):
            if((i != 0) and (student[i - 1] > 1)):
                student[i] += 1
                student[i - 1] -= 1
            elif((i != (n - 1)) and (student[i + 1] > 1)):
                student[i] += 1
                student[i + 1] -= 1
    for s in student:
        if(s): answer += 1
        
        
    return answer