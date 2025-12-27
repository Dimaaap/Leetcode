def max_total_value(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums of length n and an integer k.
    You need to choose exactly k non-empty subarrays nums[l..r] of nums. Subarrays may overlap, and the exact
    same subarray (same l and r) can be chosen more than once.
    The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
    The total value is the sum of the values of all chosen subarrays.
    Return the maximum possible total value you can achieve.
    """

    max_num, min_num = max(nums), min(nums)
    return (max_num - min_num) * k


print(max_total_value([1, 3, 2], 2))
print(max_total_value([4, 2, 5, 1], 3))