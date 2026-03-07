def check_perfect_number(num: int):
    """
    A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the
    number itself. A divisor of an integer x is an integer that can divide x evenly.
    Given an integer n, return true if n is a perfect number, otherwise return false.
    """
    ans = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            ans += i
    return ans == num


print(check_perfect_number(28))
print(check_perfect_number(7))
print(check_perfect_number(99999992))