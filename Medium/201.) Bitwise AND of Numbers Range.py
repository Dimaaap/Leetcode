def range_bitwise_and(left: int, right: int):
    """
    Given two integers left and right that represent the range [left, right],
    return the bitwise AND of all numbers in this range, inclusive.
    """
    counter = 0
    while left != right:
        left >>= 1
        right >>= 1
        counter += 1
    return left << counter


print(range_bitwise_and(5, 7))
print(range_bitwise_and(0, 0))
print(range_bitwise_and(1, 2147483647))