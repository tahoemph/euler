import sys
sys.path.append('..')

import common.primes

if __name__ == "__main__":
    primes = common.primes.compute_primes(10001);
    print primes[-1]
