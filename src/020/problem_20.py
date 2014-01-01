def factorial(n):
    rv = 1
    for i in range(2, n+1):
        rv *= i
    return rv

print sum(int(x) for x in str(factorial(100)))
