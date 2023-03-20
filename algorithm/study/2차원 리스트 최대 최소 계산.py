data = [
    [0, 3, 2],
    [0, 1, 2],
    [2, 1, 0],
    [3, 2, 1]
]
data.sort()
print(data)

data = list(map(max, data))
print(data)

data = [
    [0, 3, 2],
    [0, 1, 2],
    [2, 1, 0],
    [3, 2, 1]
]
data = max(map(max, data))
print(data)