def minimum_prefix_length(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    You need to remove exactly one prefix (possibly empty) from nums.
    Return an integer denoting the minimum length of the removed prefix such that the remaining array
    is strictly increasing.
    """

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] <= nums[i - 1]:
            return i
    return 0


print(minimum_prefix_length([1, -1, 2, 3, 3, 4, 5]))
print(minimum_prefix_length([4, 3, -2, -5]))
print(minimum_prefix_length([1, 2, 3, 4]))
print(minimum_prefix_length([-4, -10]))