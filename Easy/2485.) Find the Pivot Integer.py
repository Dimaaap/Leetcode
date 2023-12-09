def pivot_integer(n: int):
    """
    Given a positive integer n, find the pivot integer x such that:
        The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
    Return the pivot integer x. If no such integer exists, return -1.
    It is guaranteed that there will be at most one pivot index for the given input.
    """
    for i in range(1, n + 1):
        s1 = sum(range(1, i + 1))
        s2 = sum(range(i, n + 1))
        if s1 == s2:
            return i
    return -1


print(pivot_integer(8))
print(pivot_integer(1))
print(pivot_integer(4))
print(pivot_integer(49))
