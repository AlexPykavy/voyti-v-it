from find_primes import find_primes


def test_find_primes_with_5():
    assert find_primes(5) == [2, 3, 5]


def test_find_primes_with_0():
    assert find_primes(0) == []


def test_find_primes_with_10():
    assert find_primes(10) == [2, 3, 5, 7]
