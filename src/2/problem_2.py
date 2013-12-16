def fib():
    before = 1
    yield 1
    last = 2
    yield 2
    while True:
        next = before + last
        yield next
        before = last
        last = next

total = 0
for f in fib():
    if f >= 4000000:
        break
    if f % 2 == 0:
        total += f

print total
