flag = True

for i in range(2):
    if flag:
        print("true")
    for j in range(3):
        if i == 10:
            break
        print(i, ", ", j)
    else:
        print("false")