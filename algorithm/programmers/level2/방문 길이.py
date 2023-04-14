def solution(dirs):
    answer = 0
    memo = []
    s = [0, 0]
    for d in dirs:
        location = move(d, s)
        if s != location and (([s, location] not in memo)):
            answer += 1
            memo.append([s, location])
            memo.append([location, s])
        s = location
    return answer

def move(direction, s):
    if direction == "U" and s[1] != 5:
        return [s[0], s[1] + 1]
    elif direction == "D" and s[1] != -5:
        return [s[0], s[1] - 1]
    elif direction == "R" and s[0] != 5:
        return [s[0] + 1, s[1]]
    elif direction == "L" and s[0] != -5:
        return [s[0] - 1, s[1]]
    return s