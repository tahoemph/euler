import sys
sys.path.append('..')

import common.primes

sum_primes = 0

for prime in common.primes.next_prime():
    if prime >= 2000000:
        break
    sum_primes += prime
print sum_primes
