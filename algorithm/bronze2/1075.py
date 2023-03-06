n = input()
f = int(input())

for i in range(100):
    if i < 10:
        number = int(n[:-2] + '0' + str(i))
        if number%f == 0:
            print('0' + str(i))
            break
    else:
        number = int(n[:-2] + str(i))
        if number%f == 0:
            print(str(i))
            break