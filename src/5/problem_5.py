import sys
sys.path.append('..')

import collections
import common.primes

powers = collections.Counter()

for i in range(2,21):
    factors = common.primes.factor(i)
    number = i
    for factor in factors[::-1]:
        power = 1
        while True:
            remainder = number - factor**power
            if remainder > 0:
                power += 1
            elif remainder == 0:
                break
            else:
                power -= 1
                break
        number -= factor**power
        powers[factor] = max(powers[factor], power)

print reduce(lambda x, y: x*y, (number**powers[number] for number in powers))
