def count_primes(n: int) -> int:

    """
    Given an integer n, return the number of prime numbers that are strictly less than n.
    """

    if n <= 2:
        return 0

    prime = [True for _ in range(n)]
    counter = 0

    p = 2
    while p * p < n:

        if prime[p]:
            for i in range(p * p, n, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            counter += 1
    return counter


print(count_primes(10))
print(count_primes(2))
print(count_primes(3))
print(count_primes(5))