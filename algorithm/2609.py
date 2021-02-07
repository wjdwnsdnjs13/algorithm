a,b = map(int, input().split())


def least_common_factor(a, b):
    if a % b == 0:
        return b
    A = b
    B = a % b
    return least_common_factor(A, B)

def greatest_common_multiple(a, b):
    c = max(a, b)
    while True:
        if c % a == 0 and c % b == 0:
            return c
    c += 1

print(least_common_factor(a, b))
print(greatest_common_multiple(a, b))