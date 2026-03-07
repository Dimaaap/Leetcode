def hamming_distance(x: int, y: int):
    """
    The Hamming distance between two integers is the number of positions at which the
    corresponding bits are different.
    Given two integers x and y, return the Hamming distance between them.
    """
    ans = 0
    while x or y:
        ans += (x & 1) != (y & 1)
        x >>= 1
        y >>= 1
    return ans


print(hamming_distance(1, 4))
print(hamming_distance(3, 1))