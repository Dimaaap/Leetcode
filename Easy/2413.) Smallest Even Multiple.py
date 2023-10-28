def smallest_even_multiple(n: int):
    """
    Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
    """
    divided = n
    while not(divided % n == 0 and divided % 2 == 0):
        divided += n
    return divided


print(smallest_even_multiple(5))
print(smallest_even_multiple(6))