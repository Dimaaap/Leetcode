def max_product(n: int) -> int:
    """
    You are given a positive integer n.
    Return the maximum product of any two digits in n.
    Note: You may use the same digit twice if it appears more than once in n.
    """
    str_n = str(n)
    n = sorted([int(i) for i in str_n])[::-1]
    return n[0] * n[1]

print(max_product(31))
print(max_product(22))
print(max_product(124))