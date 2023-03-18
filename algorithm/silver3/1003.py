t = int(input())
memo = {
    0 : [1, 0],
    1 : [0, 1],
    2 : [1, 1],
    3 : [1, 2]
}
def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        one = fibonacci(n-1)
        two = fibonacci(n-2)
        memo[n] = [one[0] + two[0], one[1] + two[1]]
        return memo[n]
for _ in range(t):
    n = int(input())
    result = fibonacci(n)
    print(result[0], result[1])