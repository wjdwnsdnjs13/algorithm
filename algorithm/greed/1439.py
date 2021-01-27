#숏코딩

s = input()
count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
print((count+1)//2)

"""s = input()
zero, one = 0, 0
if s[0] == '0':
  zero = 1
else:
  one = 1

for i in range(1,len(s)):
  if s[i] != s[i-1]:
    if s[i] == '0':
      zero += 1
    else:
      one +=1
if zero <= one:
  print(zero)
else:
  print(one)"""
