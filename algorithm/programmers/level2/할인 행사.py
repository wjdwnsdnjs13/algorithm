def solution(want, number, discount):
    answer = 0
    check = []
    for w, n in zip(want, number):
        check += [w] * n
    check.sort()
    for i in range(len(discount) - 9):
        tenDayDiscount = sorted(discount[i:i + 10])
        if check == tenDayDiscount:
            answer += 1
    return answer