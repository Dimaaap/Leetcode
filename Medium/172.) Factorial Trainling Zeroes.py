from functools import lru_cache


def trailing_zeroes(n: int) -> int:
    """
    Given an integer n, return the number of trailing zeroes in n!.
    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
    """

    @lru_cache()
    def factorial(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    number = factorial(n)
    if number == 0:
        return 0
    counter = 0
    while True:
        if number % 10 == 0:
            counter += 1
            number = number // 10
        else:
            break
    return counter


print(trailing_zeroes(3))
print(trailing_zeroes(5))
print(trailing_zeroes(0))
print(trailing_zeroes(1574))