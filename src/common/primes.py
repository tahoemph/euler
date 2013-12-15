prime_cache = [2]

def compute_primes(number_of_primes):
    number = prime_cache[-1] + 1
    while len(prime_cache) < number_of_primes:
        for divisor in prime_cache:
            if divisor*divisor > number:
                prime_cache.append(number)
                break
            if number % divisor == 0:
                break
        else:
            prime_cache.append(number)
        number += 1
    return prime_cache[:number_of_primes]


