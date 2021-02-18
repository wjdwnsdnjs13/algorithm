# 이코테 323p 문자열 압축
s = str(input())
# 맨 처음 길이를 저장.
answer = len(s)
# 쪼개는 길이를 점점 늘리며 계산
for step in range(1, len(s)//2 + 1):
    count = 1
    # prev에 첫 글자조각 저장
    prev = s[0:step]
    compressed = ''
    for i in range(step, len(s), step):
        if prev == s[i:i+step]:
            count += 1
        else:
            compressed += str(count) + prev if count > 1 else prev
            prev = s[i:i+step]
            count = 1
    # 남은 글자조각을 추가함.(step에 딱 맞아 떨어지면 통째로 남는 조각이 있음.)
    compressed += str(count) + prev if count > 1 else prev
    answer = min(answer, len(compressed))
print(answer)
