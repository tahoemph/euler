prime_cache = [2, 3]

# TODO: If there are multiple generators then this cache isn't safe.
def next_prime():
    for prime in prime_cache:
        yield prime
    number = prime + 2
    while True:
        for divisor in prime_cache:
            if number % divisor == 0:
                number += 2
                break
            if divisor*divisor > number:
                prime_cache.append(number)
                yield(number)
                number += 2
                break

def compute_primes(number_of_primes):
    # prime (heh) cache
    for n in next_prime():
        if len(prime_cache) > number_of_primes:
            break
    return prime_cache[:number_of_primes]

def factor(number):
    if number == 1:
        return [(1,1)]
    factors = []
    append = factors.append
    multiple = 1
    for n in next_prime():
        if number % n == 0:
            power = 1
            while number % (n**(power+1)) == 0:
                power += 1
            append((n, power))
            multiple *= n**power
            if multiple == number:
                break
    return factors
