def common_factors(a: int, b: int):
    """
    Given two positive integers a and b, return the number of common factors of a and b.
    An integer x is a common factor of a and b if x divides both a and b.
    """
    counter = 0
    min_num = min(a, b)
    for i in range(1, min_num+1):
        if a % i == 0 and b % i == 0:
            counter += 1
    return counter


print(common_factors(12, 6))
print(common_factors(25, 30))
