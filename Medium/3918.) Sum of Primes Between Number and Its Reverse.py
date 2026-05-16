def sum_of_primes_in_range(n: int) -> int:
    """
    You are given an integer n.
    Let r be the integer formed by reversing the digits of n.
    Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.
    """

    str_n = str(n)
    r = int(str_n[::-1])
    counter = 0

    for i in range(min(n, r), max(n, r) + 1):
        if is_prime(i):
            counter += i
    return counter


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(sum_of_primes_in_range(13))
print(sum_of_primes_in_range(10))
print(sum_of_primes_in_range(8))