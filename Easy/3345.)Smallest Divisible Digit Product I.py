def smallest_number(n: int, t: int) -> int:
    """
    You are given two integers n and t. Return the smallest number greater than or equal to n such that
    the product of its digits is divisible by t.
    """
    for i in range(n, n + 11):
        prod = 1
        for j in str(i):
            prod *= int(j)
        if prod % t == 0:
            return i

print(smallest_number(10, 2))
print(smallest_number(15, 3))