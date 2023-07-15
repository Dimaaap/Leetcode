from heapq import nlargest


def third_max(nums: list[int]):
    """
    Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number.
    """
    return nlargest(3, set(nums))[-1] if len(set(nums)) >= 3 else max(nums)


print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))
print(third_max([1, 1, 2]))