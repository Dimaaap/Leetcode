def is_three(n: int):
    """
    Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
    An integer m is a divisor of n if there exists an integer k such that n = k * m.
    """
    counter = 2
    for number in range(2, n):
        if n % number == 0:
            counter += 1
    return counter == 3


print(is_three(2))
print(is_three(4))