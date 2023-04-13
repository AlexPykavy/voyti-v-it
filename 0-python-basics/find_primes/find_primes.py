from typing import List


def find_primes(n: int) -> List[int]:
    primes = []

    for i in range(2, n+1):
        for y in primes:
            if i % y == 0:
                break
        else:
            primes.append(i)

    return (primes)
