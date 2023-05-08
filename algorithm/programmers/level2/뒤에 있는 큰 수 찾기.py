# def solution(numbers):
numbers = [2, 3, 3, 5]
answer = [-1 for _ in range(len(numbers))]
tmp = [(numbers[0], 0)]
for i in range(1, len(numbers)):
    tmp.append((numbers[i], i))
    tmp.sort(reverse = True)
    while(tmp[-1][0] <= numbers[i]):
        if numbers[i] > tmp[-1][0]:
            answer[tmp[-1][1]] = numbers[i]
            tmp.pop()
        else:
            break
print(answer)
    # return answer