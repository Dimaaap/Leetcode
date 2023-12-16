def maximum_difference(nums: list[int]):
    """
    Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j]
    (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
    Return the maximum difference. If no such i and j exists, return -1.
    """
    ans = -1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] - nums[i] > 0 and nums[j] - nums[i] > ans:
                ans = nums[j] - nums[i]
    return ans


print(maximum_difference([7, 1, 5, 4]))
print(maximum_difference([9, 4, 3, 2]))
print(maximum_difference([1, 5, 2, 10]))
