import math


def smallest_absent(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    Return the smallest absent positive integer in nums such that it is strictly greater than
    the average of all elements in nums.
    The average of an array is defined as the sum of all its elements divided by the number of elements.
    """

    avg = sum(nums) / len(nums)
    nums = set(nums)

    if avg > 0:
        if int(avg) == avg:
            res = avg + 1
        else:
            res = math.ceil(avg)
    else:
        res = 1

    while res in nums:
        res += 1

    return int(res)


print(smallest_absent([3, 5]))
print(smallest_absent([-1, 1, 2]))
print(smallest_absent([4, -1]))
print(smallest_absent([-34]))
print(smallest_absent([1, -39, 9]))