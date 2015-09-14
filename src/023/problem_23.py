abundant = []
target_numbers = []

def is_abundant(n):
    return sum(d for d in xrange(2, n/2 + 1) if n % d == 0) > n

abundant = [n for n in xrange(12, 28123) if is_abundant(n)]
abundant_set = set(abundant)

for n in xrange(1, 28123):
    for number1 in abundant:
        if number1 >= n:
            target_numbers.append(n)
            break
        if n - number1 in abundant_set:
            break
    else:
        target_numbers.append(n)

print sum(target_numbers)
