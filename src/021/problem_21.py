import sys
sys.path.append('..')

import common.primes
import itertools

def amicable(n):
    factors_n = common.primes.factor(n)
    flattened = []
    for p, f in factors_n:
        flattened.extend([p for i in range(f)])
    divisors_n = set(x[0] for x in factors_n)
    divisors_n.add(1)
    for num_mults in range(2, len(flattened)):
        for combo in itertools.combinations(flattened, num_mults):
            divisors_n.add(reduce(lambda x, y: x*y,  (y for y in combo)))
    buddy = sum(x for x in divisors_n if x < n)
    if buddy == n:
        return None
    factors_buddy = common.primes.factor(buddy)
    flattened = []
    for p, f in factors_buddy:
        flattened.extend([p for i in range(f)])
    divisors_buddy = set(x[0] for x in factors_buddy)
    divisors_buddy.add(1)
    for num_mults in range(2, len(flattened)):
        for combo in itertools.combinations(flattened, num_mults):
            divisors_buddy.add(reduce(lambda x, y: x*y,  (y for y in combo)))
    buddy_sum = sum(x for x in divisors_buddy if x < buddy)
    if buddy_sum == n:
        return buddy
    else:
        return None

amicable_pairs = {}
for number in range(3, 10001):
    if number in amicable_pairs:
        continue
    buddy = amicable(number)
    if buddy:
        amicable_pairs[number] = buddy
        amicable_pairs[buddy] = number

print sum(amicable_pairs)
