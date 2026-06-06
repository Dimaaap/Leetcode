def digit_frequency_score(n: int) -> int:
    """
    You are given an integer n.
    The score of n is defined as the sum of d * freq(d) over all distinct digits d, where freq(d) denotes the
    number of times the digit d appears in n.
    Return an integer denoting the score of n.
    """

    n = str(n)
    res = 0

    for i in set(n):
        freq = n.count(i) * int(i)
        res += freq
    return res


print(digit_frequency_score(122))
print(digit_frequency_score(101))