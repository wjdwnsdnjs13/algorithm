def solution(elements):
    answer = set()
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            element = elements[j:(j + i)]
            if (j + i) > len(elements):
                element += elements[:j + i - len(elements)]
            answer.add(sum(element))
    return len(answer)