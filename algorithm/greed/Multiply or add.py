num = list(input("입력>"))
cal = 0
if num[0] == '0' or num[1] == '0':
    cal = int(num[0]) + int(num[1])
else:
    cal = int(num[0]) * int(num[1])
for i in range(2, len(num)):
    if num[i] == '0':
        cal += int(num[i])
    else:
        cal *= int(num[i])

print(cal)