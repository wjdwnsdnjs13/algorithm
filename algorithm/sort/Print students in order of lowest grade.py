# (이코테) 180p 성적이 낮은 순서로 학생 출력하기
n = int(input())

dic = []
for i in range(n):
    data = input().split()
    print(data)
    dic.append((data[0], int(data[1])))

dic = sorted(dic, key=lambda student: student[1])

for student in dic:
    print(student[0], end=' ')
