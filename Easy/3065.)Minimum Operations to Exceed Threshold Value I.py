def min_operations(nums: list[int], k: int):
    """
    You are given a 0-indexed integer array nums, and an integer k.

    In one operation, you can remove one occurrence of the smallest element of nums.

    Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
    """
    nums = sorted(nums)
    counter = 0
    while nums[0] < k:
        counter += 1
        nums.pop(0)
    return counter


print(min_operations([2, 11, 10, 1, 3], 10))
print(min_operations([1, 1, 2, 4, 9], 1))
print(min_operations([1, 1, 2, 4, 9], 9))