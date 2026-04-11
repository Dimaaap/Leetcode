def check_divisibility(n: int) -> bool:
    """
    You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
`       The digit sum of n (the sum of its digits).
        The digit product of n (the product of its digits).
    Return true if n is divisible by this sum; otherwise, return false.
    """

    str_n = str(n)

    digit_sum = sum(int(i) for i in str_n)
    digit_prod = int(str_n[0])

    for i in str_n[1:]:
        digit_prod *= int(i)

    sum_and_prod = digit_sum + digit_prod
    return n % sum_and_prod == 0


print(check_divisibility(99))
print(check_divisibility(23))
