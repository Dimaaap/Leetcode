from collections import defaultdict


def first_unique_even(nums: list[int]) -> int:
    """
    You are given an integer array nums.

    Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums.
    If no such integer exists, return -1.

    An integer x is considered even if it is divisible by 2.
    """
    counter = defaultdict(int)

    for num in nums:
        if num % 2 == 0:
            counter[num] += 1
    for key, value in dict(counter).items():
        if value == 1:
            return key
    return -1


print(first_unique_even([3, 4, 2, 5, 4, 6]))
print(first_unique_even([4, 4]))