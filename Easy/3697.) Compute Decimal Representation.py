def decimal_representation(n: int) -> list[int]:
    """
    You are given a positive integer n.
    A positive integer is a base-10 component if it is the product of a single digit from 1 to 9 and a
    non-negative power of 10. For example, 500, 30, and 7 are base-10 components, while 537, 102, and 11 are not.
    Express n as a sum of only base-10 components, using the fewest base-10 components possible.
    Return an array containing these base-10 components in descending order.
    """

    index = 1
    str_n = str(n)
    i = len(str_n) - 1

    res = []

    while i >= 0:
        num = int(str_n[i])
        if num:
            res.append(num * index)
        i -= 1
        index *= 10
    return res[::-1]


print(decimal_representation(537))
print(decimal_representation(102))
print(decimal_representation(6))
