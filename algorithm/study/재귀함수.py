memo = {
    0 : 0,
    1 : 1,
    2 : 1
}

def one(n):
    if n in memo: return memo[n]
    memo[n] = one(n-1) + one(n-2)
    return memo[n]

def two(n):
    if n == 1 or n == 2: return 1
    if n == 0: return 0
    return two(n-1) + two(n - 2)
print(one(100))
print(two(100))
