def maximum_gap(nums: list[int]) -> int:
    """
    Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
    If the array contains less than two elements, return 0.
    You must write an algorithm that runs in linear time and uses linear extra space.
    """
    if len(nums) < 2:
        return 0
    gap = 0
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        cur_gap = nums[i + 1] - nums[i]
        gap = max(gap, cur_gap)
    return gap


print(maximum_gap([3, 6, 9, 1]))
print(maximum_gap([10]))
