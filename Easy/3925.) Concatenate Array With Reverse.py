def concat_with_reverse(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums of length n.
    Construct a new array ans of length 2 * n such that the first n elements are the same as nums,
    and the next n elements are the elements of nums in reverse order.
    """

    reversed_nums = nums[::-1]
    res = nums + reversed_nums
    return res


print(concat_with_reverse([1, 2, 3]))
print(concat_with_reverse([1]))