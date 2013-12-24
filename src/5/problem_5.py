import sys
sys.path.append('..')

import collections
import common.primes

powers = collections.Counter()

for i in range(2,21):
    factors = common.primes.factor(i)
    for factor in factors:
        powers[factor[0]] = max(powers[factor[0]], factor[1])

print reduce(lambda x, y: x*y, (number**powers[number] for number in powers))
