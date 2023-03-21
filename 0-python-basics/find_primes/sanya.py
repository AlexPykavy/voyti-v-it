from typing import List


def find_primes_oneline(n: int) -> List[int]:
    # 1. ternary operator
    # 2. all() vs any()
    # 3. list comprehension

    return [i for i in range(2, n + 1) if not any(i % div == 0 for div in range(2, i))]
