def factorial(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = n * factorial(n-1)
    return dic[n]

n, k = map(int, input().split())
dic = {
    0 : 1,
    1 : 1
}
print(int(factorial(n)/factorial(k)/factorial(n-k)))