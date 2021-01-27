n = int(input("입력>"))
adv = list(map(int, input("입력>").split()))
group = []
length = []
adv.sort()

for i in range(n):
    group.append([adv[len(length)]])
    length.append(adv[len(length)])
    print(group)
    print(length)
    while max(group[i]) > len(group[i]):
        group[i].append(adv[len(length)])
        length.append(adv[len(length)])
        print(group, "while")
        print(length, "while")
        if len(length) == len(adv):
            break
    if max(group[i]) != len(group[i]):
        group.pop()

    if len(length) == len(adv):
        break
print(group)
print(len(group))