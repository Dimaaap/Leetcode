def min_all_one_multiple(k: int) -> int:
    """
    You are given a positive integer k.
    Find the smallest integer n divisible by k that consists of only the digit 1 in its decimal
    representation (e.g., 1, 11, 111, ...).
    Return an integer denoting the number of digits in the decimal representation of n. If no such n exists, return -1.
    """
    if k % 2 == 0 or k % 5 == 0:
        return -1
    rem = 0
    for i in range(k):
        rem = (rem * 10 + 1) % k
        if rem == 0:
            return i + 1
    return -1


print(min_all_one_multiple(3))
print(min_all_one_multiple(7))
print(min_all_one_multiple(2))
print(min_all_one_multiple(5))
print(min_all_one_multiple(8727))