def mirror_distance(n: int) -> int:
    """
    You are given an integer n.
    Define its mirror distance as: abs(n - reverse(n))
    where reverse(n) is the integer formed by reversing the digits of n.
    Return an integer denoting the mirror distance of n abs(x) denotes the absolute value of x.
    """
    reversed = str(n)[::-1]
    res = abs(n - int(reversed))
    return res


print(mirror_distance(25))
print(mirror_distance(10))
print(mirror_distance(7))