import sys
sys.path.append('..')

import common.primes
import math

number = 600851475143

factors = common.primes.factor(number)
print factors[-1][0]
