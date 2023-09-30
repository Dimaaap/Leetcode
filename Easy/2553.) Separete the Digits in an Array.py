def separate_digits(nums: list[int]):
    """
    Given an array of positive integers nums, return an array answer that consists of the
     digits of each integer in nums after separating them in the same order they appear in nums.
    To separate the digits of an integer is to get all the digits it has in the same order.
    For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
    """
    res = [int(i) for i in ''.join([str(j) for j in nums])]
    return res


def second_way(nums: list[int]):
    res = []
    for x in nums:
        t = []
        while x > 0:
            x, rest = divmod(x, 10)
            t.insert(0, rest)
        res += t
    return res


print(separate_digits([13, 25, 83, 77]))
print(separate_digits([7, 1, 3, 9]))


print(second_way([13, 25, 83, 77]))
print(second_way([7, 1, 3, 9]))