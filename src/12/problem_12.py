import sys
sys.path.append('..')
import common.primes

import collections
import itertools

# Using that the number of divisors of a number greater then 1 is the
# product of the powers of the factors plus 1 makes this fairly simple.
# This is known as the divisor function.  We avoid 1 by starting the
# sequence at the second triangle number.
next_number = 3
triangle = 3
while True:
    factors = common.primes.factor(triangle)
    num_divisors = reduce(lambda x, y: x*y, ((x[1]+1) for x in factors))
    if num_divisors > 500:
        break
    triangle += next_number
    next_number += 1
print triangle
